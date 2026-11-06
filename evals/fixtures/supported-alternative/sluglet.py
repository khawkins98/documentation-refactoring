"""Print a slug; --check remains a supported alias for --preview."""

import argparse
import re


def main():
    parser = argparse.ArgumentParser(description="Make a slug from a title.")
    parser.add_argument("--preview", "--check", action="store_true", dest="preview")
    parser.add_argument("title")
    args = parser.parse_args()
    slug = re.sub(r"[^a-z0-9]+", "-", args.title.lower()).strip("-")
    print(f"Preview: {slug}" if args.preview else slug)


if __name__ == "__main__":
    main()
