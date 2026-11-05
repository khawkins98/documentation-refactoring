# Tidy

Normalize trailing spaces in a text file. Tidy reads a text file and removes
spaces at the end of its lines. This utility makes line endings tidy by removing
unneeded trailing whitespace.

## Install

Use Python 3. No packages need installing.

## Usage

```sh
python3 tidy.py --out clean.txt input.txt
```

Use `--force` to overwrite a file. You can preview with `--check`.
Input and output are separate paths.

## Options

- `--out PATH`: the output file.
- `--check`: print what would happen.

Tidy removes spaces from line endings. The command above removes trailing spaces
from input.txt and writes clean.txt. Use this when you want whitespace cleaned.
