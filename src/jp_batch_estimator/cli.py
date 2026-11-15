"""Command-line interface for the batch estimator."""
from __future__ import annotations
import argparse
import csv
import json
from pathlib import Path

from . import geometry, interior, lumber, concrete


def _num(row, key, default=None):
    v = row.get(key, "")
    if v is None or str(v).strip() == "":
        return default
    return float(v)


def estimate_row(row: dict) -> dict:
    out = {"room_id": row.get("room_id", ""), "warnings": []}
    try:
        area = geometry.area_m2(
            row.get("shape"),
            length_m=_num(row, "length_m"), width_m=_num(row, "width_m"),
            height_m=_num(row, "height_m"), base_m=_num(row, "base_m"),
            diameter_m=_num(row, "diameter_m"))
        out["area_m2"] = round(area, 4)
        out["area_tsubo"] = round(geometry.to_tsubo(area), 4)
    except Exception as exc:
        out["warnings"].append(f"area: {exc}")

    if all(_num(row, k) is not None for k in ("tile_width_mm", "tile_length_mm")):
        try:
            out["tile_count"] = interior.tile_count(
                out.get("area_m2", 0.0), _num(row, "tile_width_mm"),
                _num(row, "tile_length_mm"), _num(row, "joint_width_mm", 0.0) or 0.0,
                _num(row, "waste_pct", 0.0) or 0.0)
        except Exception as exc:
            out["warnings"].append(f"tile: {exc}")

    if all(_num(row, k) is not None for k in ("room_width_m", "room_length_m",
                                              "board_width_mm", "board_length_mm")):
        try:
            out["flooring_pieces"] = interior.flooring_pieces(
                _num(row, "room_width_m"), _num(row, "room_length_m"),
                _num(row, "board_width_mm"), _num(row, "board_length_mm"))
        except Exception as exc:
            out["warnings"].append(f"flooring: {exc}")

    if all(_num(row, k) is not None for k in ("wall_perimeter_m", "wall_height_m",
                                              "roll_width_cm", "roll_length_m")):
        try:
            out["wallpaper_rolls"] = interior.wallpaper_rolls(
                _num(row, "wall_perimeter_m"), _num(row, "wall_height_m"),
                _num(row, "roll_width_cm"), _num(row, "roll_length_m"))
        except Exception as exc:
            out["warnings"].append(f"wallpaper: {exc}")

    if out.get("area_m2") is None and _num(row, "length_m") and _num(row, "width_m")             and _num(row, "thickness_mm") is not None:
        try:
            out["concrete_volume_m3"] = round(concrete.concrete_volume_m3(
                _num(row, "length_m"), _num(row, "width_m"),
                _num(row, "thickness_mm")), 4)
        except Exception as exc:
            out["warnings"].append(f"concrete: {exc}")

    if _num(row, "mortar_thickness_mm") is not None and out.get("area_m2"):
        try:
            out["mortar_volume_m3"] = round(interior.mortar_volume_m3(
                out["area_m2"], _num(row, "mortar_thickness_mm")), 4)
        except Exception as exc:
            out["warnings"].append(f"mortar: {exc}")

    if row.get("species") and _num(row, "volume_m3") is not None:
        try:
            mass, note = lumber.lumber_mass_kg(
                _num(row, "volume_m3"), row["species"],
                count=_num(row, "count", 1.0) or 1.0,
                moisture=row.get("moisture_condition", "air_dry"))
            out["lumber_mass_kg"] = mass
            if note:
                out["warnings"].append(note)
        except Exception as exc:
            out["warnings"].append(f"lumber: {exc}")
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description="Offline batch estimator for Japanese DIY / renovation.")
    ap.add_argument("--input", required=True, help="input CSV file")
    ap.add_argument("--output", help="output file (CSV or JSON)")
    ap.add_argument("--format", choices=["csv", "json"], default="csv")
    args = ap.parse_args(argv)

    with open(args.input, "r", encoding="utf-8-sig", newline="") as fh:
        rows = list(csv.DictReader(fh))
    results = [estimate_row(r) for r in rows]

    if args.output:
        out_path = Path(args.output)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        if args.format == "json":
            out_path.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
        else:
            fields = sorted({k for r in results for k in r if k != "warnings"})
            with open(out_path, "w", encoding="utf-8-sig", newline="") as fh:
                w = csv.DictWriter(fh, fieldnames=["room_id"] + fields + ["warnings"])
                w.writeheader()
                for r in results:
                    rr = {k: r.get(k, "") for k in ["room_id"] + fields}
                    rr["warnings"] = "; ".join(r["warnings"])
                    w.writerow(rr)
    else:
        print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
