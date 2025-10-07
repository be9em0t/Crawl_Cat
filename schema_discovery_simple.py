"""Simplified schema discovery

Workflow (single path):
1. Fetch URL HTML -> build prompt -> save prompt to schemas/{base}_prompt.txt
2. Call LLM (provider) with the prompt -> expect raw JSON Schema -> save to schemas/{base}_schema.json
3. Convert JSON Schema to Pydantic model -> write to schemas/{base}_model.py

This script intentionally omits all other execution paths, tolerant extraction, and
fallbacks. Any unexpected condition fails quickly with a short error message.
"""
import os
import sys
import json
import asyncio
from typing import Any, Dict

from dotenv import load_dotenv
load_dotenv()

from save_utils import ensure_dir_for_file, save_json, save_text

import yaml
import re

# Crawl helper (uses crawl4ai available in this repo environment)
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode

DEFAULT_URL = "https://openai.com/api/pricing/"

# MARK FOR DELETION - unused duplicate
def load_providers(providers_path: str) -> Dict[str, Any]:
    if not os.path.exists(providers_path):
        return {}
    with open(providers_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}

# MARK FOR DELETION - unused duplicate
async def fetch_url_html(url: str) -> str:
    browser_config = BrowserConfig(headless=True)
    crawler_config = CrawlerRunConfig(cache_mode=CacheMode.BYPASS, word_count_threshold=1, page_timeout=30000)
    async with AsyncWebCrawler(config=browser_config) as crawler:
        result = await crawler.arun(url=url, config=crawler_config)
        return result.cleaned_html or result.html or ""

# MARK FOR DELETION - unused duplicate
def build_schema_prompt(url: str, html_snippet: str) -> str:
    guidance = (
        "Produce a compact JSON Schema (as a single JSON object) that describes the structured data present on the page. "
        "Return only the raw JSON object (no explanation, no markdown or fences). Include a top-level `examples` array with one example instance. "
        "Ensure the schema contains a `models` array describing model entries when present on the page."
    )
    guidance = guidance + " Do NOT wrap the JSON in markdown or code fences. Return the raw JSON object only."
    prompt = (
        f"You are given the HTML content of a web page (URL: {url}).\n"
        "Analyze the content and propose a compact JSON Schema that describes the data a user would want to extract from this page.\n\n"
        f"Guidance: {guidance}\n\n"
        "Page HTML (trimmed):\n"
        f"{html_snippet}\n\n"
        "Return a single JSON object (the JSON Schema). Do not include any explanation."
    )
    return prompt

# MARK FOR DELETION - unused duplicate
def call_openai(prompt: str, model: str, api_key: str) -> str:
    try:
        import openai
    except Exception:
        raise RuntimeError("openai package is not installed")

    messages = [{"role": "user", "content": prompt}]

    # Prefer the new OpenAI client (openai>=1.0.0)
    if hasattr(openai, "OpenAI"):
        client = openai.OpenAI(api_key=api_key)
        resp = client.chat.completions.create(model=model, messages=messages, temperature=0)
        # extract primary message content
        try:
            return resp.choices[0].message.content
        except Exception:
            choice = resp.choices[0]
            if isinstance(choice, dict):
                return choice.get("message", {}).get("content") or choice.get("text") or json.dumps(choice)
            return str(choice)

    # fallback to legacy interface
    openai.api_key = api_key
    resp = openai.ChatCompletion.create(model=model, messages=messages, temperature=0)
    return resp.choices[0].message.content

# MARK FOR DELETION - unused duplicate
# Minimal JSON Schema -> Pydantic model generator (emit file)
from pydantic import create_model
import re as _re


def jsonschema_type_to_py(t: Dict[str, Any]):
    typ = t.get("type")
    if isinstance(typ, list):
        if "null" in typ and len(typ) > 1:
            non_null = [x for x in typ if x != "null"]
            typ = non_null[0]
        else:
            typ = typ[0]
    return {
        "string": str,
        "integer": int,
        "number": float,
        "boolean": bool,
        "array": list,
        "object": dict,
    }.get(typ, Any)

# MARK FOR DELETION - unused duplicate
def create_pydantic_model_from_json_schema(jschema: Dict[str, Any], name: str = "DiscoveredModel"):
    properties = jschema.get("properties", {})
    required = set(jschema.get("required", []))
    fields = {}
    for prop_name, spec in properties.items():
        jtype = spec.get("type", "string")
        if jtype == "object":
            nested_name = f"{name}_{prop_name.capitalize()}"
            nested_model = create_pydantic_model_from_json_schema(spec, nested_name)
            pytype = nested_model
            default = ... if prop_name in required else None
            fields[prop_name] = (pytype, default)
        elif jtype == "array":
            items = spec.get("items", {})
            if items.get("type") == "object":
                nested_name = f"{name}_{prop_name.capitalize()}Item"
                item_model = create_pydantic_model_from_json_schema(items, nested_name)
                pytype = list[item_model]  # type: ignore
            else:
                item_type = jsonschema_type_to_py(items)
                pytype = list[item_type]  # type: ignore
            default = ... if prop_name in required else None
            fields[prop_name] = (pytype, default)
        else:
            pytype = jsonschema_type_to_py(spec)
            default = ... if prop_name in required else None
            fields[prop_name] = (pytype, default)

    Model = create_model(name, **fields)
    return Model

