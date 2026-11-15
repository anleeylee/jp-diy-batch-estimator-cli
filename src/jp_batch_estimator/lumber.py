"""Lumber weight using verified air-dry densities by species.

Densities are the Japan Forestry Agency / J-Credit species table
(air-dry, moisture ~20%). Structural strength and moisture reduction
are NOT considered; do not use for structural design.
"""
from __future__ import annotations

WOOD_AIR_DRY_DENSITY = {
    "sugi": {"ja": "スギ", "density": 0.38},
    "hinoki": {"ja": "ヒノキ", "density": 0.44},
    "sawara": {"ja": "サワラ", "density": 0.34},
    "momi": {"ja": "モミ", "density": 0.44},
    "todomatsu": {"ja": "トドマツ", "density": 0.40},
    "karamatsu": {"ja": "カラマツ", "density": 0.50},
    "ezomatsu": {"ja": "エゾマツ", "density": 0.43},
    "akamatsu": {"ja": "アカマツ", "density": 0.52},
    "kuromatsu": {"ja": "クロマツ", "density": 0.54},
    "hiba": {"ja": "ヒバ", "density": 0.45},
    "todoroki": {"ja": "トドノキ", "density": 0.50},
    "kiri": {"ja": "キリ", "density": 0.30},
    "katsura": {"ja": "カツラ", "density": 0.50},
    "kuri": {"ja": "クリ", "density": 0.60},
    "kaki": {"ja": "カキ", "density": 0.69},
    "akashide": {"ja": "アカシデ", "density": 0.73},
    "buna": {"ja": "ブナ", "density": 0.69},
    "koono": {"ja": "ブナ（クーノノ）", "density": 0.65},
    "konara": {"ja": "コナラ", "density": 0.79},
}


def lumber_mass_kg(volume_m3, species, count=1, moisture="air_dry"):
    if species not in WOOD_AIR_DRY_DENSITY:
        raise ValueError(f"unknown species: {species}")
    density = WOOD_AIR_DRY_DENSITY[species]["density"]
    note = ""
    if moisture == "oven_dry":
        density = density / 0.87
        note = "oven-dry converted with a 0.87 factor (carbon accounting coefficient, not a strict dry-density definition)"
    elif moisture == "green":
        note = "green (unseasoned) wood density fluctuates widely; air-dry table applied with caution"
    mass = volume_m3 * density * 1000.0 * count
    return round(mass, 2), note
