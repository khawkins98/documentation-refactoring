import hashlib
import os
from pathlib import Path

configured = os.environ.get("REFERENCE_TABLE_PATH")
if not configured:
    raise SystemExit("REFERENCE_TABLE_PATH is not configured")
path = Path(configured)
if not path.is_file():
    raise SystemExit("Configured reference file does not exist")
if hashlib.sha256(path.read_bytes()).hexdigest() != "6c3da692ced8184e12744f3bd078cf725af20c5a4e0b2e64e801fe21d053b488":
    raise SystemExit("Reference does not match the pinned version")
print("Reference table matches the pinned fixture")
