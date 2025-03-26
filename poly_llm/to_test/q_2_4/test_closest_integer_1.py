def test_closest_integer(closest_integer):
    assert closest_integer("10.4") == 10
    assert closest_integer("0.3") == 0
    assert closest_integer("10.4") == 10
    assert closest_integer("0.3") == 0
