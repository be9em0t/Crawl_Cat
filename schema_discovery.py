"""Schema discovery helper

- Fetch a target URL and build a schema-generation prompt
- Providers are configured in `providers.yaml`; this script selects a provider
    automatically from that registry (preferring entries with configured env vars).
- Converts JSON Schema to a runtime Pydantic model and optionally emits a Python model file.

Usage examples:

# write prompt only (fetch page and emit prompt to schemas/<base_name>_prompt.txt)
python schema_discovery.py --emit-prompt --out <base_name>

# discover schema from a prompt file (requires provider) and save discovered schema
python schema_discovery.py --prompt my_prompt.txt --emit-schema --out <base_name>

# provide a prompt file and directly emit a model: this will first discover the schema
# from the prompt (equivalent to --emit-schema) and then emit a Pydantic model
python schema_discovery.py --prompt my_prompt.txt --emit-model --out <base_name>

# convert an existing JSON Schema file into a runtime Pydantic model
python schema_discovery.py --schema discovered_schema.json --emit-model --out discovered_schema

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
import yaml
import re

DEFAULT_URL = "https://openai.com/api/pricing/"


def load_providers(providers_path: str) -> Dict[str, Any]:
    if not os.path.exists(providers_path):
        return {}
    with open(providers_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


# Provider resolution is handled by scanning providers.yaml. The script no longer
# accepts provider/token via CLI. See providers.yaml for provider entries and
# the env_var key which names an environment variable containing the token.


async def fetch_url_html(url: str) -> str:
    browser_config = BrowserConfig(headless=True)
    crawler_config = CrawlerRunConfig(cache_mode=CacheMode.BYPASS, word_count_threshold=1, page_timeout=30000)
    async with AsyncWebCrawler(config=browser_config) as crawler:
        result = await crawler.arun(url=url, config=crawler_config)
        return result.cleaned_html or result.html or ""


def build_schema_prompt(url: str, html_snippet: str, guidance: str = None) -> str:
    guidance = guidance or (
        # "Produce a JSON Schema (draft-like) describing the structured information present on the page. "
        # "Return only the JSON Schema object as JSON (no commentary). Include required fields and types. "
        # "Prefer simple types (string, number, boolean, array, object). Add a top-level `examples` key with one example instance."
"""Produce a compact JSON Schema (as a single JSON object) that describes the structured data present on the page. Requirements:

