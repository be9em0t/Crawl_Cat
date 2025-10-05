"""
Schema discovery helper

- Fetches a target URL using AsyncWebCrawler
- Builds a prompt asking an LLM to propose a JSON Schema for the page's extracted data
- Optionally calls OpenAI (when --provider is given)
- Provider options, aliases and keys are in providers.yaml.
- Provides a safe runtime converter that builds a Pydantic model from a simple JSON Schema using pydantic.create_model
- uses base name for output, to which a suffix is added to reflect the output of each stage

Usage examples:

# write prompt only (no network calls)
python schema_discovery.py --no-call --out <base_name>

# call OpenAI (if openai package installed and OPENAI_API_KEY set or --token provided)
python schema_discovery.py --call --provider openai/gpt-4o --token $OPENAI_API_KEY --out discovered_schema.json

# convert an existing JSON Schema file into a runtime Pydantic model
python schema_discovery.py --schema-file discovered_schema.json --emit-py schemas/discovered_model.py

"""

import os
import sys
import argparse
import json
import asyncio
from typing import Any, Dict

from pydantic import create_model
from save_utils import ensure_dir_for_file, save_json, save_text
from dotenv import load_dotenv

load_dotenv()

from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
from types import SimpleNamespace
import yaml
import re

DEFAULT_URL = "https://openai.com/api/pricing/"


