"""Interior finish quantities: tile, flooring, wallpaper, mortar."""
from __future__ import annotations
import math


def tile_count(area_m2, tile_w_mm, tile_l_mm, joint_mm=0.0, waste_pct=0.0):
    """Tiles needed with joint-inclusive pitch and cut allowance.

    Pitch = tile size + joint width; pieces are rounded up per the start layout.
    """
    pitch_w = (tile_w_mm + joint_mm) / 1000.0
    pitch_l = (tile_l_mm + joint_mm) / 1000.0
    effective = pitch_w * pitch_l
    if effective <= 0:
        raise ValueError("tile dimensions and joint must produce a positive effective area")
    count = area_m2 / effective
    return math.ceil(count * (1.0 + waste_pct / 100.0))


def flooring_pieces(room_w_m, room_l_m, board_w_mm, board_l_mm):
    """Boards/strips needed; one partial allowance per strip at the end of the row."""
    bw = board_w_mm / 1000.0
    bl = board_l_mm / 1000.0
    if bw <= 0 or bl <= 0:
        raise ValueError("board dimensions must be positive")
    strips = math.ceil(room_w_m / bw)
    full = math.floor(room_l_m / bl)
    pieces = strips * full + strips
    by_area = math.ceil((room_w_m * room_l_m) / (bw * bl))
    return max(pieces, by_area)


def wallpaper_rolls(perimeter_m, wall_height_m, roll_width_cm, roll_length_m):
    """Rolls of wallpaper needed; strips per roll = floor(roll length / wall height)."""
    strip_w = roll_width_cm / 100.0
    if strip_w <= 0 or wall_height_m <= 0 or roll_length_m <= 0:
        raise ValueError("wallpaper dimensions must be positive")
    strips_needed = math.ceil(perimeter_m / strip_w)
    strips_per_roll = math.floor(roll_length_m / wall_height_m)
    if strips_per_roll <= 0:
        raise ValueError("roll length must cover at least one wall height")
    return math.ceil(strips_needed / strips_per_roll)


def mortar_volume_m3(area_m2, thickness_mm):
    return area_m2 * thickness_mm / 1000.0
