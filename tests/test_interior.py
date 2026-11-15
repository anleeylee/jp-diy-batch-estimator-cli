import unittest
from jp_batch_estimator import interior


class TestInterior(unittest.TestCase):
    def test_tile_with_joint(self):
        # 300mm tile + 3mm joint, 12 m2 room
        n = interior.tile_count(12.0, 300, 300, joint_mm=3.0, waste_pct=5.0)
        self.assertGreater(n, 0)

    def test_wallpaper_rolls(self):
        rolls = interior.wallpaper_rolls(perimeter_m=14.0, wall_height_m=2.6,
                                        roll_width_cm=92, roll_length_m=50.0)
        self.assertEqual(rolls, 1)


if __name__ == "__main__":
    unittest.main()
