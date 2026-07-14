#!/usr/bin/env python3
"""Re-embed fresh vault graph data into explorer/graph.html.

Extracts the curated core (every non-geo node type) plus the airports/countries
they reference, and replaces the JSON payload inside the self-contained explorer
page. Run after regenerating the vault:

    python3 scripts/export_graph.py
"""

from __future__ import annotations

import json
import re

from lib import REPO_ROOT, VAULT_DIR, load_yaml  # noqa: F401  (lib gives us paths)
import yaml

LINK_RE = re.compile(r"\[\[([^\]|#\n]+)(?:#[^\]|\n]*)?(?:\|[^\]\n]*)?\]\]")
CORE_TYPES = {"bank", "card", "currency", "transfer", "portal", "air-program",
              "hotel-program", "airline", "alliance", "mcc-category", "award-chart",
              "concept", "stopover-program", "home"}

DETAIL_KEYS = {
    "card": ["bank", "currency", "annual_fee_inr", "fee_waiver_spend_inr", "earn_unit",
             "reward_rate_pct", "status", "verified"],
    "transfer": ["source", "target", "ratio", "transfer_time", "group", "verified"],
    "currency": ["bank", "expiry", "redemption_floor"],
    "air-program": ["airline", "alliance", "currency_name", "pricing_model", "expiry", "fuel_surcharges"],
    "hotel-program": ["chain", "currency_name", "pricing_model", "expiry"],
    "airline": ["iata", "country", "alliance", "program", "status"],
    "alliance": ["founded"],
    "bank": ["country"],
    "mcc-category": ["mcc_codes", "typically_excluded"],
    "portal": ["bank", "kind"],
    "award-chart": ["program", "model", "last_verified"],
    "stopover-program": ["airline", "hub", "kind", "min_layover", "max_stay", "cost", "verified"],
    "airport": ["iata", "name", "municipality", "country", "size"],
    "country": ["iso2", "region"],
    "region": ["code"],
}


def parse(text):
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text
    try:
        fm = yaml.safe_load(text[4:end + 1]) or {}
    except yaml.YAMLError:
        fm = {}
    return fm, text[end + 5:]


def clean(v):
    if isinstance(v, list):
        return ", ".join(str(x).strip("[]") for x in v)
    return str(v).replace("[[", "").replace("]]", "")


def main():
    notes = {}
    for f in VAULT_DIR.rglob("*.md"):
        text = f.read_text(encoding="utf-8")
        fm, _ = parse(text)
        notes[f.stem] = {"type": fm.get("type", "untyped"), "fm": fm, "text": text}

    alias_map = {}
    for name, n in notes.items():
        for a in (n["fm"].get("aliases") or []):
            alias_map.setdefault(str(a), name)

    def resolve(t):
        t = t.strip().replace("''", "'")
        return t if t in notes else alias_map.get(t)

    core = {n for n, d in notes.items() if d["type"] in CORE_TYPES}
    extra, edges = set(), set()
    for name in core:
        for m in LINK_RE.finditer(notes[name]["text"]):
            tgt = resolve(m.group(1))
            if not tgt or tgt == name:
                continue
            if tgt in core:
                edges.add((name, tgt))
            elif notes[tgt]["type"] in ("airport", "country", "region"):
                extra.add(tgt)
                edges.add((name, tgt))
    for name in extra:
        for m in LINK_RE.finditer(notes[name]["text"]):
            tgt = resolve(m.group(1))
            if tgt and tgt != name and (tgt in core or tgt in extra):
                edges.add((name, tgt))

    out_nodes = []
    for name in sorted(core | extra):
        d = notes[name]
        det = {k: clean(d["fm"][k]) for k in DETAIL_KEYS.get(d["type"], []) if d["fm"].get(k) is not None}
        out_nodes.append({"id": name, "t": d["type"], "d": det})
    idx = {n["id"]: i for i, n in enumerate(out_nodes)}
    out_edges = sorted([idx[a], idx[b]] for a, b in edges)

    data = {"nodes": out_nodes, "edges": out_edges}
    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":"))

    page = REPO_ROOT / "explorer" / "graph.html"
    html = page.read_text(encoding="utf-8")
    html = re.sub(
        r'(<script type="application/json" id="data">).*?(</script>)',
        lambda m: m.group(1) + payload + m.group(2),
        html, count=1, flags=re.S,
    )
    page.write_text(html, encoding="utf-8")
    print(f"explorer/graph.html: {len(out_nodes)} nodes, {len(out_edges)} edges embedded")


if __name__ == "__main__":
    main()
