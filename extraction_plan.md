# Plan for Fixing Unity ShaderGraph Node Extraction

## Issue
The crawler captures only top-level categories (e.g., Artistic, Channel) without subcategories or nodes. Nodes like "Append", "Combine" under "Channel" or subcategories and nodes under "Artistic" are not extracted.

## Root Cause Analysis
- Deep crawling may not be extracting from sub-pages correctly.
- LLM might not be processing sub-page content or adhering to the instruction.
- Pydantic model complexity or token limits could be causing incomplete JSON generation.
- CSS filtering or other config issues might be limiting content availability.

## Next Steps Plan

1. **Debug deep crawling and content extraction**
   - Temporarily switch `extraction_type` to `'block'` in the config.
   - Run the crawler to capture raw text from each crawled page.
   - Analyze the output JSON (list of texts) to verify if sub-pages (e.g., Artistic-Nodes.html, Channel-Nodes.html) are being crawled.
   - Check what content is extracted from each page.

2. **Verify sub-page content availability**
   - If sub-pages are crawled, examine the raw text to ensure node names and descriptions are present.
   - If content is missing, adjust `url_match` pattern or `crawler_depth`.
   - If content is there but not structured, refine the LLM instruction for better specificity (e.g., explicitly mention table parsing).

3. **Simplify extraction model or approach**
   - If schema extraction fails due to model complexity, simplify the Pydantic model (e.g., flatten the hierarchy or use a list of nodes with category metadata).
   - Alternatively, switch permanently to block extraction followed by post-processing.

4. **Implement text-based extraction and parsing**
   - Implement a two-step process:
     1. Crawl and collect raw text from all pages using block extraction.
     2. Use a separate LLM call to parse and structure the combined text into the desired NodeLibrary format.
   - Modify `crawl-cat2.py` to concatenate all extracted texts and send to a second LLM for structuring.

5. **Manually validate page content**
   - Use `fetch_webpage` to manually inspect content from key pages (main, category like Artistic, node pages like Channel-Mixer-Node).
   - Confirm the structure and identify any elements the crawler might be skipping (e.g., tables, h1, p tags).

## Execution Notes
- Start with step 1 to isolate if the issue is crawling or extraction.
- Update the config YAML and code as needed for each step.
- Monitor token usage and costs, as LLM calls will increase.
- Test changes incrementally and validate output after each adjustment.