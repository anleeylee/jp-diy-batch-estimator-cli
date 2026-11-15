import unittest
from jp_batch_estimator import geometry


class TestGeometry(unittest.TestCase):
    def test_tsubo_constant(self):
        self.assertAlmostEqual(geometry.to_tsubo(3.305785123966942), 1.0, places=6)

    def test_rectangle(self):
        self.assertAlmostEqual(geometry.area_m2("rectangle", length_m=4, width_m=3), 12.0)

    def test_trapezoid(self):
        self.assertAlmostEqual(geometry.area_m2("trapezoid", length_m=2, width_m=4, height_m=3), 9.0)


if __name__ == "__main__":
    unittest.main()
