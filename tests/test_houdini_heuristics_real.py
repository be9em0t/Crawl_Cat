import os
import json
import requests
from bs4 import BeautifulSoup
import yaml
import pytest
from dotenv import load_dotenv


def load_houdini_config():
    cfg_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'houdini_obj_nodes.yml')
    with open(cfg_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def extract_node_links_from_index(soup, base_url):
    links = []
    for a in soup.find_all('a', href=True):
        txt = (a.get_text() or '').strip()
        if not txt:
            continue
        href = a['href']
        # consider links pointing to .html pages with meaningful link text
        if not href.endswith('.html'):
            continue
        # skip very short or noise-like link texts
        if len(txt) < 3:
            continue
        if txt.startswith('\u00a0') or txt.startswith('Â'):
            continue
        # common cruft
        if txt.lower() in ('nodes', 'index', 'houdini 20.5', 'objects'):
            continue
        links.append((txt, href))
    # deduplicate preserving order
    seen = set()
    out = []
    for name, href in links:
        if name.lower() in seen:
            continue
        seen.add(name.lower())
        out.append((name, href))
    return out


def get_soup(url):
    resp = requests.get(url, timeout=10, headers={'User-Agent': 'crawl-cat-test/1.0'})
    resp.raise_for_status()
    return BeautifulSoup(resp.text, 'html.parser')


def extract_meta_or_first_p(soup):
    if not soup:
        return None
    m = soup.find('meta', attrs={'name': 'description'}) or soup.find('meta', attrs={'property': 'og:description'})
    if m and m.get('content'):
        return m.get('content').strip()
    p = soup.find('p')
    if p and p.get_text(strip=True):
        return p.get_text(' ', strip=True)
    return None


def find_nearby_description(index_soup, node_name):
    node_lower = node_name.strip().lower()
    # search anchors for exact match
    for a in index_soup.find_all('a'):
        txt = (a.get_text() or '').strip()
        if not txt:
            continue
        if node_lower == txt.lower() or node_lower in txt.lower():
            # title attr
            if a.get('title'):
                return a.get('title').strip()
            # next sibling paragraph or text
            ns = a.find_next_sibling()
            if ns and ns.get_text(strip=True):
                return ns.get_text(' ', strip=True)
            p = a.find_parent('p')
            if p and p.get_text(strip=True):
                return p.get_text(' ', strip=True)
    return None


@pytest.mark.network
def test_houdini_index_has_descriptions_for_sample_nodes(capsys):
    cfg = load_houdini_config()
    url = cfg.get('url')
    assert url, 'houdini config must include url'
    # Run the script in-process with --content so DOM fallback + heuristics run and produce enriched output
    import sys
    sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
    import crawl_cat
    houdini_yaml = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'houdini_obj_nodes.yml')
    # Load repository .env so hosted LLM API keys are available to the test (matches runtime)
    repo_root = os.path.dirname(os.path.dirname(__file__))
    dotenv_path = os.path.join(repo_root, '.env')
    load_dotenv(dotenv_path)

    old_argv = sys.argv
    try:
        sys.argv = ['crawl_cat.py', houdini_yaml, '--content']
        crawl_cat.main()
    finally:
        sys.argv = old_argv

    enriched_path = os.path.join(os.getcwd(), 'houdini_obj_nodes_enriched.json')
    assert os.path.exists(enriched_path), 'enriched output not produced by script'

    with open(enriched_path, 'r', encoding='utf-8') as f:
        enriched = json.load(f)

    # find Agent Cam node
    target = None
    for topic in enriched:
        for c in topic.get('categories', []):
            for n in c.get('nodes', []):
                if n.get('name') == 'Agent Cam':
                    target = n
                    break
            if target:
                break
        if target:
            break

    assert target is not None, 'Agent Cam node not found in enriched output'
    desc = (target.get('description') or '').strip()
    assert 'Create and attach camera to a crowd agent' in desc, f'Unexpected Agent Cam description: {desc}'
