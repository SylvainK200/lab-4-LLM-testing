import unittest
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    closest_pair = None
    distance = None
    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                if distance is None:
                    distance = abs(elem - elem2)
                    closest_pair = tuple(sorted([elem, elem2]))
                else:
                    new_distance = abs(elem - elem2)
                    if new_distance < distance:
                        distance = new_distance
                        closest_pair = tuple(sorted([elem, elem2]))
    return closest_pair


class TestFindClosestElementsFunction(unittest.TestCase):

    def test_find_closest_elements_example(self):
        numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2.2]
        expected = (2.0, 2.2)
        self.assertEqual(find_closest_elements(numbers), expected)

    def test_find_closest_elements_duplicate(self):
        numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2.0]
        expected = (2.0, 2.0)
        self.assertEqual(find_closest_elements(numbers), expected)

    def test_find_closest_elements_empty_list(self):
        with self.assertRaises(IndexError):
            find_closest_elements([])

    def test_find_closest_elements_single_element(self):
        with self.assertRaises(IndexError):
            find_closest_elements([1.0])

    def test_find_closest_elements_negative_numbers(self):
        numbers = [-1.0, 2.0, -3.0, 4.0, 5.0, -2.2]
        expected = (-3.0, -2.2)
        self.assertEqual(find_closest_elements(numbers), expected)

    def test_find_closest_elements_equal_distance(self):
        numbers = [1.0, 3.0, 5.0, 2.0, 4.0]
        expected = (1.0, 2.0)  # either (1.0, 2.0) or (2.0, 3.0) could be considered correct
        closest = find_closest_elements(numbers)
        self.assertIn(closest, [(1.0, 2.0), (2.0, 3.0), (3.0, 4.0), (4.0, 5.0)])

    def test_find_closest_elements_floats(self):
        numbers = [1.1, 2.2, 3.3, 4.4, 5.5, 1.11]
        expected = (1.1, 1.11)
        self.assertEqual(find_closest_elements(numbers), expected)

# if __name__ == '__main__':
#     unittest.main()