def load_providers(providers_path: str) -> Dict[str, Any]:
    if not os.path.exists(providers_path):
        return {}
    with open(providers_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def resolve_provider(provider_input: str, providers_registry: Dict[str, Any], token_arg: str = None):
    api_token = token_arg or os.getenv("OPENAI_API_KEY")
    regs = providers_registry.get("providers", {})
    provider = provider_input
    if provider_input in regs:
        entry = regs[provider_input]
        provider = entry.get("provider") or provider
        env_var = entry.get("env_var")
        if env_var and not token_arg:
            api_token = os.getenv(env_var) or api_token
    else:
        found = False
        for k, entry in regs.items():
            aliases = entry.get("aliases") or []
            if provider_input in aliases:
                provider = entry.get("provider") or provider_input
                env_var = entry.get("env_var")
                if env_var and not token_arg:
                    api_token = os.getenv(env_var) or api_token
                found = True
                break
        if not found:
            provider = provider_input
    return provider, api_token


async def fetch_url_html(url: str) -> str:
    browser_config = BrowserConfig(headless=True)
    crawler_config = CrawlerRunConfig(cache_mode=CacheMode.BYPASS, word_count_threshold=1, page_timeout=30000)
    async with AsyncWebCrawler(config=browser_config) as crawler:
        result = await crawler.arun(url=url, config=crawler_config)
        return result.cleaned_html or result.html or ""


def build_schema_prompt(url: str, html_snippet: str, guidance: str = None) -> str:
    guidance = guidance or (
        "Produce a JSON Schema (draft-like) describing the structured information present on the page. "
        "Return only the JSON Schema object as JSON (no commentary). Include required fields and types. "
        "Prefer simple types (string, number, boolean, array, object). Add a top-level `examples` key with one example instance."
    )
    prompt = (
        f"You are given the HTML content of a web page (URL: {url}).\n"
        "Analyze the content and propose a compact JSON Schema that describes the "
        "data a user would want to extract from this page (fields, nested objects, arrays).\n\n"
        f"Guidance: {guidance}\n\n"
        "Page HTML (trimmed):\n"
        f"{html_snippet}\n\n"
        "Return a single JSON object (the JSON Schema). Do not include any explanation."
    )
    return prompt


def call_openai(prompt: str, model: str, api_key: str) -> str:
    try:
        import openai
    except Exception as e:
        raise RuntimeError("openai package is not installed. Install it or run with --no-call") from e

    messages = [{"role": "user", "content": prompt}]

    # Prefer the new OpenAI client (openai>=1.0.0)
    if hasattr(openai, "OpenAI"):
        try:
            client = openai.OpenAI(api_key=api_key)
            resp = client.chat.completions.create(model=model, messages=messages, temperature=0)
            # attempt to extract message content in common shapes
            try:
                return resp.choices[0].message.content
            except Exception:
                choice = resp.choices[0]
                if isinstance(choice, dict):
                    return choice.get("message", {}).get("content") or choice.get("text") or json.dumps(choice)
                return str(choice)
        except Exception as e:
            # raise a clearer error so users can see migration guidance
            raise RuntimeError(
                "OpenAI client call failed. If you are using openai>=1.0.0 ensure your API usage matches the new SDK. "
                "See https://github.com/openai/openai-python for migration details. Original error: " + str(e)
            ) from e

    # Fallback to older openai library interface (pre-1.0)
    if api_key:
        openai.api_key = api_key
    try:
        resp = openai.ChatCompletion.create(model=model, messages=messages, temperature=0)
        return resp.choices[0].message.content
    except Exception as e:
        raise RuntimeError(
            "Unable to call OpenAI using either new or legacy client interfaces. "
            "Consider running `openai migrate` or pinning openai==0.28 if you prefer the old API. Original error: " + str(e)
        ) from e


# Simple JSON Schema -> Pydantic create_model converter (recursive)

def jsonschema_type_to_py(t: Dict[str, Any]):
    tpe = t.get("type")
    if isinstance(tpe, list):
        # pick first non-null
        if "null" in tpe and len(tpe) > 1:
            # optional
            non_null = [x for x in tpe if x != "null"]
            tpe = non_null[0]
        else:
            tpe = tpe[0]
    if tpe == "string":
        return str
    if tpe == "integer":
        return int
    if tpe == "number":
        return float
    if tpe == "boolean":
        return bool
    if tpe == "array":
        return list
    if tpe == "object":
        return dict
    return Any


def create_pydantic_model_from_json_schema(jschema: Dict[str, Any], name: str = "DiscoveredModel"):
    """Create a Pydantic model (runtime) from a JSON Schema dict. Handles nested objects recursively."""
    properties = jschema.get("properties", {})
    required = set(jschema.get("required", []))

    fields = {}

    for prop_name, spec in properties.items():
        jtype = spec.get("type", "string")
        if jtype == "object":
            # nested object -> recursive
            nested_name = f"{name}_{prop_name.capitalize()}"
            nested_model = create_pydantic_model_from_json_schema(spec, nested_name)
            pytype = nested_model
            default = ... if prop_name in required else None
            fields[prop_name] = (pytype, default)
        elif jtype == "array":
            items = spec.get("items", {})
            item_type = jsonschema_type_to_py(items)
            if items.get("type") == "object":
                nested_name = f"{name}_{prop_name.capitalize()}Item"
                item_model = create_pydantic_model_from_json_schema(items, nested_name)
                pytype = list[item_model]  # type: ignore
            else:
                pytype = list[item_type]  # type: ignore
            default = ... if prop_name in required else None
            fields[prop_name] = (pytype, default)
        else:
            pytype = jsonschema_type_to_py(spec)
            default = ... if prop_name in required else None
            fields[prop_name] = (pytype, default)

    Model = create_model(name, **fields)
    return Model


def emit_model_py(model_name: str, jschema: Dict[str, Any], out_path: str):
    """Emit a very simple Python file with a Pydantic model declaration (best-effort)."""
    lines = ["from pydantic import BaseModel, Field", "from typing import List, Optional"]
    lines.append("")
    lines.append(f"class {model_name}(BaseModel):")
    props = jschema.get("properties", {})
    required = set(jschema.get("required", []))
    if not props:
        lines.append("    pass")
    for k, spec in props.items():
        jtype = spec.get("type", "string")
        py = "str"
        if jtype == "integer":
            py = "int"
        elif jtype == "number":
            py = "float"
        elif jtype == "boolean":
            py = "bool"
        elif jtype == "array":
            items = spec.get("items", {})
            itype = items.get("type", "string")
            py = f"List[{ 'dict' if itype=='object' else ('str' if itype=='string' else itype) }]"
        elif jtype == "object":
            py = "dict"
        default = "..." if k in required else "None"
        lines.append(f"    {k}: Optional[{py}] = Field({default}, description=\"{spec.get('description','')}\")")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", "-u", default=DEFAULT_URL)
    parser.add_argument("--provider", "-p", help="Provider key or alias from providers.yaml (e.g. gpt4o). If omitted, no LLM will be used and only prompt/schema/model emission flags are valid for local processing.")
    parser.add_argument("--out", "-o", default="discovered_schema", help="Base name for outputs (no extension). Files will be placed under `schemas/` with suffixes")
    parser.add_argument("--schema", "-is", help="If provided, read JSON Schema from this file and build a runtime Pydantic model")
    parser.add_argument("--prompt", "-ip", help="If provided, read a prompt from this file instead of generating one from a fetched URL/html snippet")
    parser.add_argument("--emit-prompt", "-ep", action="store_true", help="Emit prompt to --out_prompt.txt")
    parser.add_argument("--emit-schema", "-es", action="store_true", help="Emit discovered JSON Schema to --out_discovered_schema.json (requires --provider)")
    parser.add_argument("--emit-model", "-em", action="store_true", help="Create runtime Pydantic model from schema or emitted schema and write Python model file to schemas/<out>_discovered_model.py")
    args = parser.parse_args()

    # load providers registry
    providers_path = os.path.join(os.path.dirname(__file__), "providers.yaml")
    providers_registry = load_providers(providers_path)
    regs = providers_registry.get("providers", {})
    provider = None
    api_token = None
    if args.provider:
        # provider must exist in providers.yaml (by key or alias). Fail if not found.
        provider_input = args.provider
        if provider_input in regs:
            entry = regs[provider_input]
            provider = entry.get("provider") or provider_input
            env_var = entry.get("env_var")
            if env_var:
                api_token = os.getenv(env_var)
        else:
            # try aliases
            found = False
            for k, entry in regs.items():
                aliases = entry.get("aliases") or []
                if provider_input in aliases:
                    provider = entry.get("provider") or k
                    env_var = entry.get("env_var")
                    if env_var:
                        api_token = os.getenv(env_var)
                    found = True
                    break
            if not found:
                print(f"Provider '{provider_input}' not found in providers.yaml. Aborting.")
                return

    if args.schema:
        if not os.path.exists(args.schema):
            print(f"Schema file {args.schema} not found")
            return
        with open(args.schema, "r", encoding="utf-8") as f:
            jschema = json.load(f)
        Model = create_pydantic_model_from_json_schema(jschema, "DiscoveredModel")
        print("Created runtime Pydantic model: ", Model)
        if args.emit_model:
            out_py = os.path.join(os.path.dirname(__file__), "schemas", f"{args.out}_discovered_model.py")
            emit_model_py("DiscoveredModel", jschema, out_py)
            print(f"Emitted Python model to {out_py}")
        return

    # prepare outputs under schemas/ using base name from --out
    base = args.out
    schemas_dir = os.path.join(os.path.dirname(__file__), "schemas")
    # ensure directory exists using save_utils helper
    ensure_dir_for_file(os.path.join(schemas_dir, base + "_placeholder"))
    prompt_out = os.path.join(schemas_dir, f"{base}_prompt.txt")
    schema_out = os.path.join(schemas_dir, f"{base}_discovered_schema.json")
    model_out = os.path.join(schemas_dir, f"{base}_discovered_model.py")

    # If provider present we will call the LLM to produce a schema from the fetched HTML or provided prompt.
    # If no provider is given, this script only supports local operations (emit prompt from fetched URL, or convert existing schema to model).

    # generate or read prompt
    if args.prompt:
        if not os.path.exists(args.prompt):
            print(f"Prompt file {args.prompt} not found")
            return
        with open(args.prompt, "r", encoding="utf-8") as f:
            prompt = f.read()
    else:
        # fetch page html and build prompt
        print(f"Fetching {args.url} ...")
        html = await fetch_url_html(args.url)
        snippet = html[:6000]
        prompt = build_schema_prompt(args.url, snippet)

    # write prompt if requested
    if args.emit_prompt:
        save_text(prompt_out, prompt)
        print(f"Prompt written to {prompt_out}")

    # If provider requested, call LLM to get schema and emit schema/model as requested
    if provider:
        # currently only OpenAI provider interface implemented
        if not provider.startswith("openai"):
            print("Automatic call currently only implemented for OpenAI providers. Aborting.")
            return
        model_name = provider.split("/", 1)[-1]
        if not api_token:
            print("No API token configured for provider in providers.yaml (env var may be missing). Aborting.")
            return
        print(f"Calling OpenAI model {model_name} ...")
        try:
            resp_text = await asyncio.to_thread(call_openai, prompt, model_name, api_token)
        except Exception as e:
            print("OpenAI call failed:", e)
            return

        # try to parse returned JSON
        try:
            jschema = json.loads(resp_text)
        except Exception:
            print("LLM returned non-JSON content. Aborting.")
            return

        # save schema if requested
        if args.emit_schema or args.emit_model:
            save_json(schema_out, jschema)
            print(f"Saved discovered JSON Schema to {schema_out}")

        if args.emit_model:
            print("Building runtime Pydantic model from schema...")
            Model = create_pydantic_model_from_json_schema(jschema, "DiscoveredModel")
            # set module name for nicer repr
            module_name = "schemas.discovered_model"
            try:
                Model.__module__ = module_name
            except Exception:
                pass
            print("Runtime model created:", Model)
            emit_model_py("DiscoveredModel", jschema, model_out)
            print(f"Emitted Python model to {model_out}")
        return

    # If we reached here, no provider was requested. Prompts may have been emitted above.
    print("No provider requested. Done.")


if __name__ == "__main__":
    asyncio.run(main())
