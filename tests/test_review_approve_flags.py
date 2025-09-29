import os
import sys
import json
import tempfile
import asyncio
from types import SimpleNamespace

import pytest

ROOT = os.path.dirname(os.path.dirname(__file__))
SCRIPT = os.path.join(ROOT, 'crawl_cat.py')

# We'll monkeypatch asyncio.run to simulate dom_proposed detection and ensure review-file and approve write work

async def fake_run_crawl_structure(url, api_token, provider, instruction):
    extracted = [
        {
            'topic': 'T',
            'categories': [
                {'category': 'C', 'nodes': ['A', 'B', 'C']}
            ]
        }
    ]
    return extracted, extracted

async def fake_run_crawl_content(url, api_token, provider, instruction):
    # Simulate the dom_discovery_instruction returning a dict proposal for selectors on first call
    if 'discovery' in instruction.lower():
        proposed = {
            'index_selectors': ['.index a'],
            'node_page_selectors': ['.main p.description']
        }
        return proposed, proposed
    # Simulate the content pass: return empty descriptions
    extracted = [
        {
            'topic': 'T',
            'categories': [
                {'category': 'C', 'nodes': [
                    {'name': 'A', 'description': ''},
                    {'name': 'B', 'description': ''},
                    {'name': 'C', 'description': ''}
                ]}
            ]
        }
    ]
    return extracted, extracted


def run_with_monkeypatch(tmp_path, monkeypatch, extra_args):
    # Prepare a minimal crawl YAML
    yaml_path = tmp_path / 'test_crawl.yml'
    yaml_content = {
        'name': 'test_crawl',
        'url': 'https://example.com',
        'provider': 'openai/gpt-4.1',
        'structure_instruction': 'structure',
        'content_instruction': 'content',
        'dom_discovery_instruction': 'Please run discovery',
        'output_prefix': str(tmp_path / 'test_crawl')
    }
    import yaml as _yaml
    with open(yaml_path, 'w', encoding='utf-8') as f:
        _yaml.safe_dump(yaml_content, f)

    # monkeypatch asyncio.run
    orig_asyncio_run = asyncio.run
    call = {'n': 0}

    def fake_asyncio_run(coro):
        call['n'] += 1
        if call['n'] == 1:
            return orig_asyncio_run(fake_run_crawl_structure(None, None, None, None))
        elif call['n'] == 2:
            # simulate the discovery call
            return orig_asyncio_run(fake_run_crawl_content(None, None, None, 'discovery'))
        else:
            return orig_asyncio_run(fake_run_crawl_content(None, None, None, 'content'))

    monkeypatch.setattr(asyncio, 'run', fake_asyncio_run)

    # Run script
    sys.path.insert(0, ROOT)
    import crawl_cat

    old_argv = sys.argv
    try:
        sys.argv = ['crawl_cat.py', str(yaml_path), '--content'] + extra_args
        crawl_cat.main()
    finally:
        sys.argv = old_argv

    return yaml_path


def test_review_and_review_file_and_approve(tmp_path, monkeypatch):
    # Run with --review and --review-file to save proposal
    yaml_path = run_with_monkeypatch(tmp_path, monkeypatch, ['--review', '--review-file', str(tmp_path / 'proposal.json')])

    # Check that proposal file exists and contains selectors
    pf = tmp_path / 'proposal.json'
    assert pf.exists()
    with open(pf, 'r', encoding='utf-8') as f:
        data = json.load(f)
    assert 'node_page_selectors' in data or 'index_selectors' in data

    # Now run approve using the saved file
    # Ensure the original YAML does not have dom_selectors
    import yaml as _yaml
    with open(yaml_path, 'r', encoding='utf-8') as f:
        cfg = _yaml.safe_load(f)
    assert not cfg.get('dom_selectors')

    # Run main with --approve and --review-file pointing to proposal.json
    sys_argv_save = sys.argv
    try:
        sys.argv = ['crawl_cat.py', str(yaml_path), '--content', '--approve', '--review-file', str(pf)]
        # monkeypatch asyncio.run again to simulate calls during approve run
        import crawl_cat
        crawl_cat.main()
    finally:
        sys.argv = sys_argv_save

    # YAML should now contain dom_selectors
    with open(yaml_path, 'r', encoding='utf-8') as f:
        cfg2 = _yaml.safe_load(f)
    assert 'dom_selectors' in cfg2
    # ensure node_page_selectors present
    ds = cfg2['dom_selectors']
    assert 'node_page_selectors' in ds or 'index_selectors' in ds
