"""Command line interface for v2eco."""
from __future__ import annotations

import click

from .parser import parse_input
from .analyzer import analyze_data


@click.command()
@click.argument("payload")
def main(payload: str) -> None:
    """Parse ``payload`` and print analysis result."""
    model = parse_input(payload)
    result = analyze_data(model)
    click.echo(result)


if __name__ == "__main__":  # pragma: no cover
    main()
