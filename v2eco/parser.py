"""Parsing utilities using Pydantic models."""
from __future__ import annotations

from pydantic import BaseModel
import json
from typing import Any, Dict


class DataModel(BaseModel):
    """Simple data model representing input payload."""
    name: str
    value: int


def parse_input(raw: str) -> DataModel:
    """Parse a JSON string into a :class:`DataModel`.

    Parameters
    ----------
    raw: str
        JSON string containing ``name`` and ``value`` fields.
    """
    data = json.loads(raw)
    return DataModel(**data)


def load_mod(path: str) -> Dict[str, Any]:
    """Load a JSON mod description.

    The expected format is a mapping containing a ``states`` key whose value
    is a list of state definitions.  Each state may define ``raw_goods`` and
    ``processed_goods`` lists and a ``craftsmen`` count.

    Parameters
    ----------
    path: str
        Path to the JSON file describing the mod.

    Returns
    -------
    dict
        Parsed representation of the mod file.
    """

    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)
