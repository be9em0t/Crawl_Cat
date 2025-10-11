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


def save_data(path: str, data: Any, format: str, ensure_dir: bool = True, indent: int = 2) -> None:
    """
    Save data to a file in the specified format.
    
    Args:
        path: File path to save to
        data: Data to save
        format: 'json', 'markdown', or 'html'
        ensure_dir: Whether to create directories if they don't exist
        indent: Indentation for JSON (ignored for other formats)
    
    Raises:
        ValueError: If format is unsupported or data type incompatible with format
    """
    if format == 'json':
        save_json(path, data, ensure_dir, indent)
    elif format in ('markdown', 'html'):
        if not isinstance(data, str):
            raise ValueError(f"Data must be a string for {format} format, got {type(data)}")
        save_text(path, data, ensure_dir)
    else:
        raise ValueError(f"Unsupported format: {format}. Supported formats: 'json', 'markdown', 'html'")
