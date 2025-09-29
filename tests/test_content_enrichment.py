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


def run_script_with_mocks(tmp_path, monkeypatch):
    # prepare a minimal crawl YAML
    yaml_path = tmp_path / 'test_crawl.yml'
    yaml_content = {
        'name': 'test_crawl',
        'url': 'https://example.com',
        'provider': 'local/none',
        'structure_instruction': 'structure',
        'content_instruction': 'content',
        'output_prefix': str(tmp_path / 'test_crawl')
    }
    import yaml as _yaml
    with open(yaml_path, 'w', encoding='utf-8') as f:
        _yaml.safe_dump(yaml_content, f)

    # monkeypatch run_crawl used in crawl_cat.py by replacing asyncio.run to route calls
    orig_asyncio_run = asyncio.run

    call_count = {'n': 0}

    def fake_asyncio_run(coro):
        # coroutine will be a call to run_crawl(...) coroutine
        call_count['n'] += 1
        if call_count['n'] == 1:
            return orig_asyncio_run(fake_run_crawl_structure(None, None, None, None))
        else:
            return orig_asyncio_run(fake_run_crawl_content(None, None, None, None))

    monkeypatch.setattr(asyncio, 'run', fake_asyncio_run)

    # Run the script as a module
    env = os.environ.copy()
    # ensure no real API token requirement
    env.pop('OPENAI_API_KEY', None)
    env.pop('ANTHROPIC_API_KEY', None)
    env.pop('HUGGINGFACE_API_TOKEN', None)

    # execute the script's main()
    sys.path.insert(0, ROOT)
    import crawl_cat
    # call main with args
    monkeypatch.setattr(sys, 'argv', ['crawl_cat.py', str(yaml_path), '--content'])
    crawl_cat.main()

    # return path to enriched output
    enriched_out = tmp_path / 'test_crawl_enriched.json'
    return enriched_out


def test_content_enrichment_creates_enriched_file(tmp_path, monkeypatch):
    enriched_out = run_script_with_mocks(tmp_path, monkeypatch)
    assert enriched_out.exists(), 'enriched output file was not created'

    with open(enriched_out, 'r', encoding='utf-8') as f:
        enriched = json.load(f)

    assert isinstance(enriched, list)
    assert len(enriched) == 1
    topic = enriched[0]
    assert 'categories' in topic
    cats = topic['categories']
    assert len(cats) == 1
    nodes = cats[0]['nodes']
    assert isinstance(nodes, list)
    assert len(nodes) == 2
    for n in nodes:
        assert isinstance(n, dict)
        assert 'name' in n and 'description' in n
        assert n['description'] and len(n['description']) > len(n['name'])
