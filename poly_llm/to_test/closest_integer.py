
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

def test_closest_integer():# pragma: no cover
    assert closest_integer("10") == 10, "Test 1"# pragma: no cover
    assert closest_integer("14.5") == 15, "Test 2"# pragma: no cover


# Added test cases for new prompts
def test_closest_sup_integer():
    assert  closest_integer("10.6") == 11
    assert  closest_integer("15.6") == 16


def test_closest_lower_integer():
    assert closest_integer("10.4") == 10
    assert closest_integer("0.3") == 0

