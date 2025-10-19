# crawl-cat (crawl-cat2)

Minimal, actionable README for automated/AI consumption.

## Quickstart (concise)
- Ensure Python 3.11+ and dependencies from `requirements.txt` are installed.
- Put provider API keys in a `.env` at project root and configure `providers.yaml`.
- Run a source from `config.yaml`:

```bash
python crawl-cat2.py -cfg config.yaml -id shadergraph_content_dom
```

## Core concepts (short)
- Workflows: `explore`, `llm`, `dom`, `html`.
- Config: `config_<name>.yaml` contains `sources` (list). Each source declares extraction schemas and options.
- Extraction schemas: `category_schema`, `node_schema`, `node_detail_schema` (each a CSS-based schema used by crawl4ai).

## Important config knobs (concise)
- Output naming: `out_file` is combined with `workflow` and `.json` is appended. If `out_folder` set, output saved there.
- Debug: `save_debug_nodes: true` writes debug JSON; `debug_file` overrides filename.
- Node expansion: `expand_nodes: true` enables node extraction; `capture_nodes_on_category_page` (default true) controls whether to treat category-page nodes as final or follow `node_url`.
- Crawl detail pages: `crawl_node_pages: true` + `node_detail_schema` will fetch and merge detail info.

## Filters & name preservation (machine-oriented)
- Filters can be declared at schema-level or source-level. Source-level overrides schema-level.
  - Schema-level example (inside `node_detail_schema`):
    - `include_fields: ["description"]`
    - `exclude_fields: ["other_field"]`
  - Source-level example (top-level under a `sources` entry):
    - `exclude_fields: ["description"]`
- Precedence: `include_fields` > `exclude_fields`. If `include_fields` exists, only those fields are kept.
- Name preservation:
  - Default behavior: detail-page `name` is removed to avoid conflict; `node_name` from category page is canonical.
  - To preserve detail `name`: set `node_detail_schema.preserve_name: true` or `preserve_detail_name: true` at source-level.

## Add a new source (checklist)
1. Duplicate an existing `sources` entry in `config_*.yaml`.
2. Set `id`, `url` (and optional `urls`).
3. Provide `category_schema` and `node_schema` (CSS selectors + `fields`).
4. If you need detailed node pages, add `node_detail_schema` and set `crawl_node_pages: true`.
5. Tune `include_fields` / `exclude_fields` and `preserve_name` as needed.
6. Run the script with `-cfg` and `-id`.

## Output expectations
- JSON structure: a list of category objects. Each category may contain `nodes` (list of node dicts). Node keys commonly include `node_name`, `node_url`, `description`, `summary`.
- `exclude_fields` will remove keys from node objects; `include_fields` restricts to listed keys.

Note on post-processing:
- Extracted category and node/function names are cleaned (trailing pilcrow `¶` characters removed and whitespace trimmed).
- Relative URLs found in extracted fields (for example `function_url` or `node_url`) are automatically resolved to absolute URLs using the category URL or the source URL as the base. This ensures output contains full, directly-usable links.

## Troubleshooting
- If descriptions are empty, adjust `node_detail_schema.baseSelector` to narrower selector (e.g., `#_content`) and `description` selector (e.g., `h1:first-of-type ~ p, h2:first-of-type ~ p`).

---
This README is intentionally concise so an automated agent can resume work (add sources, tweak schemas, run crawls).