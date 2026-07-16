#!/usr/bin/env python3
"""PointsIQ advisor — answers wallet questions using the knowledge base in data/.

    python3 pointsiq.py balances
    python3 pointsiq.py swipe dining --amount 5000
    python3 pointsiq.py route --to singapore --cabin business
    python3 pointsiq.py sweetspots

Reads your wallet from wallet.yaml (copy wallet.example.yaml). All numbers come
from data/*.yaml — the same source of truth as the vault; ratios drift, check
`verified` dates before moving points.
"""

from __future__ import annotations

import argparse
import math
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
WIKI = re.compile(r"\[\[([^\]|]+?)(?:\|[^\]]*)?\]\]")


def load(name):
    with open(DATA / name, encoding="utf-8") as f:
        return yaml.safe_load(f)


def strip_links(s: str) -> str:
    return WIKI.sub(lambda m: m.group(1), s)


def load_wallet():
    for candidate in (ROOT / "wallet.yaml", ROOT / "wallet.example.yaml"):
        if candidate.exists():
            with open(candidate, encoding="utf-8") as f:
                w = yaml.safe_load(f) or {}
            w["_file"] = candidate.name
            w.setdefault("cards", [])
            w.setdefault("balances", {})
            w.setdefault("programs", {})
            return w
    sys.exit("no wallet.yaml or wallet.example.yaml found")


# ── transfer graph ───────────────────────────────────────────────────
def transfer_graph():
    """currency/program → list of (target, give, get, route_desc)."""
    g: dict[str, list] = {}
    for t in load("transfers.yaml")["transfers"]:
        give, get = t["ratio"]
        g.setdefault(t["from"], []).append(
            (t["to"], give, get, f"{t['from']} → {t['to']} ({give:g}:{get:g})"))
    return g


def best_paths(sources: dict[str, float], graph, max_hops=3):
    """For every reachable node: the best (highest miles-per-point) path from any
    wallet source. Returns node → (source, cum_ratio, [route_desc,...])."""
    best: dict[str, tuple] = {}
    frontier = [(src, src, 1.0, []) for src in sources]
    while frontier:
        nxt = []
        for src, node, ratio, path in frontier:
            if len(path) >= max_hops:
                continue
            for to, give, get, desc in graph.get(node, []):
                r = ratio * (get / give)
                if to in sources:      # don't route through another wallet balance
                    continue
                cur = best.get(to)
                if cur is None or r > cur[1]:
                    best[to] = (src, r, path + [desc])
                    nxt.append((src, to, r, path + [desc]))
        frontier = nxt
    return best


# ── swipe ────────────────────────────────────────────────────────────
def card_value(card, category):
    """(effective %, note) for spending in `category` on `card`."""
    if category in (card.get("excluded_categories") or []):
        return 0.0, "excluded — earns nothing"
    base = card.get("reward_rate_pct") or 0.0
    best, note = base, f"base earn ({card.get('earn_unit', '')})".strip()
    for a in card.get("accelerated_earn") or []:
        if a["category"] == category:
            rate = base * a.get("multiplier", 1)
            if rate > best:
                best = rate
                via = f" via {a['via']}" if a.get("via") else ""
                best_note = f"{a.get('multiplier')}x accelerated{via}"
                if a.get("note"):
                    best_note += f" — {a['note']}"
                note = best_note
    return best, note


def cmd_swipe(args):
    wallet = load_wallet()
    cards = {c["name"]: c for c in load("cards.yaml")["cards"]}
    cats = [c["name"] for c in load("mcc.yaml")["categories"]]
    matches = [c for c in cats if args.category.lower() in c.lower()]
    if not matches:
        sys.exit(f"no MCC category matches '{args.category}' — options: {', '.join(cats)}")
    if len(matches) > 1:
        sys.exit(f"'{args.category}' is ambiguous: {', '.join(matches)}")
    cat = matches[0]
    amount = args.amount

    rows = []
    for name, card in cards.items():
        pct, note = card_value(card, cat)
        rows.append((pct, name in wallet["cards"], name, note))
    rows.sort(key=lambda r: (-r[0], not r[1]))

    print(f"Category: {cat}   spend: ₹{amount:,}   (≈ value at effective reward rate)\n")
    print("YOUR CARDS")
    yours = [r for r in rows if r[1]]
    if not yours:
        print(f"  none in wallet ({wallet['_file']})")
    for pct, _, name, note in yours:
        print(f"  {'✓' if pct > 0 else '✗'} {name:34} {pct:5.2f}%  ≈ ₹{amount * pct / 100:8,.0f}  {note}")
    print("\nMARKET BEST (cards you don't hold marked ·)")
    for pct, held, name, note in rows[:5]:
        mark = "✓" if held else "·"
        print(f"  {mark} {name:34} {pct:5.2f}%  ≈ ₹{amount * pct / 100:8,.0f}  {note}")


