"""Command line interface for :mod:`v2eco`.

The CLI exposes two main entry points:

``analyze``
    Parse a JSON payload and run the simple analysis used in the tests.

``goods``
    Inspect a mod description and report which states produce goods and how
    many craftsmen are present.  A specific good can be supplied to filter
    the output.

Example
-------

To list the states producing ``grain`` from ``mod.json``::

    $ python -m v2eco.cli goods mod.json grain
    grain:
      raw: State A, State B
    Craftsmen per state:
      State A: 1200
      State B: 800

"""

from __future__ import annotations

import argparse
from typing import Optional

from .parser import parse_input, load_mod
from .analyzer import analyze_data


def build_parser() -> argparse.ArgumentParser:
    """Return the top level argument parser."""

    parser = argparse.ArgumentParser(prog="v2eco")
    sub = parser.add_subparsers(dest="command")

    analyze_p = sub.add_parser("analyze", help="Analyze a JSON payload")
    analyze_p.add_argument("payload", help="JSON string to parse and analyze")

    goods_p = sub.add_parser(
        "goods", help="List where goods are produced and craftsmen counts"
    )
    goods_p.add_argument("mod", help="Path to a mod file")
    goods_p.add_argument("good", nargs="?", help="Filter to a specific good")

    return parser


def handle_goods(mod_path: str, good_filter: Optional[str]) -> None:
    """Print information about goods produced in each state."""

    data = load_mod(mod_path)
    states = data.get("states", [])

    goods_map: dict[str, dict[str, list[str]]] = {}
    craftsmen: dict[str, int] = {}

    for state in states:
        name = state.get("name", "Unknown")
        craftsmen[name] = int(state.get("craftsmen", 0))
        for g in state.get("raw_goods", []):
            goods_map.setdefault(g, {"raw": [], "processed": []})["raw"].append(name)
        for g in state.get("processed_goods", []):
            goods_map.setdefault(g, {"raw": [], "processed": []})["processed"].append(name)

    if good_filter:
        goods_map = {good_filter: goods_map.get(good_filter, {"raw": [], "processed": []})}

    for good, where in goods_map.items():
        print(f"{good}:")
        if where["raw"]:
            print(f"  raw: {', '.join(where['raw'])}")
        if where["processed"]:
            print(f"  processed: {', '.join(where['processed'])}")

    if craftsmen:
        print("Craftsmen per state:")
        for state, count in sorted(craftsmen.items()):
            print(f"  {state}: {count}")


def main(argv: Optional[list[str]] = None) -> None:
    """Entry point used by ``python -m v2eco.cli``."""

    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "analyze":
        model = parse_input(args.payload)
        result = analyze_data(model)
        print(result)
    elif args.command == "goods":
        handle_goods(args.mod, getattr(args, "good", None))
    else:  # pragma: no cover - argparse shows help
        parser.print_help()


if __name__ == "__main__":  # pragma: no cover
    main()

