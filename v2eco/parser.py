"""Parsing utilities using Pydantic models."""
from __future__ import annotations

from pydantic import BaseModel
import json


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