# ── route ────────────────────────────────────────────────────────────
def flight_rows(dest: str):
    """(chart, row) pairs whose route or links mention dest."""
    out = []
    for f in sorted((DATA / "award_charts").glob("*.yaml")):
        ch = yaml.safe_load(open(f, encoding="utf-8"))
        for row in ch.get("rows", []):
            hay = row["route"].lower() + " " + " ".join(str(x).lower() for x in row.get("links", []))
            if dest.lower() in hay:
                out.append((ch, row))
    return out


def cmd_route(args):
    wallet = load_wallet()
    cabin = args.cabin
    sources = dict(wallet["balances"])
    prog_bal = dict(wallet["programs"])
    graph = transfer_graph()
    paths = best_paths(sources, graph)

    rows = flight_rows(args.to)
    rows = [(ch, r) for ch, r in rows if r.get(cabin)]
    if not rows:
        sys.exit(f"no award-chart rows match '{args.to}' with a {cabin} price — try a country, city or IATA code")

    print(f"Destination: '{args.to}'   cabin: {cabin}   wallet: {wallet['_file']}\n")
    options = []
    for ch, row in rows:
        prog = ch["program"]
        miles = row[cabin]
        # direct program balance
        have_direct = prog_bal.get(prog, 0)
        if have_direct >= miles:
            options.append((0, miles, prog, ch, row, f"already in {prog}", True))
            continue
        hit = paths.get(prog)
        if not hit:
            continue
        src, ratio, path = hit
        needed = math.ceil((miles - have_direct) / ratio)
        feasible = sources.get(src, 0) >= needed
        via = "  →  ".join(path)
        note = f"transfer {needed:,} {src}  [{via}]"
        if have_direct:
            note += f"  (+{have_direct:,} already in {prog})"
        options.append((needed if feasible else needed * 1000, miles, prog, ch, row, note, feasible))

    if not options:
        sys.exit("no transfer path from your wallet reaches any matching program")
    options.sort(key=lambda o: o[0])
    for _, miles, prog, ch, row, note, feasible in options[:8]:
        flag = "✓" if feasible else "✗ short"
        print(f"{flag}  {row['route']}  ·  {prog}")
        print(f"    {miles:,} miles {cabin}  ·  {note}")
        print(f"    chart: {ch['name']} (verified {ch['last_verified']}) — {ch['disclaimer'][:70]}…\n")
    print("caps, transfer bonuses and seat availability not modelled — charts are theoretical pricing.")


# ── sweetspots ───────────────────────────────────────────────────────
def cmd_sweetspots(args):
    wallet = load_wallet()
    paths = best_paths(dict(wallet["balances"]), transfer_graph())
    prog_bal = wallet["programs"]
    for f in sorted((DATA / "award_charts").glob("*.yaml")):
        ch = yaml.safe_load(open(f, encoding="utf-8"))
        prog = ch["program"]
        reach = prog in paths or prog in prog_bal
        for s in ch.get("sweet_spots", []):
            mark = "✓ reachable" if reach else "· out of reach"
            print(f"[{mark}] {s['title']}  ({prog})")
            print("    " + strip_links(s["body"]).strip().replace("\n", "\n    ") + "\n")


# ── balances ─────────────────────────────────────────────────────────
def cmd_balances(args):
    wallet = load_wallet()
    paths = best_paths(dict(wallet["balances"]), transfer_graph())
    print(f"wallet: {wallet['_file']}\n\nCards: " + (", ".join(wallet["cards"]) or "—"))
    print("\nBalances:")
    for cur, amt in wallet["balances"].items():
        print(f"  {cur:44} {amt:>10,}")
    for prog, amt in wallet["programs"].items():
        print(f"  {prog:44} {amt:>10,}  (in program)")
    reachable = sorted(paths.items(), key=lambda kv: -kv[1][1])
    print(f"\nReachable programs from these balances: {len(reachable)}")
    for prog, (src, ratio, path) in reachable[:12]:
        print(f"  {prog:44} best {ratio:g} miles/pt from {src} ({len(path)} hop{'s' if len(path)>1 else ''})")


def main():
    ap = argparse.ArgumentParser(prog="pointsiq", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("swipe", help="best card for a spend category")
    s.add_argument("category")
    s.add_argument("--amount", type=int, default=10000, help="spend in ₹ (default 10,000)")
    s.set_defaults(fn=cmd_swipe)
    r = sub.add_parser("route", help="best way to move your points for a trip")
    r.add_argument("--to", required=True, help="destination keyword: country, city or IATA")
    r.add_argument("--cabin", default="business", choices=["economy", "business", "first"])
    r.set_defaults(fn=cmd_route)
    sub.add_parser("sweetspots", help="chart sweet spots, flagged by reachability").set_defaults(fn=cmd_sweetspots)
    sub.add_parser("balances", help="wallet summary + reachable programs").set_defaults(fn=cmd_balances)
    args = ap.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
