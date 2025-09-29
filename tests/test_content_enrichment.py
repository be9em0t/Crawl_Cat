import os
import sys
import json
import asyncio
import tempfile
from types import SimpleNamespace

import pytest

ROOT = os.path.dirname(os.path.dirname(__file__))
SCRIPT = os.path.join(ROOT, 'crawl_cat.py')


class DummyResult:
    def __init__(self, extracted_content, normalized):
        self.extracted_content = json.dumps(extracted_content) if not isinstance(extracted_content, str) else extracted_content
        self.normalized = normalized


async def fake_run_crawl_structure(url, api_token, provider, instruction):
    # Return a simple canonical normalized structure: one topic, one category, 2 nodes
    extracted = [
        {
            'topic': 'TestTopic',
            'categories': [
                {'category': 'CatA', 'nodes': ['NodeOne', 'NodeTwo']}
            ]
        }
    ]
    normalized = extracted
    return extracted, normalized


async def fake_run_crawl_content(url, api_token, provider, instruction):
    # Simulate content pass returning nodes as objects with descriptions
    extracted = [
        {
            'topic': 'TestTopic',
            'categories': [
                {'category': 'CatA', 'nodes': [
                    {'name': 'NodeOne', 'description': 'A long description for NodeOne that is clearly longer than the name.'},
                    {'name': 'NodeTwo', 'description': 'NodeTwo does something different and has a longer description.'}
                ]}
            ]
        }
    ]
    normalized = extracted
    return extracted, normalized


def run_script_with_mocks(tmp_path):
    # prepare a minimal crawl YAML
    # This test is integration-style and requires a real hosted LLM API key to run live.
    # Fail loudly with a clear message if no API key is present (we keep secrets local).
    if not os.environ.get('OPENAI_API_KEY') and not os.environ.get('ANTHROPIC_API_KEY') and not os.environ.get('HUGGINGFACE_API_TOKEN'):
        raise AssertionError('Integration test requires a hosted LLM API key in environment (OPENAI_API_KEY, ANTHROPIC_API_KEY, or HUGGINGFACE_API_TOKEN)')

    yaml_path = tmp_path / 'test_crawl.yml'
    yaml_content = {
        'name': 'test_crawl',
        'url': 'https://example.com',
        # require a hosted provider for live testing; let the global env decide which key is present
        'provider': 'openai/gpt-4.1',
        'structure_instruction': 'structure',
        'content_instruction': 'content',
        'output_prefix': str(tmp_path / 'test_crawl')
    }
    import yaml as _yaml
    with open(yaml_path, 'w', encoding='utf-8') as f:
        _yaml.safe_dump(yaml_content, f)

    # Run the script in-process with the current environment (this is an integration test)
    sys.path.insert(0, ROOT)
    import importlib
    import crawl_cat
    # call main with args to produce enriched output
    sys_argv_save = sys.argv
    try:
        sys.argv = ['crawl_cat.py', str(yaml_path), '--content']
        crawl_cat.main()
    finally:
        sys.argv = sys_argv_save

    # return path to enriched output
    enriched_out = tmp_path / 'test_crawl_enriched.json'
    return enriched_out


def test_content_enrichment_creates_enriched_file(tmp_path):
    enriched_out = run_script_with_mocks(tmp_path)
    assert enriched_out.exists(), 'enriched output file was not created'

    with open(enriched_out, 'r', encoding='utf-8') as f:
        enriched = json.load(f)

    # Validate shape rather than exact counts (live LLM output may vary)
    assert isinstance(enriched, list)
    assert len(enriched) >= 1
    topic = enriched[0]
    assert 'categories' in topic
    cats = topic['categories']
    assert isinstance(cats, list) and len(cats) >= 1
    # Pick the first category and ensure it contains nodes with expected keys
    nodes = cats[0].get('nodes')
    assert isinstance(nodes, list) and len(nodes) >= 1
    found_valid_desc = False
    for n in nodes:
        assert isinstance(n, dict)
        assert 'name' in n and 'description' in n
        assert isinstance(n['name'], str) and n['name'].strip() != ''
        assert isinstance(n['description'], str)
        if n['description'].strip():
            found_valid_desc = True
    # At least one node should have a non-empty description in a successful enrichment
    assert found_valid_desc
