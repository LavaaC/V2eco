"""Helpers for loading economic data from mod files.

The parser understands a very small subset of the Paradox-style text
format used by Victoria 2. The expected layout is::

    STATE_NAME = {
        owner = TAG
        goods = {
            GOOD_A = 10
            GOOD_B = 5
        }
    }

Each top-level key represents a state. ``=`` signs between keys and values
are optional and ignored. Only the ``owner`` field and a ``goods`` block of
``good = craftsmen`` pairs are interpreted. Anything else in the file is
ignored.
"""

from __future__ import annotations

from typing import Iterator, List
from .models import State, Good
import re

_token_pattern = re.compile(r"\{|\}|\"[^\"]*\"|[^\s{}]+")


def _tokenize(text: str) -> Iterator[str]:
    """Yield meaningful tokens from ``text``.

    The format optionally uses ``=`` between keys and values; these
    separators are ignored so the downstream parser can operate on a
    simple ``key value`` stream.
    """
    for match in _token_pattern.finditer(text):
        token = match.group(0)
        if token == "=":
            continue
        yield token


def _parse_tokens(tokens: Iterator[str]) -> dict:
    """Recursively parse tokens into a dictionary structure."""
    result: dict = {}
    key: str | None = None
    for token in tokens:
        if token == '}':
            break
        if token == '{':
            if key is None:
                result.update(_parse_tokens(tokens))
            else:
                result[key] = _parse_tokens(tokens)
                key = None
            continue
        value = token.strip('"')
        if key is None:
            key = value
        else:
            result[key] = value
            key = None
    return result


def load_mod(path: str) -> List[State]:
    """Parse a mod file into :class:`State` objects.

    Parameters
    ----------
    path:
        Path to the mod definition file.

    Returns
    -------
    list[State]
        One :class:`State` per state block found in the file.
    """
    with open(path, 'r', encoding='utf-8') as fh:
        text = fh.read()

    tokens = ['{'] + list(_tokenize(text)) + ['}']
    data = _parse_tokens(iter(tokens))
    states: List[State] = []
    for state_name, details in data.items():
        owner = str(details.get('owner', ''))
        goods_block = details.get('goods', {})
        goods: List[Good] = []
        if isinstance(goods_block, dict):
            for g_name, craftsmen in goods_block.items():
                try:
                    craftsmen_int = int(craftsmen)
                except (TypeError, ValueError):
                    craftsmen_int = 0
                goods.append(Good(name=g_name, craftsmen=craftsmen_int))
        states.append(State(name=state_name, owner=owner, goods=goods))
    return states
