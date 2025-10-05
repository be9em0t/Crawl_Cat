import os
import json
from typing import Any


def ensure_dir_for_file(path: str) -> None:
    d = os.path.dirname(os.path.abspath(path))
    if d and not os.path.exists(d):
        os.makedirs(d, exist_ok=True)


def save_json(path: str, data: Any, ensure_dir: bool = True, indent: int = 2) -> None:
    if ensure_dir:
        ensure_dir_for_file(path)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=indent)


def save_text(path: str, text: str, ensure_dir: bool = True) -> None:
    if ensure_dir:
        ensure_dir_for_file(path)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
