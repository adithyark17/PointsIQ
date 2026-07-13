#!/usr/bin/env python3
"""Generate the curated (non-airport) vault notes from data/*.yaml."""

from __future__ import annotations

from lib import (
    DATA_DIR,
    VAULT_DIR,
    emit_note,
    load_yaml,
    prune_folder,
    safe_filename,
    wikilink,
)

emitted: set = set()


def emit(folder: str, name: str, frontmatter: dict, body: str = ""):
    path = VAULT_DIR / folder / f"{safe_filename(name)}.md"
    emit_note(path, frontmatter, body)
    emitted.add(path)
    return path


def links(names) -> list[str]:
    return [wikilink(n) for n in names]


def ratio_str(ratio) -> str:
    a, b = ratio
    fmt = lambda x: f"{x:g}"
    return f"{fmt(a)}:{fmt(b)}"


# ── banks ────────────────────────────────────────────────────────────
def gen_banks(data):
    for b in data["banks"]:
        fm = {"type": "bank", "tags": ["bank"], "country": wikilink(b["country"])}
        body = b.get("notes", "")
        body += (
            "\n\n## Cards\n\n```dataview\n"
            "TABLE currency, annual_fee_inr AS \"Fee ₹\", reward_rate_pct AS \"Rate %\", status\n"
            "FROM \"cards\" WHERE bank = this.file.link\nSORT annual_fee_inr DESC\n```\n"
        )
        emit("banks", b["name"], fm, body)


# ── currencies ───────────────────────────────────────────────────────
def gen_currencies(data):
    for c in data["currencies"]:
        fm = {"type": "currency", "tags": ["currency"]}
        if c.get("aliases"):
            fm["aliases"] = c["aliases"]
        if c.get("bank"):
            fm["bank"] = wikilink(c["bank"])
        if c.get("expiry"):
            fm["expiry"] = c["expiry"]
        if c.get("redemption_floor"):
            fm["redemption_floor"] = c["redemption_floor"]
        body = c.get("notes", "")
        body += (
            "\n\n## Transfer partners\n\n```dataview\n"
            "TABLE target AS \"To\", ratio, transfer_time, verified\n"
            "FROM \"transfers\" WHERE source = this.file.link\nSORT ratio ASC\n```\n"
            "\n## Earned by\n\n```dataview\n"
            "LIST FROM \"cards\" WHERE currency = this.file.link\n```\n"
        )
        emit("currencies", c["name"], fm, body)


# ── cards ────────────────────────────────────────────────────────────
def gen_cards(data):
    for c in data["cards"]:
        fm = {
            "type": "card",
            "tags": ["card"],
            "bank": wikilink(c["bank"]),
            "currency": wikilink(c["currency"]),
            "network": c.get("network", []),
        }
        if c.get("aliases"):
            fm["aliases"] = c["aliases"]
        for k in ("annual_fee_inr", "fee_waiver_spend_inr", "earn_unit",
                  "reward_rate_pct", "invite_only", "lounge_access", "status", "verified"):
            if c.get(k) is not None:
                fm[k] = c[k]
        if c.get("accelerated_earn"):
            fm["accelerated_earn"] = [
                {**a, "category": wikilink(a["category"]),
                 **({"via": wikilink(a["via"])} if a.get("via") else {})}
                for a in c["accelerated_earn"]
            ]
        if c.get("excluded_categories"):
            fm["excluded_categories"] = links(c["excluded_categories"])
        if c.get("milestones"):
            fm["milestones"] = c["milestones"]

        body = c.get("notes", "")
        if c.get("milestones"):
            body += "\n\n## Milestones\n\n| Spend (₹) | Period | Benefit |\n|---|---|---|\n"
            for m in c["milestones"]:
                body += f"| {m['spend_inr']:,} | {m.get('period', 'yearly')} | {m['benefit']} |\n"
        emit("cards", c["name"], fm, body)


