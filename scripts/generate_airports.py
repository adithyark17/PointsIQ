#!/usr/bin/env python3
"""Generate airport + country + region notes from the OurAirports dataset.

Usage:
    python3 scripts/generate_airports.py --fetch   # download CSVs first
    python3 scripts/generate_airports.py           # use data/cache/*.csv
"""

from __future__ import annotations

import csv
import sys
import urllib.request

from lib import DATA_DIR, VAULT_DIR, emit_note, load_yaml, prune_folder, wikilink

# github mirror of https://ourairports.com/data/ (the primary host is not
# reachable through every proxy; the mirror carries identical files)
BASE = "https://raw.githubusercontent.com/davidmegginson/ourairports-data/main"
CACHE = DATA_DIR / "cache"

CONTINENTS = {
    "AF": "Africa", "AN": "Antarctica", "AS": "Asia", "EU": "Europe",
    "NA": "North America", "OC": "Oceania", "SA": "South America",
}

SIZE_TAG = {"large_airport": "airport/large", "medium_airport": "airport/medium"}


def fetch():
    CACHE.mkdir(parents=True, exist_ok=True)
    for f in ("airports.csv", "countries.csv"):
        print(f"fetching {f} ...")
        urllib.request.urlretrieve(f"{BASE}/{f}", CACHE / f)


def read_csv(name):
    with open(CACHE / name, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def keep(row) -> bool:
    if row["type"] == "closed":
        return False
    return row["type"] in ("large_airport", "medium_airport") or row["scheduled_service"] == "yes"


def hub_overlay() -> dict[str, list[str]]:
    """IATA code → airlines hubbed there, from the curated airlines dataset."""
    hubs: dict[str, list[str]] = {}
    for a in load_yaml(DATA_DIR / "airlines.yaml")["airlines"]:
        for h in a.get("hubs", []):
            hubs.setdefault(h, []).append(a["name"])
    return hubs


def main():
    if "--fetch" in sys.argv:
        fetch()
    if not (CACHE / "airports.csv").exists():
        sys.exit("data/cache/airports.csv missing — run with --fetch")

    countries = {c["code"]: c for c in read_csv("countries.csv")}
    hubs = hub_overlay()
    rows = [r for r in read_csv("airports.csv") if keep(r)]

    emitted: set = set()
    used_names: set[str] = set()
    seen_countries: dict[str, str] = {}  # iso2 → continent code
    skipped = 0

    for r in sorted(rows, key=lambda r: (r["type"] != "large_airport", r["ident"])):
        name = r["iata_code"] or r["ident"]
        if name in used_names:
            name = r["ident"]
            if name in used_names:
                skipped += 1
                continue
        used_names.add(name)

        iso2 = r["iso_country"]
        country = countries.get(iso2)
        country_name = country["name"] if country else iso2
        continent = r["continent"] or (country["continent"] if country else "")
        region_name = CONTINENTS.get(continent, "Unknown")
        seen_countries[iso2] = continent

        fm = {
            "type": "airport",
            "tags": ["airport", SIZE_TAG.get(r["type"], "airport/small")],
            "name": r["name"],
        }
        if r["iata_code"]:
            fm["iata"] = r["iata_code"]
        if r.get("icao_code") or r["ident"]:
            fm["icao"] = r.get("icao_code") or r["ident"]
        if r["name"] != name:
            fm["aliases"] = [r["name"]]
        fm["country"] = wikilink(country_name)
        fm["region"] = wikilink(region_name)
        if r["municipality"]:
            fm["municipality"] = r["municipality"]
        fm["size"] = r["type"]
        fm["scheduled_service"] = r["scheduled_service"] == "yes"
        try:
            fm["lat"] = round(float(r["latitude_deg"]), 4)
            fm["lon"] = round(float(r["longitude_deg"]), 4)
        except ValueError:
            pass
        if r["iata_code"] and r["iata_code"] in hubs:
            fm["hub_for"] = [wikilink(a) for a in hubs[r["iata_code"]]]

        body = f"{r['name']}" + (f" — {r['municipality']}," if r["municipality"] else " —") + f" {country_name}."
        path = VAULT_DIR / "airports" / iso2 / f"{name}.md"
        emit_note(path, fm, body)
        emitted.add(path)

    # ── country notes ────────────────────────────────────────────────
    country_names = {countries[i]["name"] for i in seen_countries if i in countries}
    for iso2, continent in sorted(seen_countries.items()):
        country = countries.get(iso2)
        if not country:
            continue
        fm = {
            "type": "country",
            "tags": ["geo", "geo/country"],
            "iso2": iso2,
        }
        region_name = CONTINENTS.get(continent, "Unknown")
        if region_name != country["name"]:  # Antarctica is both country and region
            fm["region"] = wikilink(region_name)
        body = (
            "## Airports\n\n```dataview\n"
            f"TABLE iata, name, municipality, size FROM \"airports/{iso2}\"\n"
            "SORT size ASC, iata ASC\nLIMIT 400\n```\n"
        )
        path = VAULT_DIR / "geo" / "countries" / f"{country['name']}.md"
        emit_note(path, fm, body)
        emitted.add(path)

    # ── region notes (skip names already taken by a country note) ────
    for code, rname in CONTINENTS.items():
        if rname in country_names:
            continue
        fm = {"type": "region", "tags": ["geo", "geo/region"], "code": code}
        body = (
            "## Countries\n\n```dataview\n"
            "LIST FROM \"geo/countries\" WHERE region = this.file.link\n```\n"
        )
        path = VAULT_DIR / "geo" / "regions" / f"{rname}.md"
        emit_note(path, fm, body)
        emitted.add(path)

    removed = prune_folder(VAULT_DIR / "airports", emitted)
    removed += prune_folder(VAULT_DIR / "geo", emitted)

    n_airports = sum(1 for p in emitted if "airports" in p.parts)
    print(f"airports: {n_airports} · countries: {len(seen_countries)} · "
          f"skipped dupes: {skipped} · pruned: {len(removed)}")


if __name__ == "__main__":
    main()
