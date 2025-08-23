"""Metrics helpers for v2eco."""
from __future__ import annotations

from .models import Country


def soldier_count(country: Country) -> int:
    """Return the total number of soldiers in ``country``.

    Parameters
    ----------
    country:
        Country for which to count pops with category ``"soldier"``.
    """
    return sum(pop.size for pop in country.pops if pop.category == "soldier")
