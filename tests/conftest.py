import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LAB_DIRS = sorted((ROOT / "labs").glob("[0-9][0-9]_*"))
for lab in LAB_DIRS:
    sys.path.insert(0, str(lab))
