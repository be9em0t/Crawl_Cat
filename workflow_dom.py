import os
import json
import yaml
import save_utils
from crawl4ai import AsyncWebCrawler, CacheMode, BrowserConfig, CrawlerRunConfig
from crawl4ai import JsonCssExtractionStrategy
from urllib.parse import urljoin


# Helper: parse include/exclude field specs and apply to node dicts
def _parse_field_list(spec):
    if spec is None:
        return None
    if isinstance(spec, str):
        return [s.strip() for s in spec.split(',') if s.strip()]
    if isinstance(spec, (list, tuple)):
        return list(spec)
    return None


def _filter_node_fields(node, include_fields, exclude_fields):
    """Return a copy of node with fields filtered.

    Precedence: include_fields (if provided) wins; otherwise exclude_fields removes keys.
    If neither provided, return node as-is.
    """
    if not isinstance(node, dict):
        return node
    if include_fields:
        return {k: node[k] for k in include_fields if k in node}
    if exclude_fields:
        return {k: v for k, v in node.items() if k not in exclude_fields}
    return node


def _resolve_field_filters(source, node_detail_schema=None):
    """Resolve include/exclude filters from node_detail_schema and source.

    Precedence: source-level keys override schema-level keys. Returns a tuple
    (include_fields, exclude_fields) where each is either a list or None.
    """
    include = None
    exclude = None
    # Schema-level first
    if isinstance(node_detail_schema, dict):
        include = _parse_field_list(node_detail_schema.get('include_fields'))
        exclude = _parse_field_list(node_detail_schema.get('exclude_fields'))
    # Source-level overrides
    s_include = _parse_field_list(source.get('include_fields'))
    s_exclude = _parse_field_list(source.get('exclude_fields'))
    if s_include is not None:
        include = s_include
    if s_exclude is not None:
        exclude = s_exclude
    return include, exclude

