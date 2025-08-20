"""Analysis helpers for processed data."""
from __future__ import annotations

from .parser import DataModel


def analyze_data(model: DataModel) -> int:
    """Perform a trivial analysis on ``DataModel``.

    Currently returns the square of ``value`` to demonstrate functionality.
    """
    return model.value ** 2