Include top-level title and description keys summarizing the purpose of the object.
For each property under properties include:
type (string, integer, number, boolean, array, object)
description: one concise human-readable sentence describing the field and when it appears
examples: a short array with 1 example value (for objects/arrays include a representative instance)
If the field is an object, provide its own properties, required, and description keys and include examples for nested fields.
If the field is an array, specify items with a type and an examples array showing an example item.
Set required at the top-level and at nested object levels for fields that are always present. Use optional fields only when truly optional.
Keep the schema compact (avoid overly permissive additionalProperties: true unless necessary).
Add a top-level examples array containing one representative complete instance of the object (matching the schema).
Prefer concrete, narrow types (e.g., 'integer' for counts, 'number' for prices, 'string' for textual labels, 'boolean' for flags).
Return only the raw JSON object (no explanation, no markdown/code fences)."""
    )
    # Make the instruction extra-explicit to avoid models wrapping JSON in markdown/code fences.
    guidance = guidance + " Do NOT wrap the JSON in markdown or code fences (e.g. ```json). Return the raw JSON object only, with no surrounding text or formatting."
    prompt = (
        f"You are given the HTML content of a web page (URL: {url}).\n"
        "Analyze the content and propose a compact JSON Schema that describes the "
        "data a user would want to extract from this page (fields, nested objects, arrays).\n\n"
        f"Guidance: {guidance}\n\n"
        "Page HTML (trimmed):\n"
        f"{html_snippet}\n\n"
        "Return a single JSON object (the JSON Schema). Do not include any explanation.\n\n"
        "Additionally, provide a `glossary` object: a list of field entries where each entry contains `name`, `description` (one-line), and `examples` (an array with one example).\n"
        "If you cannot provide all descriptions or examples, return empty strings or empty arrays but keep the fields.\n"
        "Return a single JSON object that may contain both the schema and the glossary under keys `schema` and `glossary`, or return the schema alone - code will attempt to detect both formats."
    )
    return prompt


def extract_json_candidate(text: str):
    """Try a few conservative extraction strategies and return a parsed JSON object or None.

    Strategies (in order):
    - Each fenced code block (```json or ```)
    - The first {...} block
    - The first [...] block
    """
    # fenced code blocks (may be multiple) - try each
    fence_pattern = re.compile(r"```(?:json)?\s*(.*?)\s*```", re.DOTALL | re.IGNORECASE)
    for m in fence_pattern.finditer(text):
        candidate = m.group(1).strip()
        try:
            return json.loads(candidate)
        except Exception:
            continue

    # first {...} object
    first_brace = text.find("{")
    last_brace = text.rfind("}")
    if first_brace != -1 and last_brace != -1 and last_brace > first_brace:
        candidate = text[first_brace:last_brace+1]
        try:
            return json.loads(candidate)
        except Exception:
            pass

    # first [...] array
    first_sq = text.find("[")
    last_sq = text.rfind("]")
    if first_sq != -1 and last_sq != -1 and last_sq > first_sq:
        candidate = text[first_sq:last_sq+1]
        try:
            return json.loads(candidate)
        except Exception:
            pass

    return None


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
    """Emit a Python file with nested Pydantic models for any nested objects/arrays.

    Strategy:
    - Walk the schema recursively and generate a class for any object with `properties`.
    - For arrays whose `items` are objects with `properties`, generate item classes and use List[ItemClass].
    - Name nested classes deterministically using the parent model name and the property name.
    """

    lines: list[str] = []
    header_imports = {"from pydantic import BaseModel, Field", "from typing import Optional, Any"}
    type_imports = set()

    # store generated classes to avoid duplicates
    generated: Dict[str, list[str]] = {}

    def safe_class_name(base: str, prop: str) -> str:
        # build a deterministic class name
        name = f"{base}_{prop.capitalize()}"
        # remove invalid chars
        return re.sub(r"[^0-9A-Za-z_]+", "", name)

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
        # name: class name
        if name in generated:
            return name
        props = schema.get("properties", {})
        required = set(schema.get("required", []))
        class_lines = [f"class {name}(BaseModel):"]
        if not props:
            class_lines.append("    pass")
        for k, spec in props.items():
            # resolve type
            t = spec.get("type", "string")
            if isinstance(t, list):
                t = [x for x in t if x != "null"][0] if "null" in t and len(t) > 1 else t[0]

            # nested object
            if t == "object" and spec.get("properties"):
                nested_name = safe_class_name(name, k)
                process_object(nested_name, spec)
                pytype = nested_name
            # array of objects
            elif t == "array":
                items = spec.get("items", {}) or {}
                it = items.get("type")
                if it == "object" and items.get("properties"):
                    nested_name = safe_class_name(name, k + "Item")
                    process_object(nested_name, items)
                    pytype = f"List[{nested_name}]"
                    type_imports.add("List")
                else:
                    # primitive array
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

    # start processing top-level
    root_name = model_name
    process_object(root_name, jschema)

    # compose header
    lines.extend(sorted(header_imports))
    if type_imports:
        lines.append(f"from typing import {', '.join(sorted(type_imports))}")
    lines.append("")

    # Emit nested classes before classes that reference them to avoid NameError on import.
    # Heuristic: nested/generated helper classes tend to have longer names (e.g. Parent_Child_Item).
    # Sort non-root classes by descending name length (then alphabetically) so dependencies are defined
    # before the classes that reference them. Emit the root class last.
    non_root = [c for c in generated.keys() if c != root_name]
    for cname in sorted(non_root, key=lambda x: (-len(x), x)):
        lines.extend(generated[cname])
        lines.append("")

    # finally emit root class
    lines.extend(generated[root_name])

    # write to file
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


async def main():
    from argparse import RawDescriptionHelpFormatter
    examples = (
        "Usage examples:\n\n"
        "# write prompt only\n"
        "python schema_discovery.py --emit-prompt --out <base_name>\n"
        "# discover schema from a prompt file and save discovered JSON schema\n"
        "python schema_discovery.py --prompt my_prompt.txt --emit-schema --out <base_name>\n"
        "# convert an existing JSON Schema file into a runtime Pydantic model\n"
        "python schema_discovery.py --schema discovered_schema.json --emit-model --out discovered_schema\n"
        "# provide a prompt file and directly emit a Pydantic model\n"
        "python schema_discovery.py --prompt my_prompt.txt --emit-model --out <base_name>\n"
        " \n"
    )
    parser = argparse.ArgumentParser(epilog=examples, formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument("--url", "-u", default=DEFAULT_URL)
    parser.add_argument("--provider", "-p", help="Provider key or alias from providers.yaml (e.g. gpt4o). If omitted, no LLM will be used and LLM-required operations will abort.")
    parser.add_argument("--out", "-o", default="discovered_schema", help="Base name for outputs (no extension). Files will be placed under `schemas/` with suffixes")
    parser.add_argument("--schema", "-is", help="If provided, read JSON Schema from this file and build a runtime Pydantic model")
    parser.add_argument("--prompt", "-ip", help="If provided, read a prompt from this file instead of generating one from a fetched URL/html snippet")
    parser.add_argument("--emit-prompt", "-ep", action="store_true", help="Emit prompt to --out_prompt.txt")
    parser.add_argument("--emit-schema", "-es", action="store_true", help="Emit discovered JSON Schema to --out_discovered_schema.json (requires --provider)")
    parser.add_argument("--emit-model", "-em", action="store_true", help="Create runtime Pydantic model from schema or emitted schema and write Python model file to schemas/<out>_discovered_model.py")
    parser.add_argument("--emit-glossary", action="store_true", help="If set, also save the discovered field glossary to --out_field_glossary.json in addition to appending it to the emitted model.")
    # tolerant extraction is enabled by default; use --strict to disable it
    parser.add_argument("--strict", dest="tolerant", action="store_false", help="Run in strict mode: do not attempt tolerant JSON extraction (opposite of default tolerant behavior)")
    args = parser.parse_args()

    # If the user supplied a prompt file and asked to emit a model, ensure we
    # perform schema discovery first (emit the schema) so the model is created
    # from the discovered schema. If an explicit --schema file was provided,
    # respect that instead.
    if args.prompt and args.emit_model and not args.schema:
        # We still need to run discovery so the model can be generated from the discovered schema,
        # but do not save the schema to disk unless the user explicitly requests --emit-schema.
        print("Notice: --prompt + --emit-model detected. Schema discovery will run to build the model. The schema will not be saved unless you pass --emit-schema.")

    # load providers registry
    providers_path = os.path.join(os.path.dirname(__file__), "providers.yaml")
    providers_registry = load_providers(providers_path)
    regs = providers_registry.get("providers", {})

    provider = None
    api_token = None
    if args.provider:
        provider_input = args.provider
        if provider_input in regs:
            entry = regs[provider_input]
        else:
            # try aliases
            entry = None
            for k, v in regs.items():
                aliases = v.get("aliases") or []
                if provider_input in aliases:
                    entry = v
                    break
            if entry is None:
                print(f"Provider '{provider_input}' not found in providers.yaml. Aborting.")
                return
        provider = entry.get("provider") or provider_input
        env_var = entry.get("env_var")
        if env_var:
            api_token = os.getenv(env_var)

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

    # If user requested discovery (emit_schema or emit_model), ensure we have a provider to call
    if args.emit_schema or args.emit_model:
        if not provider:
            print("No usable provider found in providers.yaml. To run schema discovery you must configure a provider and token in providers.yaml and .env. Aborting.")
            return
        # currently only OpenAI provider interface implemented
        if not provider.startswith("openai"):
            print("Automatic discovery currently only implemented for OpenAI providers. Aborting.")
            return
        model_name = provider.split("/", 1)[-1]
        if not api_token:
            print(f"Provider '{provider}' requires an API token set via the env var referenced in providers.yaml. Aborting.")
            return

        print(f"Calling OpenAI model {model_name} ...")
        try:
            resp_text = await asyncio.to_thread(call_openai, prompt, model_name, api_token)
        except Exception as e:
            print("OpenAI call failed:", e)
            return

        # try to parse returned JSON (supporting either a raw schema or an object containing {schema, glossary})
        try:
            parsed = json.loads(resp_text)
        except Exception:
            # 1) Conservative single outer-fence stripper: if the whole response is a single
            #    fenced block (```json ... ``` or ``` ... ```), strip it and try parsing the inner text.
            outer_fence = re.compile(r"^\s*```(?:json)?\s*(.*?)\s*```\s*$", re.DOTALL | re.IGNORECASE)
            m = outer_fence.match(resp_text)
            if m:
                candidate = m.group(1).strip()
                try:
                    jschema = json.loads(candidate)
                    print("Parsed JSON after removing a single outer code fence. Proceeding.")
                except Exception:
                    jschema = None
            else:
                jschema = None

            # 2) If outer-fence removal succeeded, proceed. Otherwise, offer tolerant extraction only if requested.
            if 'parsed' in locals() and parsed is not None:
                pass
            else:
                # optionally try to extract JSON from common LLM formats when --tolerant is set
                if args.tolerant:
                    repaired = extract_json_candidate(resp_text)
                    if repaired is None:
                        save_text(schema_out, resp_text)
                        print(f"LLM returned non-JSON content and extraction failed. Raw output written to {schema_out}")
                        print("Hint: try inspecting the file for fenced blocks or adjust the prompt to return pure JSON.")
                        return
                    parsed = repaired
                    print("Extracted JSON from LLM response (tolerant mode). Proceeding with schema conversion.")
                else:
                    # Save the raw LLM output for diagnostics
                    save_text(schema_out, resp_text)
                    print(f"LLM returned non-JSON content. Raw output written to {schema_out}")
                    # give a helpful hint if the JSON is inside fenced code blocks
                    fence_pattern = re.compile(r"```(?:json)?\s*(.*?)\s*```", re.DOTALL | re.IGNORECASE)
                    if fence_pattern.search(resp_text):
                        print("Hint: response contains fenced code blocks (```json ... ```). Inspect the saved file and extract the JSON inside the fences.")
                    else:
                        print("Hint: response could not be parsed as JSON. Inspect the saved file to see what's returned by the LLM.")
                    return

        # At this point `parsed` may be the schema object or a wrapper containing schema+glossary
        jschema = None
        glossary = None
        if isinstance(parsed, dict):
            # If parsed contains 'schema' key, use that; otherwise assume it's the schema itself
            if 'schema' in parsed and isinstance(parsed['schema'], dict):
                jschema = parsed['schema']
            else:
                # maybe the model returned the schema directly
                # try to detect whether this dict looks like a JSON Schema (has 'properties' or '$schema')
                if 'properties' in parsed or '$schema' in parsed:
                    jschema = parsed
            # glossary may be present under 'glossary' or 'field_glossary'
            if 'glossary' in parsed:
                glossary = parsed['glossary']
            elif 'field_glossary' in parsed:
                glossary = parsed['field_glossary']

        # if jschema still None, try tolerant extraction for a top-level schema object
        if jschema is None and isinstance(parsed, dict):
            # try to find the first nested dict with 'properties'
            for v in parsed.values():
                if isinstance(v, dict) and 'properties' in v:
                    jschema = v
                    break

        # save schema only when explicitly requested via --emit-schema. If user asked only
        # for --emit-model, discovery will still run (above) but we won't persist the schema.
        if args.emit_schema:
            if jschema is None:
                print("No JSON Schema could be extracted from the LLM response. Raw response saved for inspection.")
                save_text(schema_out, resp_text)
            else:
                save_json(schema_out, jschema)
                print(f"Saved discovered JSON Schema to {schema_out}")

        # Optionally write a separate glossary file if the user explicitly requests it.
        # By default we only append the glossary to the emitted model file for convenience.
        if glossary is not None and args.emit_glossary:
            glossary_out = os.path.join(schemas_dir, f"{base}_field_glossary.json")
            try:
                save_json(glossary_out, glossary)
                print(f"Saved field glossary to {glossary_out}")
            except Exception:
                # fallback: save raw text
                save_text(glossary_out, json.dumps(glossary, ensure_ascii=False, indent=2))

        if args.emit_model:
            if jschema is None:
                print("Cannot build model: no parsed JSON Schema available.")
                return
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

            # append glossary as a JSON comment at end of emitted model for easy editing
            if glossary is not None:
                try:
                    with open(model_out, "a", encoding="utf-8") as mf:
                        mf.write("\n\n# Field glossary (generated by LLM)\n# ````json\n")
                        # write lines prefixed with # for safe inclusion
                        gl_text = json.dumps(glossary, ensure_ascii=False, indent=2)
                        for line in gl_text.splitlines():
                            mf.write("# " + line + "\n")
                        mf.write("# ````\n")
                    print(f"Appended glossary to {model_out}")
                except Exception as e:
                    print("Failed to append glossary to model file:", e)
        return

    # If we reached here, no provider was requested. Prompts may have been emitted above.
    print("No provider requested. Done.")


if __name__ == "__main__":
    asyncio.run(main())
