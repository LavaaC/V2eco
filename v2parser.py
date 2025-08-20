"""Utilities for reading .v2 save files."""

from __future__ import annotations

import gzip
import zlib
import re
from typing import Iterator, Dict, Any

_token_pattern = re.compile(r'\{|\}|"[^"]*"|[^\s{}]+')


def _decompress(data: bytes) -> str:
    """Return UTF-8 text from gzipped or zlib-compressed data."""
    if data[:2] == b"\x1f\x8b":
        return gzip.decompress(data).decode("utf-8")
    return zlib.decompress(data).decode("utf-8")


def _tokenize(text: str) -> Iterator[str]:
    for match in _token_pattern.finditer(text):
        yield match.group(0)


def _parse_tokens(tokens: Iterator[str]) -> Dict[str, Any]:
    result: Dict[str, Any] = {}
    key: str | None = None
    for token in tokens:
        if token == '}':
            break
        elif token == '{':
            if key is None:
                # Start of top-level block.
                result.update(_parse_tokens(tokens))
            else:
                result[key] = _parse_tokens(tokens)
                key = None
        else:
            value = token.strip('"')
            if key is None:
                key = value
            else:
                result[key] = value
                key = None
    return result


def parse_save(path: str) -> Dict[str, Any]:
    """Parse a compressed `.v2` save file into a dictionary.

    Parameters
    ----------
    path: str
        Path to the `.v2` file.

    Returns
    -------
    dict
        Nested representation of the file.
    """
    with open(path, 'rb') as fh:
        data = fh.read()
    text = _decompress(data)
    tokens = ['{'] + list(_tokenize(text)) + ['}']
    return _parse_tokens(iter(tokens))
