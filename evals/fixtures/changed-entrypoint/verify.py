"""A passing public check can coexist with warnings and an omitted private check."""
from pathlib import Path
from preview import Controls

if __name__ == "__main__":
    controls = Controls()
    controls.feed(Path(__file__).with_name("app.html").read_text())
    if "play-current" not in controls.ids:
        raise SystemExit("ERROR: current Play control is missing")
    print("PASS: current Play control exists")
    print("WARN: layout still requires manual review")
    reference = Path(__file__).with_name("reference.bin")
    if not reference.exists():
        print("SKIP: reference rendering check; reference.bin is not supplied")
    elif reference.read_bytes() != b"demo-reference-v1\n":
        raise SystemExit("ERROR: reference version mismatch")
    else:
        print("PASS: reference version accepted; pixels still require manual review")
