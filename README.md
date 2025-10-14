# Name
crawl-cat.py

# Crawl-cat Crawl4Ai-based documentation extractor
Documentation extraction crawler that uses crawl4ai CLI, LLM capability to analyze schema and select elements, then use DOM selectors for actual content extraction.

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
├── providers.yaml
├── crawl_cat.py
├── save_utils.py
└── output
```


# CRWL CLI Overview

The Crawl4ai CLI (`crwl`) provides a command-line interface for web crawling and data extraction. Below are the possible YAML configuration files you can use for different scenarios:

## Core Configuration Files

1. **`browser.yml`** - Browser settings
   ```yaml
   headless: true
   viewport_width: 1280
   user_agent_mode: "random"
   verbose: true
   ignore_https_errors: true
   ```

2. **`crawler.yml`** - Crawling behavior
   ```yaml
   cache_mode: "bypass"
   wait_until: "networkidle"
   page_timeout: 30000
   delay_before_return_html: 0.5
   word_count_threshold: 100
   scan_full_page: true
   scroll_delay: 0.3
   process_iframes: false
   remove_overlay_elements: true
   magic: true
   verbose: true
   css_selector: "#content"  # Optional: limit content to specific element
   ```

3. **`extract.yml`** - Extraction configuration (for structured data)
   ```yaml
   # For CSS/XPath extraction
   type: "json-css"
   params:
     verbose: true
   
   # For LLM extraction
   type: "llm"
   provider: "openrouter/openai/gpt-4o-mini"
   instruction: "Extract all articles with titles and links"
   api_token: "${OPENROUTER_API_KEY}"
   params:
     temperature: 0.3
     max_tokens: 1000
   ```

4. **`filter.yml`** - Content filtering
   ```yaml
   # BM25 filtering
   type: "bm25"
   query: "target content"
   threshold: 1.0
   
   # Pruning filtering
   type: "pruning"
   query: "focus topic"
   threshold: 0.48
   ```

## Schema Files (JSON)

5. **`schema.json`** - Pydantic schema for structured extraction
   ```json
   {
     "name": "ArticleExtractor",
     "baseSelector": ".article",
     "fields": [
       {
         "name": "title",
         "selector": "h1.title",
         "type": "text"
       }
     ]
   }
   ```

## Global Configuration

6. **`~/.crawl4ai/global.yml`** - Global settings and API keys
   ```yaml
   llm:
     provider: "openrouter/openai/gpt-4o-mini"
     api_token: "${OPENROUTER_API_KEY}"
   
   browser:
     headless: true
     viewport_width: 1920
   ```

## Usage Scenarios

- **Basic crawling**: No YAML files needed
- **DOM extraction**: `crawler.yml` (with `css_selector`)
- **LLM extraction**: `extract.yml` + `schema.json` + global config
- **CSS structured extraction**: `extract.yml` + `schema.json`
- **Filtered content**: Any of above + `filter.yml`
- **Custom browser**: Any of above + `browser.yml`

## CLI Command Patterns

```bash
# Basic
crwl https://example.com

# With configs
crwl https://example.com -B browser.yml -C crawler.yml -e extract.yml -s schema.json -f filter.yml -o json
```

# Simplified Wrapper Script

For easier usage, use the `crawl_cat.py` wrapper script that reads all configuration from a single YAML file instead of multiple separate files.

## Wrapper Script Usage

```bash
# Basic usage with config file (single source)
python crawl_cat.py -cfg config_shadergraph.yaml

# With custom source ID (for multiple sources in config)
python crawl_cat.py -cfg config_shadergraph.yaml -id shadergraph_toc
python crawl_cat.py -cfg config_shadergraph.yaml -id shadergraph_content
```

The wrapper script displays a **configuration summary** before starting the crawler, allowing you to verify your settings:

```
🔧 Configuration Summary:
   URL: https://docs.unity3d.com/Packages/com.unity.shadergraph@17.4/manual/Node-Library.html
   Output Format: markdown
   Save Path: output/shadergraph_toc.md
   Browser: viewport=1280, headless=True
   Crawler: css_selector=#toc, cache_mode=BYPASS
