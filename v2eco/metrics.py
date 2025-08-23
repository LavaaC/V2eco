from __future__ import annotations

"""Metrics and models for v2eco."""

from pydantic import BaseModel
from typing import List


class Industry(BaseModel):
    """Representation of an industry within a country."""

    name: str
    employees: int


class Country(BaseModel):
    """Country holding multiple industries."""

    name: str
    industries: List[Industry] = []


def factory_employment(country: Country) -> int:
    """Return the total number of factory employees in ``country``."""

    return sum(ind.employees for ind in country.industries)
