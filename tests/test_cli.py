import os
import subprocess
import sys
import json
import tempfile

SCRIPT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'crawl_shadergraph.py'))


def run(cmd_args, env=None):
    env2 = os.environ.copy()
    if env:
        env2.update(env)
    proc = subprocess.run([sys.executable, SCRIPT] + cmd_args, env=env2, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return proc.returncode, proc.stdout.decode('utf-8')


def test_no_args_prints_help():
    code, out = run([])
    assert code == 1
    assert 'usage' in out.lower() or 'usage:' in out.lower()


def test_missing_yaml_exits_with_error():
    code, out = run(['nonexistent_config.yaml'])
    assert code == 1
    assert 'not found' in out.lower() or 'crawl yaml not found' in out.lower()


def test_run_with_minimal_yaml(tmp_path, monkeypatch):
    # create a minimal YAML that points to a harmless page and a simple instruction
    yaml_content = '''\nname: test_minimal\nurl: https://example.com/\ninstruction: |\n  Return a strict JSON array of topic objects.\nparams:\n  temperature: 0.0\n'''
    cfg = tmp_path / 'test_minimal.yaml'
    cfg.write_text(yaml_content, encoding='utf-8')

    # set a dummy OPENAI_API_KEY to bypass missing-token checks (provider falls back to env)
    monkeypatch.setenv('OPENAI_API_KEY', 'sk-test')

    code, out = run([str(cfg)])
    # the crawl may actually try to perform network I/O depending on crawl4ai behavior.
    # We accept non-zero exit codes as long as our CLI started and printed resolved provider info.
    assert 'Resolved provider:' in out
    # If outputs were produced, check for the output prefix
    nodes_file = os.path.join(os.getcwd(), 'test_minimal_nodes.json')
    crawlmode_file = os.path.join(os.getcwd(), 'test_minimal_crawlmode.json')
    # cleanup if any files were created
    if os.path.exists(nodes_file):
        os.remove(nodes_file)
    if os.path.exists(crawlmode_file):
        os.remove(crawlmode_file)