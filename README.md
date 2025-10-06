# Crawl-cat Crawl4Ai-based documentation extractor
Documentation extraction crawler that uses crawl4ai, LLM capability to analyze schema and select elements, then use DOM selectors for actual content extraction.

# Prerequisites
- pyenv (optional but recommended) to match the project's Python version (see `.python-version` if present)
- Python 3.11+ (the project was tested with pyenv Python 3.13.x)
- An OpenAI API key stored in a `.env` file at the project root as `OPENAI_API_KEY=sk-...`
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

# Running the script

```bash
# main.py will contain minimal GUI in the future
python schema_discovery.py --help
python crawl_cat.py --help
```

# What the script does
- Crawls the OpenAI pricing page (`https://openai.com/api/pricing/`)
- Uses crawl4ai's LLM extraction strategy to extract structured model fee information
- Prints the extracted JSON to stdout


# Internal structure
```text
Root
├── main.py
├── schema_discovery.py 
├── crawl_cat.py
├── save_utils.py
├── requirements.txt
├── .env
├── sources
│   ├── providers.yaml
│   ├── prompt_Unity_Shadergraph_gpt41.md
│   ├── prompt_Unity_Shadergraph_oss.md
│   └── guidance_OpenAI_fees_gpt4o.md
├── schemas
│   ├── openai_price_discovered_model.py
│   └── openai_price_prompt.txt
└── output
```