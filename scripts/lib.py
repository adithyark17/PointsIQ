"""Shared helpers for the PointsIQ vault generators."""

from __future__ import annotations

import re
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "data"
VAULT_DIR = REPO_ROOT / "vault"

GENERATED_MARKER = "<!-- generated: edits above this line will be overwritten -->"

# Characters Obsidian cannot use in note names (plus path separators).
_FORBIDDEN = re.compile(r'[\\/:#^|\[\]?*"<>]')


def load_yaml(path: Path):
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def wikilink(name: str) -> str:
    return f"[[{name}]]"


def safe_filename(name: str) -> str:
    return _FORBIDDEN.sub("-", name).strip()


def render_frontmatter(fm: dict) -> str:
    """Render frontmatter preserving key order; wikilinks come out quoted."""
    dumped = yaml.safe_dump(
        fm, sort_keys=False, allow_unicode=True, default_flow_style=False, width=1000
    )
    return f"---\n{dumped}---\n"


def emit_note(path: Path, frontmatter: dict, body: str) -> Path:
    """Write a generated note, preserving any manual content below the marker."""
    manual_tail = ""
    if path.exists():
        existing = path.read_text(encoding="utf-8")
        if GENERATED_MARKER in existing:
            manual_tail = existing.split(GENERATED_MARKER, 1)[1].rstrip("\n")

    content = render_frontmatter(frontmatter)
    body = body.strip("\n")
    if body:
        content += "\n" + body + "\n"
    content += "\n" + GENERATED_MARKER + "\n"
    if manual_tail:
        content += manual_tail + "\n"

    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists() or path.read_text(encoding="utf-8") != content:
        path.write_text(content, encoding="utf-8")
    return path


def prune_folder(folder: Path, keep: set[Path]) -> list[Path]:
    """Delete generated .md files in *folder* that were not emitted this run."""
    removed = []
    if not folder.exists():
        return removed
    for md in folder.rglob("*.md"):
        if md not in keep:
            md.unlink()
            removed.append(md)
    return removed
