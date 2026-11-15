"""Concrete / mortar volume from plan dimensions."""
from __future__ import annotations


def concrete_volume_m3(length_m, width_m, thickness_mm):
    if length_m <= 0 or width_m <= 0 or thickness_mm <= 0:
        raise ValueError("dimensions must be positive")
    return length_m * width_m * thickness_mm / 1000.0
