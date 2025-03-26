import unittest

def closest_integer(value):
    '''
    Create a function that takes a value (string) representing a number
    and returns the closest integer to it. If the number is equidistant
    from two integers, round it away from zero.
    Note:
    Rounding away from zero means that if the given number is equidistant
    from two integers, the one you should return is the one that is the
    farthest from zero. For example closest_integer("14.5") should
    return 15 and closest_integer("-14.5") should return -15.
    '''
    from math import floor, ceil

    if value.count('.') == 1:
        # remove trailing zeros
        while (value[-1] == '0'):
            value = value[:-1]

    num = float(value)
    if value[-2:] == '.5':
        if num > 0:
            res = ceil(num)
        else:
            res = floor(num)
    elif len(value) > 0:
        res = int(round(num))
    else:
        res = 0

    return res

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

# if __name__ == '__main__':
#     unittest.main()