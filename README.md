# v2eco

Minimal utilities for parsing and analyzing JSON payloads.

## Command Line Usage

The CLI exposes subcommands via ``python -m v2eco.cli``. To analyze a
country's factory employment from a JSON file, run:

```
python -m v2eco.cli analyze sample_save.json
```

Example output:

```
Steel: 1200
Textiles: 800
Total: 2000
```