# ── transfers ────────────────────────────────────────────────────────
def gen_transfers(data):
    for t in data["transfers"]:
        name = f"{t['from']} → {t['to']}"
        rs = ratio_str(t["ratio"])
        fm = {
            "type": "transfer",
            "tags": ["transfer"],
            "source": wikilink(t["from"]),
            "target": wikilink(t["to"]),
            "ratio": rs,
            "ratio_give": t["ratio"][0],
            "ratio_get": t["ratio"][1],
            "transfer_time": t.get("transfer_time", "unknown"),
            "verified": str(t.get("verified", "")),
        }
        body = f"**{t['from']}** transfers to **{t['to']}** at **{rs}**."
        if t.get("notes"):
            body += f"\n\n> {t['notes']}"
        emit("transfers", name, fm, body)


# ── programs ─────────────────────────────────────────────────────────
def gen_programs_air(data):
    for p in data["programs"]:
        fm = {"type": "air-program", "tags": ["program", "program/air"]}
        if p.get("aliases"):
            fm["aliases"] = p["aliases"]
        fm["airline"] = wikilink(p["airline"])
        if p.get("alliance"):
            fm["alliance"] = wikilink(p["alliance"])
        for k in ("currency_name", "pricing_model", "expiry", "fuel_surcharges", "status"):
            if p.get(k):
                fm[k] = p[k]
        if p.get("award_chart"):
            fm["award_chart"] = wikilink(p["award_chart"])
        body = p.get("notes", "")
        body += (
            "\n\n## Inbound transfer routes\n\n```dataview\n"
            "TABLE source AS \"From\", ratio, transfer_time, verified\n"
            "FROM \"transfers\" WHERE target = this.file.link\nSORT ratio ASC\n```\n"
        )
        emit("programs/air", p["name"], fm, body)


def gen_programs_hotel(data):
    for p in data["programs"]:
        fm = {"type": "hotel-program", "tags": ["program", "program/hotel"],
              "chain": p["chain"]}
        for k in ("currency_name", "pricing_model", "expiry", "status"):
            if p.get(k):
                fm[k] = p[k]
        body = p.get("notes", "")
        body += (
            "\n\n## Inbound transfer routes\n\n```dataview\n"
            "TABLE source AS \"From\", ratio, transfer_time, verified\n"
            "FROM \"transfers\" WHERE target = this.file.link\nSORT ratio ASC\n```\n"
            "\n## Outbound transfer routes\n\n```dataview\n"
            "TABLE target AS \"To\", ratio, transfer_time, verified\n"
            "FROM \"transfers\" WHERE source = this.file.link\nSORT ratio ASC\n```\n"
        )
        emit("programs/hotel", p["name"], fm, body)


# ── airlines & alliances ─────────────────────────────────────────────
def gen_airlines(data):
    for a in data["airlines"]:
        fm = {"type": "airline", "tags": ["airline"], "iata": a["iata"],
              "country": wikilink(a["country"])}
        if a.get("alliance"):
            fm["alliance"] = wikilink(a["alliance"])
        if a.get("program"):
            fm["program"] = wikilink(a["program"])
        if a.get("hubs"):
            fm["hubs"] = links(a["hubs"])
        if a.get("status"):
            fm["status"] = a["status"]
        emit("airlines", a["name"], fm, a.get("notes", ""))


def gen_alliances(data):
    for al in data["alliances"]:
        fm = {"type": "alliance", "tags": ["alliance"]}
        if al.get("founded"):
            fm["founded"] = al["founded"]
        body = al.get("notes", "")
        body += (
            "\n\n## Member airlines\n\n```dataview\n"
            "TABLE iata, program, country FROM \"airlines\" WHERE alliance = this.file.link\nSORT iata ASC\n```\n"
            "\n## Member programs\n\n```dataview\n"
            "TABLE airline, pricing_model, fuel_surcharges\n"
            "FROM \"programs/air\" WHERE alliance = this.file.link\n```\n"
        )
        emit("alliances", al["name"], fm, body)


