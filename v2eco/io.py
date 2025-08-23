"""Input/output helpers for v2eco."""
from __future__ import annotations

import json
from pathlib import Path
from typing import List

from .models import Country, Pop


def load_save_file(path: str | Path) -> List[Country]:
    """Load a simplified save file.

    The file is expected to be JSON with structure::

        {
            "countries": [
                {
                    "name": "CountryName",
                    "pops": [{"size": 10, "category": "laborer"}, ...]
                },
                ...
            ]
        }

    Parameters
    ----------
    path:
        Path to the JSON save file.
    """
    with open(path, "r", encoding="utf-8") as fh:
        raw = json.load(fh)

    countries: List[Country] = []
    for cdata in raw.get("countries", []):
        pops = [
            Pop(size=p["size"], category=p.get("category", "laborer"))
            for p in cdata.get("pops", [])
        ]
        countries.append(Country(name=cdata["name"], pops=pops))
    return countries
