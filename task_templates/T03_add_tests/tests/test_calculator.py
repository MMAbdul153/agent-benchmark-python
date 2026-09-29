# tests/test_calculator.py
import unittest
from src.calculator import add, apply_discount, average

class TestDiscount(unittest.TestCase):
    def test_valid_discount(self):
        self.assertEqual(apply_discount(100.0, 10.0), 90.0)

    def test_rounding(self):
        self.assertEqual(apply_discount(99.99, 25.0), 74.99)

    def test_negative_price_raises(self):
        with self.assertRaises(ValueError):
            apply_discount(-10.0, 10.0)

    def test_discount_over_100_raises(self):
        with self.assertRaises(ValueError):
            apply_discount(100.0, 150.0)

    def test_negative_discount_raises(self):
        with self.assertRaises(ValueError):
            apply_discount(100.0, -5.0)

class TestAverage(unittest.TestCase):
    def test_average_non_empty(self):
        self.assertAlmostEqual(average([1, 2, 3, 4]), 2.5)

    def test_average_single_element(self):
        self.assertAlmostEqual(average([10]), 10.0)

    def test_empty_list_raises(self):
        with self.assertRaises(ValueError):
            average([])


if __name__ == "__main__":
    unittest.main()
