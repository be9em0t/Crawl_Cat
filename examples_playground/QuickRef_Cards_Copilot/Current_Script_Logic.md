Script logic (high level)

- The script crawls a target web page (currently hardcoded to [https://openai.com/api/pricing/](vscode-file://vscode-app/Users/dunevv/Applications/VS%20Code%20Portable/Visual%20Studio%20Code.app/Contents/Resources/app/out/vs/code/electron-browser/workbench/workbench.html)) using Crawl4AI's AsyncWebCrawler.
- It converts page content to markdown/clean HTML internally and passes selected content to an extraction strategy.
- The extraction is performed by the LLMExtractionStrategy: an LLM is used to parse the crawled content and produce structured JSON according to the provided Pydantic schema ([OpenAIModelFee](vscode-file://vscode-app/Users/dunevv/Applications/VS%20Code%20Portable/Visual%20Studio%20Code.app/Contents/Resources/app/out/vs/code/electron-browser/workbench/workbench.html)).
- The extracted JSON is returned to the caller and (by default) saved to a provider-labeled JSON file under [output](vscode-file://vscode-app/Users/dunevv/Applications/VS%20Code%20Portable/Visual%20Studio%20Code.app/Contents/Resources/app/out/vs/code/electron-browser/workbench/workbench.html).

Key internal parameters that affect results and where to change them

- URL (what to crawl)
    
    - Location: inside [extract_structured_data_using_llm](vscode-file://vscode-app/Users/dunevv/Applications/VS%20Code%20Portable/Visual%20Studio%20Code.app/Contents/Resources/app/out/vs/code/electron-browser/workbench/workbench.html) when calling [crawler.arun(url=...)](vscode-file://vscode-app/Users/dunevv/Applications/VS%20Code%20Portable/Visual%20Studio%20Code.app/Contents/Resources/app/out/vs/code/electron-browser/workbench/workbench.html).
    - Effect: Changing URL changes the entire source content; make sure the page contains the data you're targeting.
- LLM Provider and Token
    
    - CLI flags: `--provider/-p` and `--token/-t` (or use [providers.yaml](vscode-file://vscode-app/Users/dunevv/Applications/VS%20Code%20Portable/Visual%20Studio%20Code.app/Contents/Resources/app/out/vs/code/electron-browser/workbench/workbench.html) for keys/aliases and [.env](vscode-file://vscode-app/Users/dunevv/Applications/VS%20Code%20Portable/Visual%20Studio%20Code.app/Contents/Resources/app/out/vs/code/electron-browser/workbench/workbench.html) for tokens).
    - Effect: Different models (OpenAI vs Ollama) produce different parsing behaviors and hallucination rates; token/config differences can change outputs.
- Schema (Pydantic model)
    
    - Location: [OpenAIModelFee.model_json_schema()](vscode-file://vscode-app/Users/dunevv/Applications/VS%20Code%20Portable/Visual%20Studio%20Code.app/Contents/Resources/app/out/vs/code/electron-browser/workbench/workbench.html) inside the [LLMExtractionStrategy](vscode-file://vscode-app/Users/dunevv/Applications/VS%20Code%20Portable/Visual%20Studio%20Code.app/Contents/Resources/app/out/vs/code/electron-browser/workbench/workbench.html) call.
    - Effect: The schema tells the LLM which fields to extract and their types. Tighter schemas reduce missed or extra fields.
- Instruction prompt given to the LLM
    
    - Location: the [instruction=](vscode-file://vscode-app/Users/dunevv/Applications/VS%20Code%20Portable/Visual%20Studio%20Code.app/Contents/Resources/app/out/vs/code/electron-browser/workbench/workbench.html) argument passed to [LLMExtractionStrategy](vscode-file://vscode-app/Users/dunevv/Applications/VS%20Code%20Portable/Visual%20Studio%20Code.app/Contents/Resources/app/out/vs/code/electron-browser/workbench/workbench.html) inside [extract_structured_data_using_llm](vscode-file://vscode-app/Users/dunevv/Applications/VS%20Code%20Portable/Visual%20Studio%20Code.app/Contents/Resources/app/out/vs/code/electron-browser/workbench/workbench.html).
    - Effect: This greatly impacts results. Make the instruction explicit about required fields, formats, units, and edge cases to reduce noisy outputs.
- LLM extraction extra_args (temperature, top_p, max_tokens, extra_headers)
    
    - Location: the [extra_args](vscode-file://vscode-app/Users/dunevv/Applications/VS%20Code%20Portable/Visual%20Studio%20Code.app/Contents/Resources/app/out/vs/code/electron-browser/workbench/workbench.html) dict in [extract_structured_data_using_llm](vscode-file://vscode-app/Users/dunevv/Applications/VS%20Code%20Portable/Visual%20Studio%20Code.app/Contents/Resources/app/out/vs/code/electron-browser/workbench/workbench.html).
    - Effect:
        - temperature/top_p control sampling randomness — set temperature to 0 for deterministic extraction.
        - max_tokens limits LLM output size.
        - extra_headers can provide custom headers for API calls (rate limiting, auth variants).
- Extraction strategy options
    
    - The script uses [LLMExtractionStrategy](vscode-file://vscode-app/Users/dunevv/Applications/VS%20Code%20Portable/Visual%20Studio%20Code.app/Contents/Resources/app/out/vs/code/electron-browser/workbench/workbench.html), but Crawl4AI supports alternatives (JSON CSS extraction, CosineStrategy).
    - Effect: CSS-based extraction is deterministic and faster for structured pages. LLM-based extraction is flexible for free-form pages.
- Content filtering and chunking settings
    
    - Example fields: [word_count_threshold](vscode-file://vscode-app/Users/dunevv/Applications/VS%20Code%20Portable/Visual%20Studio%20Code.app/Contents/Resources/app/out/vs/code/electron-browser/workbench/workbench.html), `chunk_token_threshold`, `overlap_rate` (some are set via CrawlerRunConfig or strategy internals).
    - Location: when building [CrawlerRunConfig](vscode-file://vscode-app/Users/dunevv/Applications/VS%20Code%20Portable/Visual%20Studio%20Code.app/Contents/Resources/app/out/vs/code/electron-browser/workbench/workbench.html) and the strategy.
    - Effect: These parameters control what content is sent to the LLM and how it's split. Too-large chunks lead to truncated calls; too-small chunks can lose context.
- JavaScript execution / CSS selectors / DOM hooks
    
    - If the target page needs JS to render, set [BrowserConfig(java_script_enabled=True)](vscode-file://vscode-app/Users/dunevv/Applications/VS%20Code%20Portable/Visual%20Studio%20Code.app/Contents/Resources/app/out/vs/code/electron-browser/workbench/workbench.html) or pass `js_code` in [CrawlerRunConfig](vscode-file://vscode-app/Users/dunevv/Applications/VS%20Code%20Portable/Visual%20Studio%20Code.app/Contents/Resources/app/out/vs/code/electron-browser/workbench/workbench.html).
    - Use `css_selector` to focus on specific DOM sections to reduce noise.
    - Effect: Targeting the correct DOM region dramatically improves extraction accuracy and reduces irrelevant content.

Testing and tuning tips (quick)

- Start with `temperature=0` for deterministic extraction.
- Limit content by setting `css_selector` or excluded tags to reduce noise.
- If the page is structured, prefer `JsonCssExtractionStrategy` (faster, deterministic).
- When using LLMExtractionStrategy:
    - Make the instruction explicit and enumerate required fields and units.
    - Increase `max_tokens` if the schema is large.
    - Use provider-specific settings (e.g., different `max_tokens` for Ollama vs OpenAI).
- Inspect intermediate data:
    - Print [result.cleaned_html](vscode-file://vscode-app/Users/dunevv/Applications/VS%20Code%20Portable/Visual%20Studio%20Code.app/Contents/Resources/app/out/vs/code/electron-browser/workbench/workbench.html) or [result.markdown.raw_markdown](vscode-file://vscode-app/Users/dunevv/Applications/VS%20Code%20Portable/Visual%20Studio%20Code.app/Contents/Resources/app/out/vs/code/electron-browser/workbench/workbench.html) to see what was sent to the LLM.
    - Save raw LLM outputs (before schema parsing) to debug parsing errors.

Suggested minimal checklist to improve accuracy

- Confirm the correct URL and that the data is present in the page.
- If possible, target a specific CSS selector to reduce page noise.
- Use a clear LLM instruction and set temperature to 0.
- Validate and refine the Pydantic schema to match the actual fields and types.