# MARK FOR DELETION - unused duplicate
def emit_model_py(model_name: str, jschema: Dict[str, Any], out_path: str):
    lines: list[str] = []
    header_imports = {"from pydantic import BaseModel, Field", "from typing import Optional, Any"}
    type_imports = set()
    generated: Dict[str, list[str]] = {}

    def safe_class_name(base: str, prop: str) -> str:
        name = f"{base}_{prop.capitalize()}"
        return _re.sub(r"[^0-9A-Za-z_]+", "", name)

    def render_field_args(spec: Dict[str, Any], required: bool) -> str:
        default = "..." if required else "None"
        desc = spec.get("description", "")
        example = spec.get("examples")
        field_args = f"{default}, description=\"{desc}\""
        if example:
            try:
                ex = json.dumps(example[0], ensure_ascii=False)
                field_args = f"{default}, description=\"{desc}\", example={ex}"
            except Exception:
                pass
        return field_args

    def process_object(name: str, schema: Dict[str, Any]):
        if name in generated:
            return name
        props = schema.get("properties", {})
        required = set(schema.get("required", []))
        class_lines = [f"class {name}(BaseModel):"]
        if not props:
            class_lines.append("    pass")
        for k, spec in props.items():
            t = spec.get("type", "string")
            if isinstance(t, list):
                t = [x for x in t if x != "null"][0] if "null" in t and len(t) > 1 else t[0]

            if t == "object" and spec.get("properties"):
                nested_name = safe_class_name(name, k)
                process_object(nested_name, spec)
                pytype = nested_name
            elif t == "array":
                items = spec.get("items", {}) or {}
                it = items.get("type")
                if it == "object" and items.get("properties"):
                    nested_name = safe_class_name(name, k + "Item")
                    process_object(nested_name, items)
                    pytype = f"List[{nested_name}]"
                    type_imports.add("List")
                else:
                    itype = items.get("type", "string")
                    py_primitive = {
                        "string": "str",
                        "integer": "int",
                        "number": "float",
                        "boolean": "bool",
                    }.get(itype, "Any")
                    pytype = f"List[{py_primitive}]"
                    type_imports.add("List")
            else:
                pytype = {
                    "string": "str",
                    "integer": "int",
                    "number": "float",
                    "boolean": "bool",
                    "object": "dict",
                }.get(t, "Any")

            if pytype.startswith("List["):
                type_imports.add("List")
            type_imports.add("Optional")

            field_args = render_field_args(spec, k in required)
            class_lines.append(f"    {k}: Optional[{pytype}] = Field({field_args})")

        generated[name] = class_lines
        return name

    root_name = model_name
    process_object(root_name, jschema)

    lines.extend(sorted(header_imports))
    if type_imports:
        lines.append(f"from typing import {', '.join(sorted(type_imports))}")
    lines.append("")

    non_root = [c for c in generated.keys() if c != root_name]
    for cname in sorted(non_root, key=lambda x: (-len(x), x)):
        lines.extend(generated[cname])
        lines.append("")

    lines.extend(generated[root_name])

    ensure_dir_for_file(out_path)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


# MARK FOR DELETION - unused duplicate
async def main():
    import argparse
    parser = argparse.ArgumentParser(description="Simplified schema discovery: fetch URL, build prompt, get JSON schema from provider, emit pydantic model")
    parser.add_argument("--url", "-u", default=DEFAULT_URL)
    parser.add_argument("--provider", "-p", required=True, help="Provider key from providers.yaml (e.g. gpt4o)")
    parser.add_argument("--out", "-o", default="discovered", help="Base name for outputs (no extension). Files are placed under schemas/ as {base}_prompt.txt, {base}_schema.json, {base}_model.py")
    args = parser.parse_args()

    # load providers
    providers_path = os.path.join(os.path.dirname(__file__), "providers.yaml")
    providers_registry = load_providers(providers_path)
    regs = providers_registry.get("providers", {})
    entry = None
    # direct key match
    if args.provider in regs:
        entry = regs[args.provider]
    else:
        # try aliases
        for k, v in regs.items():
            aliases = v.get("aliases") or []
            if args.provider in aliases:
                entry = v
                break
    if entry is None:
        print("Provider not found in providers.yaml")
        sys.exit(1)
    provider = entry.get("provider") or args.provider
    env_var = entry.get("env_var")
    if not env_var:
        print("Provider entry missing env_var in providers.yaml")
        sys.exit(1)
    api_token = os.getenv(env_var)
    if not api_token:
        print("Provider API token not set in environment")
        sys.exit(1)

    if not provider.startswith("openai"):
        print("Only OpenAI-style providers are supported in this simplified script")
        sys.exit(1)

    base = args.out
    schemas_dir = os.path.join(os.path.dirname(__file__), "schemas")
    prompt_out = os.path.join(schemas_dir, f"{base}_prompt.txt")
    schema_out = os.path.join(schemas_dir, f"{base}_schema.json")
    model_out = os.path.join(schemas_dir, f"{base}_model.py")

    # fetch page and build prompt
    html = await fetch_url_html(args.url)
    snippet = html[:6000]
    prompt = build_schema_prompt(args.url, snippet)

    # save prompt
    save_text(prompt_out, prompt)
    print(f"Prompt written to {prompt_out}")

    # call provider
    model_name = provider.split("/", 1)[-1]
    resp_text = await asyncio.to_thread(call_openai, prompt, model_name, api_token)

    # parse response strictly as JSON
    try:
        jschema = json.loads(resp_text)
    except Exception:
        print("LLM returned non-JSON content; aborting")
        sys.exit(1)

    # save schema
    save_json(schema_out, jschema)
    print(f"Saved JSON Schema to {schema_out}")

    # build runtime model and emit python module
    Model = create_pydantic_model_from_json_schema(jschema, "DiscoveredModel")
    emit_model_py("DiscoveredModel", jschema, model_out)
    print(f"Emitted Pydantic model to {model_out}")


if __name__ == "__main__":
    asyncio.run(main())