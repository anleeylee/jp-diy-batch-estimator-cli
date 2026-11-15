"""Area and tsubo conversions.

Statutory constants follow the Measurement Act Enforcement Act
(計量法施行法 第四条): 1 shaku = 10/33 m, 1 tsubo = 400/121 m2.
"""
from __future__ import annotations
import math

TSUBO_PER_SQM = 121.0 / 400.0  # 1 m2 in tsubo
SQM_PER_TSUBO = 400.0 / 121.0


def area_m2(shape, length_m=None, width_m=None, height_m=None,
            base_m=None, diameter_m=None):
    shape = (shape or "rectangle").strip().lower()
    if shape in ("rectangle", "rect", "矩形", "長方形"):
        if length_m is None or width_m is None:
            raise ValueError("length_m and width_m are required for a rectangle")
        return length_m * width_m
    if shape in ("triangle", "三角"):
        if base_m is None or height_m is None:
            raise ValueError("base_m and height_m are required for a triangle")
        return base_m * height_m / 2.0
    if shape in ("circle", "円", "円形"):
        if diameter_m is None:
            raise ValueError("diameter_m is required for a circle")
        return math.pi * (diameter_m / 2.0) ** 2
    if shape in ("trapezoid", "台形"):
        if length_m is None or width_m is None or height_m is None:
            raise ValueError("length_m, width_m and height_m are required for a trapezoid")
        return (length_m + width_m) * height_m / 2.0
    raise ValueError(f"unknown shape: {shape}")


def to_tsubo(area_m2: float) -> float:
    return area_m2 * TSUBO_PER_SQM


def to_sqm(tsubo: float) -> float:
    return tsubo * SQM_PER_TSUBO
