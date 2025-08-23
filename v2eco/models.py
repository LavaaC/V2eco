"""Data models for v2eco."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import List


@dataclass
class Pop:
    """Representation of a population unit.

    Parameters
    ----------
    size:
        Number of individuals in the pop.
    category:
        Type of pop such as ``"laborer"`` or ``"soldier"``.
    """

    size: int
    category: str = "laborer"


@dataclass
class Country:
    """Simple country model containing pops."""

    name: str
    pops: List[Pop] = field(default_factory=list)