🚀 Starting crawler...
```

## Multiple Sources Example

The `config_shadergraph.yaml` demonstrates multiple sources in action:

- **`shadergraph_toc`**: Extracts only the table of contents using `css_selector: "#toc"`
- **`shadergraph_content`**: Extracts the full page content (no CSS selector for comprehensive extraction)

## Single Config File Structure

The wrapper script supports both single source and multiple sources configurations:

### Single Source Format
```yaml
# Direct configuration for single source
url: "https://example.com"
output_format: "markdown"
save: "my_output"  # Optional: auto-generates "my_output.md"
verbose: true
bypass_cache: true

browser:
  viewport_width: 1280
  user_agent_mode: "random"

crawler:
  css_selector: "#content"
  cache_mode: "BYPASS"
  # ... other crawler settings
```

### Multiple Sources Format
```yaml
# Global settings (applied to all sources unless overridden)
save_folder: "output"  # All outputs go to ./output/ folder

# Multiple sources configuration
sources:
  - id: "source_one"
    save: "toc_output"  # Saves as "output/toc_output.md"
    url: "https://example.com/page1"
    output_format: "markdown"
    verbose: true
    bypass_cache: true
    
    browser:
      viewport_width: 1280
      user_agent_mode: "random"
    
    crawler:
      css_selector: "#toc"
      cache_mode: "BYPASS"
  
  - id: "source_two"
    save: "full_content"  # Saves as "output/full_content.md"
    url: "https://example.com/page2"
    output_format: "json"
    verbose: true
    bypass_cache: true
    
    browser:
      viewport_width: 1920
      user_agent_mode: "random"
    
    crawler:
      # No css_selector = extract full page
      cache_mode: "BYPASS"
```

## Benefits of Wrapper Script

- **Single file configuration**: All settings in one YAML file instead of 4-5 separate files
- **Multiple sources support**: Define multiple extraction targets in one config with custom IDs
- **Automatic file saving**: Use `save` field to automatically generate output filenames with correct extensions
- **Automatic cleanup**: Temporary files are created and cleaned up automatically
- **Consistent CLI calls**: Standardized command generation for all scenarios
- **Source selection**: Use `-id source_name` to run specific extractions from multi-source configs

## Automatic File Saving

Each source can specify a `save` field that automatically generates the output filename:

```yaml
# Global settings (applied to all sources)
save_folder: "output"  # Optional: saves all files to ./output/ folder

sources:
  - id: "my_extraction"
    save: "my_output"        # Base filename
    output_format: "markdown" # Format: markdown, json, html
    save_folder: "custom"    # Optional: override global folder
    # Result: "custom/my_output.md" (or "output/my_output.md" if no override)
```

**Supported formats and extensions:**
- `markdown` / `md` → `.md`
- `json` → `.json` 
- `html` → `.html`
- Other formats → `.txt`

**Save folder hierarchy:**
1. Per-source `save_folder` (highest priority)
2. Global `save_folder` (middle priority)  
3. Current directory (default)

## Example Config Files

- `config_shadergraph.yaml` - Unity ShaderGraph documentation extraction
- `config_unity_shadergraph.yaml` - Alternative ShaderGraph config (legacy format)

# Usage

## Running the script

Usage examples:
  python crawl-cat2.py -cfg config_openai_fees.yaml
  python crawl-cat2.py -cfg config_openai_fees.yaml -id openai_fees_or-gpt4o-mini

Required files:
- config_<name>.yaml: Configuration file with sources, URLs, models, etc.
- providers.yaml: Provider definitions with LLM aliases and API keys reference

## Yaml - Extracion filters
... document consizely at some point ...