def test_find_closest_elements(find_closest_elements):
    assert find_closest_elements([1.0,1.1,0.9,0.8]) == (1.1, 1.1)
    assert find_closest_elements([1.0,1.2,0.9,0.8]) == (0.9, 0.8)
    assert find_closest_elements([1.0,1.1,0.9,0.8]) == (1.1, 1.1)
