"""Command line interface for v2eco."""
from __future__ import annotations

import click

from .parser import parse_input
from .analyzer import analyze_data
from .io import load_save_file
from .metrics import soldier_count


@click.command()
@click.argument("payload")
def main(payload: str) -> None:
    """Parse ``payload`` and print analysis result."""
    model = parse_input(payload)
    result = analyze_data(model)
    click.echo(result)


@click.command()
@click.argument("save_file")
def analyze_cmd(save_file: str) -> None:
    """Load ``save_file`` and print soldier counts per country."""
    countries = load_save_file(save_file)
    for country in countries:
        click.echo(f"{country.name}: {soldier_count(country)}")


if __name__ == "__main__":  # pragma: no cover
    main()
