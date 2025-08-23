# v2eco

Utilities for parsing and analyzing data with a small command line
interface.

## Goods lookup

The CLI exposes a ``goods`` subcommand that reports where goods are
produced and how many craftsmen are present in each state.  Pass the path to
the mod description followed by an optional good name to filter the output.

```bash
$ python -m v2eco.cli goods mod.json grain
grain:
  raw: State A, State B
Craftsmen per state:
  State A: 1200
  State B: 800
```

The example above shows that *grain* is produced as a raw good in
``State A`` and ``State B``.  The summary at the end lists the number of
craftsmen in those states.
