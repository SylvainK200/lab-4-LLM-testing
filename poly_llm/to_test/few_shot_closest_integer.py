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

class TestClosestIntegerFunction(unittest.TestCase):

    def test_closest_integer_zero(self):
        value = "0"
        expected = 0
        self.assertEqual(closest_integer(value), expected)

    def test_closest_integer_positive_integer(self):
        value = "10"
        expected = 10
        self.assertEqual(closest_integer(value), expected)

    def test_closest_integer_negative_integer(self):
        value = "-10"
        expected = -10
        self.assertEqual(closest_integer(value), expected)

    def test_closest_integer_positive_half(self):
        value = "14.5"
        expected = 15
        self.assertEqual(closest_integer(value), expected)

    def test_closest_integer_negative_half(self):
        value = "-14.5"
        expected = -15
        self.assertEqual(closest_integer(value), expected)

    def test_closest_integer_positive_decimal(self):
        value = "14.7"
        expected = 15
        self.assertEqual(closest_integer(value), expected)

    def test_closest_integer_negative_decimal(self):
        value = "-14.7"
        expected = -15
        self.assertEqual(closest_integer(value), expected)

    def test_closest_integer_empty_string(self):
        value = ""
        expected = 0
        self.assertEqual(closest_integer(value), expected)

    def test_closest_integer_invalid_input(self):
        value = "abc"
        with self.assertRaises(ValueError):
            closest_integer(value)

# if __name__ == '__main__':
#     unittest.main()