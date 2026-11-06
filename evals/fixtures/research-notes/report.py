import argparse
parser = argparse.ArgumentParser(description="Print a scoped fixture report")
parser.add_argument("--format", choices=["text", "json"], default="text")
args = parser.parse_args()
print('{"rows": 3, "scope": "fixture only"}' if args.format == "json" else "3 fixture rows; no general inference")
