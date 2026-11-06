import argparse
from pathlib import Path

parser = argparse.ArgumentParser(description="Normalize trailing spaces in a text file")
parser.add_argument("input", type=Path)
parser.add_argument("--output", type=Path, required=True)
parser.add_argument("--dry-run", action="store_true")
args = parser.parse_args()
text = "\n".join(line.rstrip() for line in args.input.read_text().splitlines()) + "\n"
if args.dry_run:
    print(f"Would write {args.output}")
else:
    args.output.write_text(text)
