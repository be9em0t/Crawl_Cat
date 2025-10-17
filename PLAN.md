# Plan for Fixing Unity ShaderGraph Node Extraction

## Issue
Not all pages are correctly structured (surprise).
So we need to use smartly DOM elements and use LLM only for extremely messy sites.
Soem reqire user interaction (JS) to browse.

## Root Cause Analysis
- Sidebar structure isn't fully reflected in page subcategories; some category pages exist but aren't nested under the main Node Library page.
- LLM-based extraction works but is slow/expensive; switching to CSS/DOM selectors for speed is needed for repetitive extraction.
- Potential need for JS actions to expand dynamic sidebars or deep crawling to auto-discover links.


## Next Steps Plan

1. **Support CSS-based extraction**
   - Inspect Unity page DOM to identify selectors for node names/descriptions (e.g., `.node-title`, `.node-desc`).
   - Use `JsonCssExtractionStrategy` for structured output without LLM (generate schema once if needed).
   - If pages are dynamic, add `js_code` to expand/load content.

2. **Implement sidebar reading and selection**
   - Use deep crawl or JS actions to extract sidebar links from the main page.
   - Filter links to only those under "Node Library".
   - Print the list for user approval; proceed only after confirmation.

3. **Integrate deep crawl**
   - If manual URL listing is insufficient, use `BFSDeepCrawlStrategy` with filters to auto-discover and crawl selected pages.

4. **OPTIONAL - Integrate JS if necessary**
   - If manual URL listing is insufficient, use `BFSDeepCrawlStrategy` with filters to auto-discover and crawl selected pages.
   - Test JS interactions for collapsible sidebars.

5. **Fallback to hybrid LLM/CSS**
   - If CSS selectors fail for complex pages, combine LLM for schema generation with CSS for extraction.

6. **Validate and optimize**
   - Test on a subset of pages; ensure all nodes are captured without duplicates.
   - Monitor speed and cost; aim for non-LLM extraction where possible.

## Notes on Useful Functions Analyzed
From Crawl4ai examples (`quickstart.py`, `quickstart_examples_set_1.py` and `quickstart_examples_set_2.py`):
- **`JsonCssExtractionStrategy`**: For fast, structured extraction via CSS selectors. Define a schema (baseSelector + fields) for JSON output without LLM. Use `generate_schema()` once with LLM for setup, then reuse. Ideal for (c) node extraction.
- **`BFSDeepCrawlStrategy`**: Enables deep crawling with `max_depth`, `max_pages`, and `FilterChain` (e.g., `DomainFilter`, `url_match`). Useful for (a) auto-discovering sidebar links and (b) selective crawling.
- **`js_code` in CrawlerRunConfig**: Execute JS before extraction (e.g., click to expand sidebars). Essential for dynamic content in (a) and (c).
- **`simple_example_with_css_selector()`**: Basic CSS limiting for focused crawling; pair with manual parsing for simple cases.
- **`demo_deep_crawl()`**: Demonstrates filtered deep crawl; adapt for sidebar link discovery.
- **`demo_css_structured_extraction_no_schema()`**: One-time schema gen via LLM, then pure CSS extraction. Perfect for repeatable, fast node pulls.

### Content Selection documentation
Url: https://docs.crawl4ai.com/core/content-selection/

Yes, the Content Selection documentation is very helpful for the extraction process. Here's how it applies to our task:

## Key Helpful Features:

1. **CSS Selector Scoping**: We can use `css_selector="#toc"` in `CrawlerRunConfig` to limit the crawl to just the table of contents region, reducing noise and improving parsing accuracy.

2. **Content Filtering**: Parameters like `excluded_tags`, `word_count_threshold`, and link/media exclusions can help clean up the extracted TOC HTML before parsing.

3. **Structured Extraction**: The `JsonCssExtractionStrategy` with nested schemas could potentially extract hierarchical link data from the TOC, though for complex nested structures like `#toc`, manual parsing with BeautifulSoup might still be needed.

4. **Target Elements**: `target_elements` allows focusing on specific parts while preserving full page context for link analysis.

## How It Fits Our Process:

- **Main Page Crawl**: Use `css_selector="#toc"` to get clean TOC HTML, then parse the hierarchy with BeautifulSoup.
- **Node Page Crawls**: Use content filtering to exclude unwanted elements (nav, footer, etc.) when extracting `<h1>` and `<p>` from individual node pages.
- **Performance**: The LXML scraping strategy mentioned provides fast processing for large HTML documents.

The documentation confirms that Crawl4AI's content selection capabilities will make our modular Python function more efficient and precise, especially for scoping crawls and filtering irrelevant content. We can combine CSS selection with manual parsing for the hierarchical structure.


