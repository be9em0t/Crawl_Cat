# openAI-cat LLM extraction

This small project contains a minimal script `openAI-cat.py` that runs the "LLM Extraction Example" from Crawl4AI.

Prerequisites
- pyenv (optional but recommended) to match the project's Python version (see `.python-version` if present)
- Python 3.11+ (the project was tested with pyenv Python 3.13.x)
- An OpenAI API key stored in a `.env` file at the project root as `OPENAI_API_KEY=sk-...`

Install dependencies

Use the included `requirements.txt`:

```bash
python -m pip install -r requirements.txt
```

If you use pyenv and want to activate the project's Python version:

```bash
pyenv shell $(cat .python-version)
```

Playwright browsers

If you haven't installed Playwright browsers (used by crawl4ai), run:

```bash
python -m playwright install
```

Running the script

From the project root run:

```bash
py openAI-cat.py
```

Or from a subfolder (example):

```bash
py ../../openAI-cat.py
```

What the script does
- Crawls the OpenAI pricing page (`https://openai.com/api/pricing/`)
- Uses crawl4ai's LLM extraction strategy to extract structured model fee information
- Prints the extracted JSON to stdout

Troubleshooting
- Missing API key: ensure `.env` contains `OPENAI_API_KEY`.
- Playwright errors: ensure browsers are installed (`python -m playwright install`).
- Dependency issues: create a fresh venv/pyenv and install `requirements.txt`.

# Internal logic

