import os
import json
from bs4 import BeautifulSoup

import pytest

import sys
import os
ROOT = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, ROOT)
from crawl_cat import extract_meta_or_first_p, extract_text_by_selectors_from_soup


def test_extract_meta_or_first_p_prefers_meta():
    html = '<html><head><meta name="description" content="Meta description here"></head><body><p>First paragraph</p></body></html>'
    soup = BeautifulSoup(html, 'html.parser')
    assert extract_meta_or_first_p(soup) == 'Meta description here'


def test_extract_meta_or_first_p_after_header():
    html = '<html><body><h1>NodeName</h1><p>This is the descriptive paragraph after header.</p></body></html>'
    soup = BeautifulSoup(html, 'html.parser')
    assert 'descriptive paragraph' in extract_meta_or_first_p(soup)


def test_extract_text_by_selectors_from_soup_simple():
    html = '<html><body><div class="desc">Important description text.</div></body></html>'
    soup = BeautifulSoup(html, 'html.parser')
    sel = ['.desc']
    assert 'Important description' in extract_text_by_selectors_from_soup(soup, sel)


def test_extract_text_by_selectors_from_soup_handles_missing():
    html = '<html><body><p>No match here</p></body></html>'
    soup = BeautifulSoup(html, 'html.parser')
    sel = ['.nope']
    assert extract_text_by_selectors_from_soup(soup, sel) is None
