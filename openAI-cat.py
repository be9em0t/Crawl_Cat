# fetch OpenAI models and their parameters (token window, cost etc.)
# the script can be run either via python openAI-cat.py or be invoked from the main.py GUI
# token should be imported from environment using dotenv.


import os
import sys
import asyncio
import argparse
import json
from save_utils import save_json
from dotenv import load_dotenv
load_dotenv()
import yaml
from bs4 import BeautifulSoup

from typing import Dict, List, Optional
from types import SimpleNamespace
from pydantic import BaseModel, Field
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
from crawl4ai import LLMExtractionStrategy

# user editable vars (defaults)
OUTPUT_FOLDER = "output"
OUTPUT_JSON = "openAI_prices.json"

class OpenAIModelFee(BaseModel):
	# model_name: str = Field(..., description="Name of the OpenAI model.")
	# input_fee: str = Field(..., description="Fee for input token for the OpenAI model.")
	# output_fee: str = Field(
	# 	..., description="Fee for output token for the OpenAI model."
	# )

	# model_name: str = Field(..., description="OpenAI model name")
	# model_group: str = Field(..., description="API group the model belongs to")
	# model_type: str = Field(..., description="The type of content (audio, text etc.)")
	# model_input_fee: str = Field(..., description="The price per input tokens")
	# model_cached_input_fee: str = Field(..., description="The price per cached input tokens")
	# model_output_fee: str = Field(..., description="The price per output tokens")

	pageTitle: Optional[str] = Field(..., description="The title of the web page.")
	mainHeading: Optional[str] = Field(..., description="The main heading of the page.")
	contactSalesLink: Optional[str] = Field(..., description="URL to contact sales for more information.")
	pricingDescription: Optional[str] = Field(..., description="Description of the pricing strategy.")
	pricingOptions: Optional[List[dict]] = Field(..., description="List of available pricing options with descriptions.")

async def extract_structured_data_using_llm(
	provider: str,
	api_token: str = None,
	extra_headers: Dict[str, str] = None,
	strategy: str = "llm",
	css_selector: str = None,
) -> dict:
	print(f"\n--- Extracting Structured Data with {provider} ---")

	# TUNABLE: Provider/token selection
	# - provider: provider string or registry key/alias (resolved in main)
	# - api_token: token used for the chosen provider (from env or --token)
	if api_token is None and provider != "ollama":
		print(f"API token is required for {provider}. Skipping this example.")
		return

	browser_config = BrowserConfig(headless=True)

	# TUNABLE: LLM call parameters
	# - temperature/top_p: control randomness (use 0 for deterministic extraction)
	# - max_tokens: maximum tokens allowed for the extraction response
	extra_args = {"temperature": 0, "top_p": 0.9, "max_tokens": 2000}
	if extra_headers:
		extra_args["extra_headers"] = extra_headers

	# TUNABLE: CrawlerRunConfig and extraction strategy
	# - word_count_threshold / page_timeout: control crawling and time limits
	# - css_selector: when provided, it narrows the DOM region to extract
	crawler_config = CrawlerRunConfig(
		cache_mode=CacheMode.BYPASS,
		word_count_threshold=1,
		page_timeout=80000,
		css_selector=css_selector if css_selector else None,
		# extraction_strategy is None for 'css' flow; LLM flow sets it below
	)

	if strategy == "llm":
		# TUNABLE: Schema and instruction
		# - schema: Pydantic schema that tells the LLM what to output
		# - instruction: the prompt that frames extraction behavior
		llm_strategy = LLMExtractionStrategy(
			# pass a simple object with attributes expected by crawl4ai
			llm_config=SimpleNamespace(
				provider=provider,
				api_token=api_token,
				base_url=None,
				extra_headers=extra_headers or {},
			),
			schema=OpenAIModelFee.model_json_schema(),
			extraction_type="schema",
			instruction=(
				"""From the crawled content, extract all mentioned model names along with their fees for input and output tokens. \nDo not miss any models in the entire content."""
			),
			extra_args=extra_args,
		)
		# attach extraction strategy
		crawler_config.extraction_strategy = llm_strategy

	async with AsyncWebCrawler(config=browser_config) as crawler:
		# TUNABLE: URL
		# - Change this URL to target a different page for extraction
		result = await crawler.arun(url="https://openai.com/api/pricing/", config=crawler_config)

		if strategy == "css":
			# CSS-based extraction: use BeautifulSoup to select elements and return text
			# TUNABLE: css_selector (passed in crawler_config / CLI)
			html = result.cleaned_html or result.html or ""
			soup = BeautifulSoup(html, "html.parser")
			if css_selector:
				elements = soup.select(css_selector)
				parsed = [el.get_text(separator=" ", strip=True) for el in elements]
			else:
				# fallback: return full cleaned HTML as raw
				parsed = {"raw_html": html}
			return parsed

		# default: LLM-based extraction
		try:
			parsed = json.loads(result.extracted_content)
		except Exception:
			parsed = {"raw": result.extracted_content}
		return parsed