## Code Organization Principles
- Keep `crawl-cat2.py` minimal, universal, and modular (aim for under ~400 lines; offload to separate modules if exceeded).
- Work towards achieving flexibilty and modularity with end goal of support for all Workflows listed below
- Store all site-specific extraction details (e.g., URLs, instructions, models, new keys like `crawl_depth`) in config YAML files (e.g., `config_unity_shadergraph.yaml`).
- Use minimal command-line options: `python crawl-cat2.py -cfg config_file.yaml -id id_key`. Support multiple `id_key` entries per YAML for variations (e.g., different LLM providers).
- Adopt a minimalistic approach: clear error messages on failures, limited defaults (only obvious values/logic), no implicit second-guessing.
- Avoid using implicit functionality, prefer clear error message to direct user
- If hooman's request violates these principles warn him and ask for decision

## Workflows
- Launch app
- Load yaml, branch to different workflow strategies based on it
   - explore - try to capture only tructure
   - llm - intelligently crawl pages and select content according to instructions
   - hybrid - LLM + DOM - intelligent crawl pages, but collect information based on DOM selectors
   - dom - use predefined schema, follow through the pages based om DOMselectors
   - hierarchy - convert flat json into hierarchy organised one
   - Full HTML - extracion to download all candidate pages, extract content locally
- Optional verification of results
- Optional processing with postprocessing prompt
- Optional format filters (clear fences, UTF charecters etc.)
- Save as JSON (via save_utils.py module)
- Exit


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


# Remarks
- Seems that llm workflow can generate pretty well a non-structured json and markdown, whcih than hierarchy workwlow sorts nicely. We still miss ui nodes for some reason, but on the right track.
- the idea for next step was to build flexible dom workflow, that can follow detailed dom element instructions as in the propmt below

# dom workflow creation prompt:
Next we will work on dom workflow.

The goal is to extract information specified by the user based on dom elements, using the strengths if crawl4ai.

Our first use case will be set using this yaml id: "shadergraph_content_dom"

We will use this source
url: "https://docs.unity3d.com/Packages/com.unity.shadergraph@17.4/manual/Node-Library.html"

We will be extracting Node names and descriptions, hierarchically ordered under Categories.

We will limit contents to css_selector: "#_content"


Analyze the task first, check documentation at #fetch https://docs.crawl4ai.com/core/content-selection/ and tell me what will work and what will not work within these constraints:
- We should be able to do this only using DOM selectors.
- If we need a specific python function optimized for this case it's also fine, but it needs to be modular. If we can do it with universal python code driven by a well-formed yaml config - even better.
- You will provide a DOM selectror schema template that the user can fill to extract the right information from the rigth category
- In a future development we can include LLM inthe DOM discovery process

----


We will limit contents of css_selector: "#toc"

- filter out the contents of "#toc" and keep only
  * [Node Library](https://docs.unity3d.com/Packages/com.unity.shadergraph@17.4/manual/Node-Library.html "Node Library") and all of its sub-pages, remove all other content. (we might need to use LLM request for this)

- structure them hierarchically, exactly as they are structured in captured #toc

- capture for each Node (this are always the furthest down the hierachy) the 
 -- name (<h1> containing something like "Normal Strength Node". Node seems to be always present.)
 -- description (first <p> after the <h1>)


Let's execute with the following restraints:
- It seems we should be able to do this only using DOM selectors.
- If we need a specific python function optimized for this case it's also fine, but it needs to be modular.
- I hope we can achieve this without LLM, and will try LLM approach in our next case.
- Analyze the task first, check documentation at #fetch https://docs.crawl4ai.com/core/content-selection/
 and tell me what will work and what will not work within these constraints:

---
Hooray, the debug json is not written out ny more.

Lets continue to fixing id: "houdini21_content_dom_minimal"

Currently we are only capturing the top-level categories using DOM selectors.
Update the schema so that we extract not only categories, but hieararchically include node names, node urls and node summaries listed on each category page. Do not crawl the node pages themselves for full descriptions, this will be very slow.

Example:
the schema correctly captures 
  {
    "category_name": "Channel nodes",
    "category_url": "https://www.sidefx.com/docs/houdini21.0/nodes/chop/index.html",
    "description": "Channel nodes create, filter, and manipulate channel data."
  }
From the category_url we need to look up 
<ul class="subtopics_item_group item_group">. It contains multiple #ind_item selectors, one for each node we need to capture.
The #ind_item selectors contain something like 
<a class="label-text node" href="agent.html">Agent</a> - this is the name of the node and it's url.
<p class="summary">Imports an animation clip from an agent primitive.</p> - this the node summary.
So, using these selectors, please update the schema to capture correclty hierarchical structure and save it out as json.


Store not relative, but full urls, please, to be used for online referencing when necessary.


---
improving shadergraph:
on node pages crawl only the contents of #_content, and from it use
- the first <h1> is the node name
- after it there may are mai not be an <h2> which we ignore (usually its just a title "Description")
- all the <p> tags after it and before the #ports are the description