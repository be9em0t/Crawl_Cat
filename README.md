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