if __name__ == "__main__":
	# create parser without automatic -h/--help to control help flag explicitly
	parser = argparse.ArgumentParser(add_help=False)
	# add explicit help flag
	parser.add_argument("--help", "-h", action="help", help="Show this help message and exit")
	parser.add_argument("--out", "-o", help="Optional path to save extracted JSON (overrides defaults)")
	parser.add_argument("--write", "-w", help="Write output to default file (overrides OUTPUT_FOLDER/OUTPUT_JSON)", action="store_true")
	parser.add_argument("--no-write", "-n", help="Do not write output to file; print to console instead", action="store_true")
	parser.add_argument("--provider", "-p", help="LLM provider to use (e.g. openai/gpt-4o or ollama/phi4-mini:latest)", default="openai/gpt-4o")
	parser.add_argument("--token", "-t", help="API token to use (overrides OPENAI_API_KEY from .env)")
	parser.add_argument("--strategy", "-s", help="Extraction strategy: 'llm' (default) or 'css' for CSS selector based extraction", choices=["llm", "css"], default="llm")
	parser.add_argument("--css-selector", "-c", help="When using --strategy css, narrow extraction to this CSS selector (e.g. '.pricing')", default=None)
	parser.add_argument("--list-providers", "-lp", help="List known providers from providers.yaml", action="store_true")
	args = parser.parse_args()

	# load providers registry if available
	providers_registry = {}
	providers_path = os.path.join(os.path.dirname(__file__), "providers.yaml")
	if os.path.exists(providers_path):
		try:
			with open(providers_path, "r", encoding="utf-8") as f:
				providers_registry = yaml.safe_load(f) or {}
		except Exception:
			providers_registry = {}

	if args.list_providers:
		regs = providers_registry.get("providers", {})
		for k, v in regs.items():
			aliases = v.get("aliases") or []
			aliases_str = ", ".join(aliases)
			provider_str = v.get("provider") or ""
			print(f"{k} : {aliases_str} : {provider_str}")
		sys.exit(0)

	# resolve provider and token from registry if a key or alias was provided
	api_token = args.token or os.getenv("OPENAI_API_KEY")
	provider_input = args.provider
	regs = providers_registry.get("providers", {})

	provider = provider_input
	# 1) direct key match
	if provider_input in regs:
		entry = regs[provider_input]
		provider = entry.get("provider") or provider
		env_var = entry.get("env_var")
		if env_var and not args.token:
			api_token = os.getenv(env_var) or api_token
	else:
		# 2) alias match
		found = False
		for k, entry in regs.items():
			aliases = entry.get("aliases") or []
			if provider_input in aliases:
				provider = entry.get("provider") or provider_input
				env_var = entry.get("env_var")
				if env_var and not args.token:
					api_token = os.getenv(env_var) or api_token
				found = True
				break
		# 3) otherwise assume user passed a full provider string (like 'ollama/phi4-mini:latest')
		if not found:
			provider = provider_input
	# wire strategy and css_selector from CLI to the extractor
	parsed = asyncio.run(
		extract_structured_data_using_llm(
			provider, api_token, extra_headers=None, strategy=args.strategy, css_selector=args.css_selector
		)
	)

	# Decide where to write
	if args.no_write:
		# explicitly print to console
		print(json.dumps(parsed, indent=2, ensure_ascii=False))
	else:
		if args.out:
			out_path = args.out
		else:
			# default behavior: write to default file, include provider in filename for clarity
			# sanitize provider label for filesystem safety
			provider_label = provider.replace("/", "_").replace(":", "-").replace(" ", "_")
			base_name = f"{os.path.splitext(OUTPUT_JSON)[0]}_{provider_label}.json"
			out_path = os.path.join(OUTPUT_FOLDER, base_name)

		save_json(out_path, parsed)
		print(f"Saved extracted content to {out_path}")