async def workflow_dom(source, urls, common):
    source_id = source.get('id', '<unknown>')
    category_schema = source.get('category_schema') or source.get('schema')
    if not category_schema:
        raise ValueError("Schema is required for dom workflow")

    out_folder = common.get('out_folder', '')
    output_file = source.get('out_file', 'extracted_dom')
    workflow = source.get('workflow', 'dom')
    output_file = f"{output_file}_{workflow}"
    if not output_file.endswith('.json'):
        output_file += '.json'
    if out_folder:
        output_file = f"{out_folder}/{output_file}"
    
    css_selector = source.get('css_selector')
    headless = source.get('headless', True)
    cache_mode = source.get('cache_mode', 'BYPASS')
    word_count_threshold = source.get('word_count_threshold', 1)
    page_timeout = source.get('page_timeout', 80000)
    
    main_url = source.get('url')
    if not urls:
        urls = [main_url]
    
    extraction_strategy = JsonCssExtractionStrategy(category_schema)
    
    config = CrawlerRunConfig(
        extraction_strategy=extraction_strategy,
        css_selector=css_selector,
        cache_mode=CacheMode[cache_mode.upper()] if cache_mode else CacheMode.BYPASS,
        word_count_threshold=word_count_threshold,
        page_timeout=page_timeout
    )
    
    async with AsyncWebCrawler() as crawler:
        if len(urls) == 1:
            result = await crawler.arun(url=urls[0], config=config)
            categories = json.loads(result.extracted_content)
        else:
            # For multiple URLs, combine
            categories = []
            for url in urls:
                result = await crawler.arun(url=url, config=config)
                data = json.loads(result.extracted_content)
                categories.extend(data)
    
    # Filter categories if needed
    categories = [item for item in categories if item.get('category_name') != 'Block']
    
    # Make category URLs full
    for cat in categories:
        cat_url = cat.get('category_url')
        if cat_url and not cat_url.startswith('http'):
            cat['category_url'] = urljoin(main_url, cat_url)
    
    expand_nodes = source.get('expand_nodes', False)
    if expand_nodes:
        preview_limit = source.get('preview_limit')
        processed_nodes = 0
        # node_schema is required when expand_nodes is enabled
        if 'node_schema' not in source:
            raise ValueError(
                f"Source '{source_id}': expand_nodes is True but 'node_schema' is missing in the config."
            )
        node_schema = source.get('node_schema')
        # Crawling node detail pages is optional. Control with 'crawl_node_pages' flag.
        crawl_node_pages = bool(source.get('crawl_node_pages', False))
        node_detail_schema = None
        if crawl_node_pages:
            if 'node_detail_schema' not in source:
                raise ValueError(
                    f"Source '{source_id}': 'crawl_node_pages' is True but 'node_detail_schema' is missing in the config."
                )
            node_detail_schema = source.get('node_detail_schema')
        
        node_config = CrawlerRunConfig(
            extraction_strategy=JsonCssExtractionStrategy(node_schema),
            css_selector=node_schema.get('css_selector', css_selector),
            cache_mode=CacheMode[cache_mode.upper()] if cache_mode else CacheMode.BYPASS,
            word_count_threshold=word_count_threshold,
            page_timeout=page_timeout
        )
        
        # Only build a detail_config when crawling node pages is enabled
        detail_config = None
        if crawl_node_pages:
            detail_config = CrawlerRunConfig(
                extraction_strategy=JsonCssExtractionStrategy(node_detail_schema),
                css_selector=None,  # Whole page
                cache_mode=CacheMode[cache_mode.upper()] if cache_mode else CacheMode.BYPASS,
                word_count_threshold=word_count_threshold,
                page_timeout=page_timeout
            )

        # Control debug output
        save_debug = source.get('save_debug_nodes')
        # Control whether node entries listed on category pages should be captured there
        # or used only as links to drill down into node pages.
        capture_nodes_on_category_page = bool(source.get('capture_nodes_on_category_page', True))
        # Aggregate debug information for all categories so we write one debug file
        debug_nodes = []
        # Field filtering configuration: resolve from schema or source (source overrides)
        include_fields, exclude_fields = _resolve_field_filters(source, source.get('node_detail_schema'))
        # Detail-name preservation: allow per-schema or per-source override
        preserve_detail_name = False
        if isinstance(source.get('node_detail_schema'), dict):
            preserve_detail_name = bool(source.get('node_detail_schema', {}).get('preserve_name', False))
        # Source-level override
        if 'preserve_detail_name' in source:
            preserve_detail_name = bool(source.get('preserve_detail_name'))

        for cat in categories:
            cat_url = cat.get('category_url')
            if cat_url:
                # Make full URL if relative
                if not cat_url.startswith('http'):
                    cat_url = urljoin(main_url, cat_url)
                
                try:
                    async with AsyncWebCrawler() as node_crawler:
                        result = await node_crawler.arun(url=cat_url, config=node_config)
                        nodes = json.loads(result.extracted_content) if result and result.extracted_content else []
                except Exception as e:
                    # If the browser fails to start or another error occurs, skip node extraction for this category
                    print(f"[{source_id}] Warning: failed to crawl category page '{cat.get('category_name')}' ({cat_url}): {e}")
                    nodes = []
                if save_debug:
                    print(f"[{source_id}] Category '{cat.get('category_name')}' raw nodes: {len(nodes)}")

                if source.get('has_subcategories'):
                    subcategories = []
                    for i, table_data in enumerate(nodes):
                        subcat_name = f"sub{i+1:02d}"
                        classes = table_data.get('classes', [])
                        normalized_classes = []
                        for cls in classes:
                            name = cls.get('class_name', '') or cls.get('name', '') or cls.get('title', '')
                            url = cls.get('class_url', '') or cls.get('url', '') or cls.get('link', '')
                            desc = cls.get('description', '') or cls.get('summary', '') or ''
                            if url and not url.startswith('http'):
                                url = urljoin(cat_url, url)
                            normalized_classes.append({'name': name, 'url': url, 'description': desc})
                        subcategories.append({'name': subcat_name, 'classes': normalized_classes})
                    cat['subcategories'] = subcategories
                    if save_debug:
                        debug_nodes.append({
                            'category_name': cat.get('category_name'),
                            'category_url': cat.get('category_url'),
                            'subcategories': subcategories
                        })
                    continue  # Skip further processing for this category

                # Normalize and clean nodes: ensure node_name, node_url, description exist
                normalized = []
                for node in nodes:
                    # defensive field mapping
                    name = node.get('node_name') or node.get('name') or node.get('title') or ''
                    node_url = node.get('node_url') or node.get('url') or node.get('link') or ''
                    # Houdini uses 'summary' for node short descriptions; map it into description
                    desc = node.get('description') or node.get('summary') or node.get('body') or node.get('text') or ''

                    # Clean description by removing leading node name if present
                    if name and desc.startswith(name):
                        desc = desc[len(name):].strip()

                    # Build canonical node dict while preserving other fields
                    canon = {'node_name': name, 'node_url': node_url, 'description': desc}
                    for k, v in node.items():
                        if k not in canon:
                            canon[k] = v

                    # Apply include/exclude filtering immediately so debug shows the filtered shape
                    filtered = _filter_node_fields(canon, include_fields, exclude_fields)
                    normalized.append(filtered)

                # Save normalized nodes to debug aggregation
                debug_nodes.append({
                    'category_name': cat.get('category_name'),
                    'category_url': cat.get('category_url'),
                    'nodes': normalized
                })

                # Filter nodes to only those with names
                nodes = [node for node in normalized if node.get('node_name')]
                if save_debug:
                    print(f"[{source_id}] Category '{cat.get('category_name')}' normalized nodes with names: {len(nodes)}")

                # If the config indicates that nodes on the category page are just links
                # to be followed for full details, and crawl_node_pages is True, then
                # collect node URLs and crawl them for details. Otherwise, treat nodes
                # on the category page as the final extracted nodes.
                if not capture_nodes_on_category_page and crawl_node_pages:
                    # Collect node URLs to crawl in parallel
                    node_urls_to_crawl = []
                    nodes_to_update = []
                    for node in nodes:
                        if preview_limit and processed_nodes >= preview_limit:
                            break
                        node_url = node.get('node_url')
                        if node_url:
                            if not node_url.startswith('http'):
                                node_url = urljoin(cat_url, node_url)
                            node['node_url'] = node_url  # Update to full URL
                            node_urls_to_crawl.append(node_url)
                            nodes_to_update.append(node)
                        processed_nodes += 1

                    # Crawl node details in parallel
                    if node_urls_to_crawl and detail_config:
                        async with AsyncWebCrawler() as detail_crawler:
                            import asyncio
                            tasks = [detail_crawler.arun(url=url, config=detail_config) for url in node_urls_to_crawl]
                            results = await asyncio.gather(*tasks, return_exceptions=True)
                        final_nodes = []
                        for node, result in zip(nodes_to_update, results):
                            if isinstance(result, Exception):
                                print(f"[{source_id}] Warning: failed to crawl node detail page {node.get('node_url')}: {result}")
                                final_nodes.append(node)
                                continue
                            raw = result.extracted_content
                            # Some crawler runs may return no extracted_content (None).
                            # Treat that as empty details rather than calling json.loads(None).
                            if not raw:
                                details = []
                            else:
                                details = json.loads(raw)
                            if details:
                                # Merge details over node; details[0] expected to contain name/description etc.
                                merged = node.copy()
                                # Merge details then normalize description field
                                detail_obj = details[0].copy()
                                desc = detail_obj.get('description')
                                if isinstance(desc, list):
                                    # Join multiple paragraph matches into a single string
                                    # Preserve paragraph breaks with double newlines
                                    detail_obj['description'] = '\n\n'.join([d.strip() for d in desc if d and d.strip()])
                                elif isinstance(desc, str):
                                    detail_obj['description'] = desc.strip()
                                # Remove 'name' from detail pages unless preservation is requested.
                                if not preserve_detail_name:
                                    # Avoid conflicting with canonical 'node_name' from category pages.
                                    detail_obj.pop('name', None)
                                merged.update(detail_obj)
                                merged = _filter_node_fields(merged, include_fields, exclude_fields)
                                final_nodes.append(merged)
                            else:
                                final_nodes.append(node)
                        cat['nodes'] = final_nodes
                    else:
                        # No detail crawl performed; still update full URLs if present
                        for node in nodes:
                            if node.get('node_url') and not node['node_url'].startswith('http'):
                                node['node_url'] = urljoin(cat_url, node['node_url'])
                            # Ensure final filtering applied (in case normalized earlier didn't include dynamic merges)
                            node = _filter_node_fields(node, include_fields, exclude_fields)
                        cat['nodes'] = nodes
                else:
                    # Treat nodes on category page as final extracted nodes
                    for i, node in enumerate(nodes):
                        if node.get('node_url') and not node['node_url'].startswith('http'):
                            node['node_url'] = urljoin(cat_url, node['node_url'])
                        # Apply filtering to each final node
                        nodes[i] = _filter_node_fields(node, include_fields, exclude_fields)
                    cat['nodes'] = nodes
            if preview_limit and processed_nodes >= preview_limit:
                break

        # Save aggregate debug file only when explicitly requested via config
        # Use explicit key 'save_debug_nodes: true' and optional 'debug_file' to control output
        if save_debug:
            debug_filename = source.get('debug_file') or (os.path.splitext(output_file)[0] + "_debug_nodes.json")
            save_utils.save_json(debug_filename, debug_nodes)
        else:
            # Do not write debug output unless explicitly requested. This avoids unexpected files.
            pass
    
    # Save the extracted data
    # Post-processing: normalize category names and resolve relative function/node URLs
    for cat in categories:
        # Clean category_name by removing pilcrow marks and trimming
        cname = cat.get('category_name')
        if isinstance(cname, str) and cname:
            cat['category_name'] = cname.replace('¶', '').strip()

        # Normalize any category-level URL as absolute (already done earlier for 'category_url'
        # but ensure it's present and absolute for subsequent joins)
        if cat.get('category_url') and not cat['category_url'].startswith('http'):
            cat['category_url'] = urljoin(main_url, cat['category_url'])

        # Resolve nested function or node URLs and clean names
        for list_key in ('functions', 'nodes'):
            items = cat.get(list_key)
            if isinstance(items, list):
                for item in items:
                    # Clean function/node names
                    for name_key in ('function_name', 'node_name', 'name', 'title'):
                        if name_key in item and isinstance(item[name_key], str):
                            item[name_key] = item[name_key].replace('¶', '').strip()

                    # Resolve common URL-like fields to absolute URLs
                    for url_key in ('function_url', 'node_url', 'url', 'link', 'href'):
                        val = item.get(url_key)
                        if isinstance(val, str) and val and not val.startswith('http'):
                            base = cat.get('category_url') or main_url
                            item[url_key] = urljoin(base, val)

        # Handle subcategories
        for subcat in cat.get('subcategories', []):
            for cls in subcat.get('classes', []):
                # Clean class names
                for name_key in ('name',):
                    if name_key in cls and isinstance(cls[name_key], str):
                        cls[name_key] = cls[name_key].replace('¶', '').strip()

                # Resolve class URLs
                for url_key in ('url',):
                    val = cls.get(url_key)
                    if isinstance(val, str) and val and not val.startswith('http'):
                        base = cat.get('category_url') or main_url
                        cls[url_key] = urljoin(base, val)

    save_utils.save_json(output_file, categories)
    print(f"Extracted data saved to {output_file}")