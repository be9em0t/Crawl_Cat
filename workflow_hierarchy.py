import json
import os
import re
from typing import Dict, List, Any

def parse_markdown_table(content: str) -> List[Dict[str, str]]:
    """Parse markdown table to extract links and descriptions."""
    lines = content.split('\n')
    table_start = False
    headers = []
    rows = []

    for line in lines:
        line = line.strip()
        if '**Topic**' in line and '**Description**' in line:
            table_start = True
            headers = ['topic', 'description']
            continue
        elif table_start and '---' in line:
            continue
        elif table_start and '|' in line and not line.startswith('##'):
            parts = [p.strip() for p in line.split('|')]
            if len(parts) >= 2:
                topic = parts[0]
                description = parts[1] if len(parts) > 1 else ""
                # Extract link from [text](url)
                link_match = re.search(r'\[([^\]]+)\]\(([^)]+)\)', topic)
                if link_match:
                    name = link_match.group(1)
                    url = link_match.group(2)
                    rows.append({
                        'name': name,
                        'url': url,
                        'description': description
                    })
        elif table_start and line.startswith('##'):
            # New section, stop parsing table
            break

    return rows


def build_hierarchy(flat_data: List[Dict[str, Any]], root_url: str) -> Dict[str, Any]:
    """Build hierarchical structure from flat crawled data."""
    # Create lookup by URL, normalize
    url_to_content = {}
    for item in flat_data:
        url = item['url'].replace('%40', '@')
        url_to_content[url] = item['content']

    if root_url not in url_to_content:
        raise ValueError("Root URL not found in data")

    root_content = url_to_content[root_url]

    # Parse root for categories
    categories = parse_markdown_table(root_content)

    hierarchy = {
        'name': 'Node Library',
        'url': root_url,
        'description': 'Explore nodes that enable color and channel manipulation...',
        'categories': []
    }

    for cat in categories:
        cat_url = cat['url']
        if cat_url in url_to_content:
            cat_content = url_to_content[cat_url]
            # Parse category for subcategories and nodes
            sub_sections = parse_category_content(cat_content)
            hierarchy['categories'].append({
                'name': cat['name'],
                'url': cat_url,
                'description': cat['description'],
                'subcategories': sub_sections
            })

    return hierarchy


def parse_category_content(content: str) -> List[Dict[str, Any]]:
    """Parse category page content for subcategories and nodes."""
    lines = content.split('\n')
    subcategories = []
    current_sub = None

    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith('## ') and '[](' in line:
            # New subcategory
            sub_match = re.search(r'##\s+\[\]\(([^)]+)#([^)]+)\)(.+)', line)
            if sub_match:
                anchor = sub_match.group(2)
                title = sub_match.group(3).strip()
                current_sub = {
                    'name': title,
                    'anchor': anchor,
                    'nodes': []
                }
                subcategories.append(current_sub)
                # Look for table after this
                i += 1
                while i < len(lines):
                    table_line = lines[i].strip()
                    if '**Topic**' in table_line and '**Description**' in table_line:
                        # Parse table
                        table_content = []
                        i += 1  # skip the header line
                        if i < len(lines) and '---' in lines[i].strip():
                            i += 1  # skip the separator line
                        while i < len(lines) and not lines[i].strip().startswith('##'):
                            table_content.append(lines[i])
                            i += 1
                        table_str = '**Topic** | **Description**\n---|---\n' + '\n'.join(table_content)
                        nodes = parse_markdown_table(table_str)
                        if current_sub:
                            current_sub['nodes'] = nodes
                        break
                    i += 1
            else:
                print("Regex did not match")
                i += 1
        elif '**Topic**' in line and '**Description**' in line and not current_sub:
            # Direct nodes without subcategory
            table_content = []
            i += 1
            if i < len(lines) and '---' in lines[i].strip():
                i += 1
            while i < len(lines) and not lines[i].strip().startswith('##'):
                table_content.append(lines[i])
                i += 1
            table_str = '**Topic** | **Description**\n---|---\n' + '\n'.join(table_content)
            nodes = parse_markdown_table(table_str)
            if nodes:
                subcategories.append({
                    'name': 'General',
                    'nodes': nodes
                })
        else:
            i += 1

    return subcategories


async def workflow_hierarchy(source, urls, common):
    input_file = source.get('input_file')
    if not input_file:
        raise ValueError("input_file required for hierarchy workflow")
    
    explore_json_path = f"output/{input_file}"
    
    if not os.path.exists(explore_json_path):
        raise ValueError(f"Explore JSON not found: {explore_json_path}. Run explore workflow first.")
    
    with open(explore_json_path, 'r') as f:
        flat_data = json.load(f)
    
    root_url = source.get('url')
    if not root_url:
        raise ValueError("url required for hierarchy workflow")
    
    # Build hierarchy
    hierarchy = build_hierarchy(flat_data, root_url)
    
    # Save
    out_folder = common.get('out_folder', 'output')
    out_file = source.get('out_file', 'hierarchy_output')
    workflow = source.get('workflow', 'hierarchy')
    out_file_with_workflow = f"{out_file}_{workflow}.json"
    with open(f"{out_folder}/{out_file_with_workflow}", 'w') as f:
        json.dump(hierarchy, f, indent=2)
    
    print(f"Hierarchical JSON saved to {out_folder}/{out_file_with_workflow}")