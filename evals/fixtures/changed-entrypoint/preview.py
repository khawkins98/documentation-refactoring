"""Synthetic control probe for the viewer's former launch flow."""
from html.parser import HTMLParser
from pathlib import Path


class Controls(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        if tag == "button":
            self.ids.add(dict(attrs).get("id"))


if __name__ == "__main__":
    controls = Controls()
    controls.feed(Path(__file__).with_name("app.html").read_text())
    if "launch-classic" not in controls.ids:
        raise SystemExit("ERROR: launch control #launch-classic not found")
    print("Preview control found")
