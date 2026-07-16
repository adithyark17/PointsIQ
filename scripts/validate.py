#!/usr/bin/env python3
"""Validate the vault: broken wikilinks, duplicate names, orphans, and a
node/edge census. Exits 1 if any wikilink is broken. Stdlib only."""

from __future__ import annotations

import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

VAULT = Path(__file__).resolve().parent.parent / "vault"

LINK_RE = re.compile(r"\[\[([^\]|#\n]+)(?:#[^\]|\n]*)?(?:\|[^\]\n]*)?\]\]")
TYPE_RE = re.compile(r"^type:\s*(\S+)", re.M)
ALIAS_BLOCK_RE = re.compile(r"^aliases:\n((?:- .*\n)+)", re.M)


def frontmatter(text: str) -> str:
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            return text[4:end + 1]
    return ""


def main():
    files = sorted(VAULT.rglob("*.md"))
    name_to_file: dict[str, list[Path]] = defaultdict(list)
    note_type: dict[Path, str] = {}
    texts: dict[Path, str] = {}

    for f in files:
        text = f.read_text(encoding="utf-8")
        texts[f] = text
        fm = frontmatter(text)
        m = TYPE_RE.search(fm)
        note_type[f] = m.group(1) if m else "untyped"
        name_to_file[f.stem.casefold()].append(f)
        am = ALIAS_BLOCK_RE.search(fm)
        if am:
            for line in am.group(1).strip().splitlines():
                alias = line[2:].strip().strip("'\"")
                if alias:
                    name_to_file[alias.casefold()].append(f)

    # duplicate canonical stems (aliases may legitimately collide — warn separately)
    dup_stems = {n: fs for n, fs in name_to_file.items()
                 if len({p for p in fs}) > 1 and any(p.stem.casefold() == n for p in fs)}

    broken: list[tuple[Path, str]] = []
    inbound: Counter = Counter()
    outbound: Counter = Counter()
    edge_pairs: Counter = Counter()
    total_edges = 0

    for f in files:
        for m in LINK_RE.finditer(texts[f]):
            # YAML single-quoted scalars escape ' as '' — undo before resolving
            target = m.group(1).strip().replace("''", "'")
            hit = name_to_file.get(target.casefold())
            if not hit:
                broken.append((f, target))
                continue
            total_edges += 1
            outbound[f] += 1
            inbound[hit[0]] += 1
            edge_pairs[(note_type[f], note_type[hit[0]])] += 1

    orphans = [f for f in files
               if inbound[f] == 0 and outbound[f] == 0 and note_type[f] != "airport"]

    # ── report ───────────────────────────────────────────────────────
    print("── Census ──")
    for t, n in sorted(Counter(note_type.values()).items(), key=lambda x: -x[1]):
        print(f"  {t:15} {n:>6}")
    print(f"  {'TOTAL NODES':15} {len(files):>6}")
    print(f"  {'TOTAL EDGES':15} {total_edges:>6}")

    print("\n── Top edge type-pairs ──")
    for (a, b), n in edge_pairs.most_common(15):
        print(f"  {a:14} → {b:14} {n:>6}")

    if dup_stems:
        print(f"\n⚠ {len(dup_stems)} duplicate note names:")
        for n, fs in list(dup_stems.items())[:10]:
            print(f"  {n}: {[str(p.relative_to(VAULT)) for p in set(fs)]}")

    if orphans:
        print(f"\n⚠ {len(orphans)} orphan notes (no links in or out):")
        for f in orphans[:10]:
            print(f"  {f.relative_to(VAULT)}")

    if broken:
        print(f"\n✗ {len(broken)} broken wikilinks:")
        for f, t in broken[:40]:
            print(f"  {f.relative_to(VAULT)} → [[{t}]]")
        sys.exit(1)

    print("\n✓ no broken wikilinks")


if __name__ == "__main__":
    main()