# ── MCC categories ───────────────────────────────────────────────────
def gen_mcc(data):
    for m in data["categories"]:
        fm = {
            "type": "mcc-category",
            "tags": ["mcc"],
            "mcc_codes": [str(x) for x in m["mcc_codes"]],
            "typically_excluded": m.get("typically_excluded", False),
        }
        body = m.get("notes", "")
        body += "\n\n**Concept:** [[Merchant Category Code]]"
        body += (
            "\n\n## Cards that accelerate this category\n\n```dataview\n"
            "TABLE earn_unit, reward_rate_pct AS \"Base %\"\n"
            "FROM \"cards\" WHERE contains(string(accelerated_earn), this.file.name)\n```\n"
            "\n## Cards that exclude this category\n\n```dataview\n"
            "LIST FROM \"cards\" WHERE econtains(excluded_categories, this.file.link)\n```\n"
        )
        emit("mcc", m["name"], fm, body)


# ── portals ──────────────────────────────────────────────────────────
def gen_portals(data):
    for p in data["portals"]:
        fm = {"type": "portal", "tags": ["portal"], "bank": wikilink(p["bank"]),
              "kind": p.get("kind", "")}
        emit("portals", p["name"], fm, p.get("notes", ""))


# ── concepts ─────────────────────────────────────────────────────────
def gen_concepts(data):
    for c in data["concepts"]:
        fm = {"type": "concept", "tags": ["concept"]}
        if c.get("aliases"):
            fm["aliases"] = c["aliases"]
        body = c.get("summary", "")
        if c.get("links"):
            body += "\n\n**See also:** " + " · ".join(links(c["links"]))
        emit("concepts", c["name"], fm, body)


# ── award charts ─────────────────────────────────────────────────────
def gen_award_charts():
    for path in sorted((DATA_DIR / "award_charts").glob("*.yaml")):
        ch = load_yaml(path)
        fm = {
            "type": "award-chart",
            "tags": ["award-chart"],
            "program": wikilink(ch["program"]),
            "model": ch["model"],
            "last_verified": str(ch["last_verified"]),
        }
        body = f"> {ch['disclaimer']}\n"
        body += "\n## Pricing\n\n| Route | Economy | Business | First |\n|---|---|---|---|\n"
        for r in ch["rows"]:
            cell = lambda v: f"{v:,}" if v else "—"
            route = r["route"]
            if r.get("links"):
                route += " (" + ", ".join(links(r["links"])) + ")"
            body += f"| {route} | {cell(r.get('economy'))} | {cell(r.get('business'))} | {cell(r.get('first'))} |\n"
        for s in ch.get("sweet_spots", []):
            body += f"\n## Sweet spot: {s['title']}\n\n{s['body'].strip()}\n"
        emit("award-charts", ch["name"], fm, body)


def main():
    gen_alliances(load_yaml(DATA_DIR / "alliances.yaml"))
    gen_airlines(load_yaml(DATA_DIR / "airlines.yaml"))
    gen_programs_air(load_yaml(DATA_DIR / "programs_air.yaml"))
    gen_programs_hotel(load_yaml(DATA_DIR / "programs_hotel.yaml"))
    gen_banks(load_yaml(DATA_DIR / "banks.yaml"))
    gen_currencies(load_yaml(DATA_DIR / "currencies.yaml"))
    gen_cards(load_yaml(DATA_DIR / "cards.yaml"))
    gen_mcc(load_yaml(DATA_DIR / "mcc.yaml"))
    gen_portals(load_yaml(DATA_DIR / "portals.yaml"))
    gen_transfers(load_yaml(DATA_DIR / "transfers.yaml"))
    gen_concepts(load_yaml(DATA_DIR / "concepts.yaml"))
    gen_award_charts()

    removed = []
    for folder in ("banks", "cards", "currencies", "transfers", "portals",
                   "programs", "airlines", "alliances", "mcc", "award-charts", "concepts"):
        removed += prune_folder(VAULT_DIR / folder, emitted)

    print(f"emitted {len(emitted)} notes; pruned {len(removed)} stale notes")


if __name__ == "__main__":
    main()
