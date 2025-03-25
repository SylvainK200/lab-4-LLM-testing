import unittest

class TestClosestInteger(unittest.TestCase):
    def test_exact_integers(self):
        self.assertEqual(closest_integer("10"), 10)
        self.assertEqual(closest_integer("-10"), -10)
        self.assertEqual(closest_integer("0"), 0)

    def test_trailing_zeros(self):
        self.assertEqual(closest_integer("10.0"), 10)
        self.assertEqual(closest_integer("-10.0"), -10)
        self.assertEqual(closest_integer("0.0"), 0)

    def test_positive_numbers(self):
        self.assertEqual(closest_integer("10.5"), 11)
        self.assertEqual(closest_integer("10.6"), 11)
        self.assertEqual(closest_integer("10.4"), 10)
        self.assertEqual(closest_integer("10.1"), 10)
        self.assertEqual(closest_integer("10.9"), 11)

    def test_negative_numbers(self):
        self.assertEqual(closest_integer("-10.5"), -11)
        self.assertEqual(closest_integer("-10.6"), -11)
        self.assertEqual(closest_integer("-10.4"), -10)
        self.assertEqual(closest_integer("-10.1"), -10)
        self.assertEqual(closest_integer("-10.9"), -11)

    def test_equidistant_numbers(self):
        self.assertEqual(closest_integer("14.5"), 15)
        self.assertEqual(closest_integer("-14.5"), -15)

    def test_zero_point_five(self):
        self.assertEqual(closest_integer("0.5"), 1)
        self.assertEqual(closest_integer("-0.5"), -1)

    def test_empty_string(self):
        with self.assertRaises(ValueError):
            closest_integer("")

    def test_non_numeric_string(self):
        with self.assertRaises(ValueError):
            closest_integer("hello")

if __name__ == '__main__':
    unittest.main()