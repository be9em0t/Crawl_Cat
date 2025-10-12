# Plan for Fixing Unity ShaderGraph Node Extraction

## Issue
The crawler now captures hierarchical categories with subcategories and nodes, but there's a discrepancy: the sidebar lists more pages than the subcategories available on individual pages. Some pages aren't linked via subcategories, leading to incomplete coverage.

## Root Cause Analysis
- Sidebar structure isn't fully reflected in page subcategories; some category pages exist but aren't nested under the main Node Library page.
- LLM-based extraction works but is slow/expensive; switching to CSS/DOM selectors for speed is needed for repetitive extraction.
- Potential need for JS actions to expand dynamic sidebars or deep crawling to auto-discover links.

## Updated Requirements
1. **Read sidebar structure and print for approval (a)**: Crawl the main Node-Library.html, extract all sidebar links (especially under "Node Library"), and output them for user confirmation before proceeding.
2. **Select only part of the sidebar (b)**: Filter to pages under "Node Library" (e.g., Artistic-Nodes.html, Channel-Nodes.html, etc.), excluding unrelated sections.
3. **Capture from each page using CSS/DOM selectors (c)**: For selected pages, extract node names and descriptions using pure CSS selectors (no LLM) for speed. If dynamic content, use JS to load it first.

## Next Steps Plan

1. **Implement sidebar reading and selection**
   - Use deep crawl or JS actions to extract sidebar links from the main page.
   - Filter links to only those under "Node Library".
   - Print the list for user approval; proceed only after confirmation.

2. **Switch to CSS-based extraction**
   - Inspect Unity page DOM to identify selectors for node names/descriptions (e.g., `.node-title`, `.node-desc`).
   - Use `JsonCssExtractionStrategy` for structured output without LLM (generate schema once if needed).
   - If pages are dynamic, add `js_code` to expand/load content.

3. **Integrate deep crawl and JS if necessary**
   - If manual URL listing is insufficient, use `BFSDeepCrawlStrategy` with filters to auto-discover and crawl selected pages.
   - Test JS interactions for collapsible sidebars.

4. **Fallback to hybrid LLM/CSS**
   - If CSS selectors fail for complex pages, combine LLM for schema generation with CSS for extraction.

5. **Validate and optimize**
   - Test on a subset of pages; ensure all nodes are captured without duplicates.
   - Monitor speed and cost; aim for non-LLM extraction where possible.

## Notes on Useful Functions Analyzed
From Crawl4ai examples (`quickstart.py` and `quickstart_examples_set_1.py`):
- **`JsonCssExtractionStrategy`**: For fast, structured extraction via CSS selectors. Define a schema (baseSelector + fields) for JSON output without LLM. Use `generate_schema()` once with LLM for setup, then reuse. Ideal for (c) node extraction.
- **`BFSDeepCrawlStrategy`**: Enables deep crawling with `max_depth`, `max_pages`, and `FilterChain` (e.g., `DomainFilter`, `url_match`). Useful for (a) auto-discovering sidebar links and (b) selective crawling.
- **`js_code` in CrawlerRunConfig**: Execute JS before extraction (e.g., click to expand sidebars). Essential for dynamic content in (a) and (c).
- **`simple_example_with_css_selector()`**: Basic CSS limiting for focused crawling; pair with manual parsing for simple cases.
- **`demo_deep_crawl()`**: Demonstrates filtered deep crawl; adapt for sidebar link discovery.
- **`demo_css_structured_extraction_no_schema()`**: One-time schema gen via LLM, then pure CSS extraction. Perfect for repeatable, fast node pulls.

## Execution Notes
- Prioritize CSS extraction for speed; use LLM only for schema setup or complex parsing.
- Test changes on the main page first, then expand to sub-pages.
- Update config YAML and `crawl-cat2.py` incrementally.
- If expanding functionality, add as separate modules (e.g., a sidebar reader function).

## Code Organization Principles
- Keep `crawl-cat2.py` minimal, universal, and modular (aim for under ~400 lines; offload to separate modules if exceeded).
- Store all site-specific extraction details (e.g., URLs, instructions, models, new keys like `crawl_depth`) in config YAML files (e.g., `config_unity_shadergraph.yaml`).
- Use minimal command-line options: `python crawl-cat2.py -cfg config_file.yaml -id id_key`. Support multiple `id_key` entries per YAML for variations (e.g., different LLM providers).
- Adopt a minimalistic approach: clear error messages on failures, limited defaults (only obvious values/logic), no implicit second-guessing.
- Avoid using implicit functionality, prefer clear error message so that the user can make adjustments
- if hooman's request violates these principles warn him and ask for decision

## Workflows proposal
- load yaml, branch to different strategies based on it
   - Explore strategy - try to capture only tructure
   - Pure LLM strategy - intelligently crawl pages and select content according to instructions
   - LLM + DOM - intelligent crawl pages, but collect information based on DOM selectors
   - Pure DOM - use predefined schema, follow through the pages based om DOMselectors
   - Full HTML extracion to download all candidate pages, extract content locally
- Optional verification of results
- Optional processing with postprocessing prompt
- Optional format filters (clear fences, UTF charecters etc.)
- Save as JSON (via save_utils.py module)

### Remarks for Future Implementation (workflows explore, llm, dom, html)
- **Feasibility**: All workflows are fully feasible with Crawl4Ai (e.g., LLM via LLMExtractionStrategy, DOM via JsonCssExtractionStrategy, Explore via BFSDeepCrawlStrategy). No major gaps identified.
- **Efficiency Priority**: Pure DOM > Full HTML > LLM + DOM > Pure LLM > Explore (speed/cost). Prioritize DOM-based for production; use LLM only for setup or complex cases.
- **Modularity**: Implement each workflow as a separate async function (e.g., `workflow_llm`, `workflow_explore`) in `crawl-cat2.py` or separate modules if code grows >400 lines. Call from `main()` based on `workflow` key.
- **Config Enhancements**: Add optional keys like `js_code` for dynamic content, `crawl_depth` for deep crawls, `postprocess_prompt` for optional LLM postprocessing. Default `workflow` to 'llm' if missing.
- **Testing/Validation**: For each workflow, add optional verification (e.g., via `runTests` or custom checks). Include format filters (e.g., UTF-8, fence removal) in save_utils.py.
- **Error Handling**: Add try-except blocks per workflow with clear error messages. Log workflow start/end for debugging.
- **Scalability**: Integrate `BFSDeepCrawlStrategy` where needed (e.g., Explore, HTML). For large crawls, add `max_pages` and filters.
- **Fallbacks**: If DOM fails, allow hybrid LLM+DOM. For Explore, print links for user approval before full extraction.
- **Next Steps**: Start with 'llm' (done), then 'explore' (link discovery), 'dom' (CSS extraction), 'html' (raw download). Add optionals last.


