"""Print the selected URL; this preview does not fetch or download anything."""
import argparse

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--prototype", action="store_true")
args = parser.parse_args()

mapx_url = "https://catalog.example.test/exports/regions.csv"
inventory_url = "https://files.example.test/regions.csv"
print(inventory_url if args.prototype else mapx_url)
