import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LABS = sorted((ROOT / "labs").glob("[0-9][0-9]_*"))


def test_all_five_labs_have_required_artifacts():
    assert len(LABS) == 5
    required = {"notebook.ipynb", "notebook.py", "README.md", "exercises.md", "solution.py", "test_lab.py"}
    for lab in LABS:
        assert required <= {p.name for p in lab.iterdir()}
        assert len(json.loads((lab / "notebook.ipynb").read_text(encoding="utf-8"))["cells"]) >= 3
        assert (lab / "exercises.md").read_text(encoding="utf-8").count("## 练习") >= 5


def test_every_solution_imports():
    for lab in LABS:
        spec = importlib.util.spec_from_file_location(f"workshop_{lab.name}", lab / "solution.py")
        assert spec and spec.loader
        module = importlib.util.module_from_spec(spec)  # type: ignore[arg-type]
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
