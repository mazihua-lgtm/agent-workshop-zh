import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LAB_DIRS = sorted((ROOT / "labs").glob("[0-9][0-9]_*"))


def pytest_pycollect_makemodule(module_path, parent):
    """Make each lab's local solution importable while pytest imports its test module."""
    path = Path(str(module_path))
    if path.name != "test_lab.py" or path.parent.parent.name != "labs":
        return None
    spec = importlib.util.spec_from_file_location("solution", path.parent / "solution.py")
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules["solution"] = module
    spec.loader.exec_module(module)
    return None
