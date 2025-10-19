# Name
crawl-cat2.py

# Crawl-cat Crawl4Ai-based documentation extractor
Documentation extraction crawler that uses crawl4ai, LLM capability to analyze schema and select elements, then use DOM selectors for actual content extraction.

# Prerequisites
- pyenv to match the project's Python version (see `.python-version` if present)
- Python 3.11+ (the project was tested with pyenv Python 3.13.x)
- An API keys stored in a `.env` file at the project root
- Crawl4Ai installed and verified.

## Verify Crawl4ai install:
```
# Install the package
pip install -U crawl4ai

# For pre release versions
pip install crawl4ai --pre

# Run post-installation setup
crawl4ai-setup

# Verify your installation
crawl4ai-doctor
```

## Install dependencies

Use the included `requirements.txt`:

```bash
python -m pip install -r requirements.txt
```

If you use pyenv and want to activate the project's Python version:

```bash
pyenv shell $(cat .python-version)
```

# What the script does
- Crawls page(s)
- May use user-supplied pythonic model
- Uses crawl4ai's extraction strategies to extract structured information
- Supports different workflows
    - explore (explore the structure using CSS selectors)
    - llm (ai-assisted extraction)
    - dom (or css) - non-ai extraction
    - html - page extraction for loacal processing
- Prints the extracted information to stdout
- Saves to JSON, markdown, HTML (depending on yaml settings)


# Internal structure
```text
Root
├── .env
├── requirements.txt
├── config_<1>.yaml 
├── config_<2>.yaml 
├── providers.yaml
├── crawl_cat2.py
├── save_utils.py
├── main.py
└── output
```


# Usage

## Running the script

Usage examples:
  python crawl-cat2.py -cfg config_openai_fees.yaml
  python crawl-cat2.py -cfg config_openai_fees.yaml -id openai_fees_or-gpt4o-mini

Required files:
- config_<name>.yaml: Configuration file with sources, URLs, models, etc.
- providers.yaml: Provider definitions with LLM aliases and API keys reference

## Field filters and detail-name preservation

You can control which fields are included in the final extracted node objects using simple filters in your YAML config. Filters can be placed at two levels:

- Schema-level (recommended when the filter is specific to a particular extraction schema):
  - Add `include_fields` or `exclude_fields` inside a schema object such as `node_detail_schema`.
  - Example:
    ```yaml
    node_detail_schema:
      baseSelector: "#_content"
      fields:
        - name: "description"
          selector: "h1:first-of-type ~ p"
          type: "text"
      include_fields: ["description"]
    ```

- Source-level (overrides schema-level and applies to the whole source):
  - Add `include_fields` or `exclude_fields` at the top-level of a `sources` entry.
  - Example:
    ```yaml
    - id: houdini21_content_dom_minimal
      exclude_fields:
        - description
    ```

Precedence rules
- If both schema-level and source-level filters exist, the source-level filters take precedence.
- `include_fields` has higher precedence than `exclude_fields` — if `include_fields` is present, only those fields will be kept.

Detail-page name preservation
- By default the crawler treats the category page `node_name` as the canonical name and will remove any `name` extracted from a node detail page to avoid duplication or conflicts.
- To override this behavior you can set either:
  - `node_detail_schema.preserve_name: true` (schema-level)
  - `preserve_detail_name: true` (source-level)

This makes the extraction flexible: keep `name` when detail pages are authoritative, or drop it when category pages already provide the canonical `node_name`.