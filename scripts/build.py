"""Validate the showcase inventory and assemble its public website with Python 3."""
from pathlib import Path, PurePosixPath
import argparse
import os
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]


def fail(message):
    raise SystemExit(message)


def inventory():
    paths = (ROOT / "release-files.txt").read_text(encoding="utf-8").splitlines()
    if not paths or paths != sorted(set(paths)):
        fail("The release inventory must be sorted and contain unique paths.")
    for name in paths:
        p = PurePosixPath(name)
        if p.is_absolute() or str(p) != name or ".." in p.parts or not p.parts:
            fail(f"Invalid inventory path: {name}")
        if name not in {".gitignore", ".github/workflows/pages.yml"} and any(part.startswith(".") for part in p.parts):
            fail(f"Hidden file outside the release inventory contract: {name}")
        source = ROOT / p
        if not source.is_file() or source.resolve() != source or source.stat().st_size == 0:
            fail(f"Missing, empty or symbolic source: {name}")
    return set(paths)


def verify_tree(expected):
    result = subprocess.run(["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
                            cwd=ROOT, check=True, capture_output=True)
    found = {os.fsdecode(path) for path in result.stdout.split(b"\0") if path}
    if found != expected:
        fail(f"Repository inventory differs: {sorted(found ^ expected)}")


def build(paths):
    output = ROOT / "dist"
    if output.is_symlink() or (output.exists() and not output.is_dir()):
        fail("Expected a local dist directory.")
    with tempfile.TemporaryDirectory(dir=ROOT, prefix=".build-") as workspace:
        target = Path(workspace) / "site"
        for name in sorted(path for path in paths if path.startswith("site/")):
            relative = Path(name).relative_to("site")
            destination = target / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / name, destination)
        if not (target / "index.html").is_file():
            fail("Missing English landing page.")
        previous = Path(workspace) / "previous"
        if output.exists():
            output.rename(previous)
        try:
            target.rename(output)
        except OSError:
            if previous.exists():
                previous.rename(output)
            raise
    print(f"Built {sum(p.is_file() for p in output.rglob('*'))} static files into dist/")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify-tree", action="store_true", help="Compare the Git inventory before building.")
    args = parser.parse_args()
    paths = inventory()
    if args.verify_tree:
        verify_tree(paths)
    build(paths)
