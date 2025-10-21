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

1. **Done - Support CSS-based extraction**
   - Inspect Unity page DOM to identify selectors for node names/descriptions (e.g., `.node-title`, `.node-desc`).
   - Use `JsonCssExtractionStrategy` for structured output without LLM (generate schema once if needed).
   - If pages are dynamic, add `js_code` to expand/load content.

2. **Done - Implement sidebar reading and selection**
   - Use deep crawl or JS actions to extract sidebar links from the main page.
   - Filter links to only those under "Node Library".
   - Print the list for user approval; proceed only after confirmation.

3. **Done - Integrate deep crawl**
   - If manual URL listing is insufficient, use `BFSDeepCrawlStrategy` with filters to auto-discover and crawl selected pages.

4. **OPTIONAL - Integrate JS if necessary**
   - If manual URL listing is insufficient, use `BFSDeepCrawlStrategy` with filters to auto-discover and crawl selected pages.
   - Test JS interactions for collapsible sidebars.

5. **Fallback to hybrid LLM/CSS**
   - If CSS selectors fail for complex pages, combine LLM for schema generation with CSS for extraction.

6. **Done - Validate and optimize**
   - Test on a subset of pages; ensure all nodes are captured without duplicates.

7. **Streamline config.json**
   - Remove redundant fields.
   - Unify.
   - Make template.
   - Extract default fields to a defaults caegory.

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




-- DONE extract minimal 
https://www.sidefx.com/docs/houdini21.0/vex/functions/index.html

  - id: "houdini21_vex_dom_minimal"

DOM description:
Limit extraction only to <div class="original filtered-body">
It will contain multiple <section class="heading pull left  ">, which contain the VEX categories
Each such <section class="heading pull left  "> will contain the name of the category and the list of functions in that category.
Name of category, for example 'Arrays' will be contained in someting like
<h2 class="label heading pull left" id="array_group" data-title="arrays">Arrays</h2>.
List of functions in that category will be contained inside <div id="array_group-body" class="content">.
Finally, each of the fucntions is defined inside list item, for example 'append' function name, url and summary are defined like this:
<li class="item subtopics_item ind-item   " data-title="append">
   <p class="label">
            <a class="label-text vex" href="append.html">append</a>
   </p>
      <p class="summary">Adds an item to an array or string.</p>
</li>
Please unclude full, not relative, urls for easy reference.



-- extract minimal PyQGIS 
https://qgis.org/pyqgis/3.40/index.html

  - id: "pyqgis_340_minimal"

I've created a new source id: "pyqgis_340_minimal" that will contain YAML settings to extract documentation from https://qgis.org/pyqgis/3.40/index.html
We need to use the dom workflow, and generate a correct YAML that will do the crawl and extraction without using LLM.
If you have to edit the python code, limit edits only to #file:workflow_dom.py  and make sure not to break existing functionality that captures unity nodes and houdini nodes and functions with names, urls, descriptions and summaries.

Here is a DOM guidance:
from the root URL we're instrested only in the Python classes:
<div class="toctree-wrapper compound">

There all class categories are listed inside <ul></ul> tag
The main categories are on their separate index pages, foe example:
<li class="toctree-l1"><a class="reference internal" href="core/index.html">core</a><ul>

The category pages, mentioned above (<a class="reference internal" href="core/index.html">core</a>) have to be crawled carfully.
For each category page we have to extract all sub-categories, classes, class URLs and class descriptions.

Sub-categories mostly live in something like this:
<section id="d">
and right below the subcategory name is in 
<span id="core-3d">
Under it you will have 
<table class="docutils align-default">
that containes the class name, URL and short description:
<tr class="row-odd"><td><p><a class="reference external" href="Qgs3DRendererAbstractMetadata.html">Qgs3DRendererAbstractMetadata</a></p></td>
<td><p>Base metadata class for 3D renderers. Instances of derived classes may be registered in Qgs3DRendererRegistry.</p></td>
</tr>

The exception to this are classes that do not have sub-category, but belong to the category directly. 
They can be listed in 
<table class="docutils align-default">
but without <section id> or <span id>.
These are classes directly belonging to the Category, and not part of any sub-category.

So, to reiterate:
We need to hierarchically extract PyQGIS classes 
PyQGIS 3.40
  - Categories
      - Classes with URLs and descriptions
      - Sub-categories
         - Classes with URLs and descriptions

Please verify my DOM guidance aginst the url: https://qgis.org/pyqgis/3.40/index.html




  - id: "pyqgis_340_minimal"

I've created a new source id: "pyqgis_340_minimal" that will contain YAML settings to extract documentation from https://qgis.org/pyqgis/3.40/index.html
We need to use the dom workflow, and generate a correct YAML that will do the crawl and extraction without using LLM.
If you have to edit the python code, limit edits only to #file:workflow_dom.py  and make sure not to break existing functionality that captures unity nodes and houdini nodes and functions with names, urls, descriptions and summaries.

Here is a DOM guidance:
from the root URL we're instrested only in the Python classes:
<div class="toctree-wrapper compound">

There all class categories are listed inside <ul></ul> tag
The main categories are on their separate index pages, foe example:
<li class="toctree-l1"><a class="reference internal" href="core/index.html">core</a><ul>

The category pages, mentioned above (<a class="reference internal" href="core/index.html">core</a>) have to be crawled carfully.
For each category page we have to extract all sub-categories, classes, class URLs and class descriptions.

There are multiple <table class="docutils align-default"> on each category page. Capture them all as different sub-categories. You can name them sub 01, sub 02 etc if the name of the category is not obvious.

Each of these tables (sub-categories) contains multiple class names, URLs and short descriptions:
<tr class="row-odd"><td><p><a class="reference external" href="Qgs3DRendererAbstractMetadata.html">Qgs3DRendererAbstractMetadata</a></p></td>
<td><p>Base metadata class for 3D renderers. Instances of derived classes may be registered in Qgs3DRendererRegistry.</p></td>
</tr>

Make sure the JSON is structured in a way that the categoires contain subcategories which contain classes with name, url and description. 

It is not expected that classes will be duplicated, if this happens we probably have error in the dom crawling.

Please verify my DOM guidance aginst the url: https://qgis.org/pyqgis/3.40/index.html

----------

We now have a pretty solid hierarchical extraction of categories, subcategories and classes.

We intentionally do not capure subcategory names, just calling them sub01, sub02 etc.
Each category lives in its own baseSelector: "table.docutils.align-default"
Some of the tables are preceded by a <h2> containing the subcategory name, please use it if available.
If not just use leave the subcategory name blank.

Do not alter the structure. Do not filter out nodes. Just work on subcategory name capture.