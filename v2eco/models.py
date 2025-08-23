"""Data models for mod state economics.

The :mod:`v2eco.models` module defines dataclasses representing ownership
and goods production within a state. These are used by :func:`v2eco.mod_io.load_mod`
to interpret mod files.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass
class Good:
    """A good produced within a state.

    Attributes
    ----------
    name:
        Identifier of the good.
    craftsmen:
        Number of craftsmen producing the good.
    """

    name: str
    craftsmen: int


@dataclass
class State:
    """Economic information for a state.

    Attributes
    ----------
    name:
        Name of the state as defined in the mod file.
    owner:
        Country tag owning the state.
    goods:
        Goods produced in the state with associated craftsmen counts.
    """

    name: str
    owner: str
    goods: List[Good]
