"""Command line interface for v2eco."""
from __future__ import annotations

import json
import click

from .parser import parse_input
from .analyzer import analyze_data
from .metrics import Country, factory_employment


@click.group()
def main() -> None:
    """Entry point for v2eco commands."""


@main.command("parse")
@click.argument("payload")
def parse_cmd(payload: str) -> None:
    """Parse ``payload`` and print analysis result."""
    model = parse_input(payload)
    result = analyze_data(model)
    click.echo(result)


@main.command("analyze")
@click.argument("path")
def analyze_cmd(path: str) -> None:
    """Print each industry's employees and country total from ``path``."""
    with open(path) as fh:
        data = json.load(fh)
    country = Country(**data)
    for ind in country.industries:
        click.echo(f"{ind.name}: {ind.employees}")
    total = factory_employment(country)
    click.echo(f"Total: {total}")


if __name__ == "__main__":  # pragma: no cover
    main()
