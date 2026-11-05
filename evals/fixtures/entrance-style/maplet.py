"""Synthetic local text viewer: writes the supplied text to standard output."""
import argparse

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--text", required=True, help="text to display locally")
args = parser.parse_args()
print(args.text)
