def test_closest_integer(closest_integer):
    assert closest_integer("10") == 10, "Test 1"# pragma: no cover
    assert closest_integer("14.5") == 15, "Test 2"# pragma: no cover
    assert  closest_integer("10.6") == 11
    assert  closest_integer("15.6") == 16
