import unittest

def file_name_check(file_name):
    """Create a function which takes a string representing a file's name, and returns
    'Yes' if the the file's name is valid, and returns 'No' otherwise.
    A file's name is considered to be valid if and only if all the following conditions
    are met:
    - There should not be more than three digits ('0'-'9') in the file's name.
    - The file's name contains exactly one dot '.'
    - The substring before the dot should not be empty, and it starts with a letter from
    the latin alphapet ('a'-'z' and 'A'-'Z').
    - The substring after the dot should be one of these: ['txt', 'exe', 'dll']
    Examples:
    file_name_check("example.txt") # => 'Yes'
    file_name_check("1example.dll") # => 'No' (the name should start with a latin alphapet letter)
    """
    suf = ['txt', 'exe', 'dll']
    lst = file_name.split(sep='.')
    if len(lst) != 2:
        return 'No'
    if not lst[1] in suf:
        return 'No'
    if len(lst[0]) == 0:
        return 'No'
    if not lst[0][0].isalpha():
        return 'No'
    t = len([x for x in lst[0] if x.isdigit()])
    if t > 3:
        return 'No'
    return 'Yes'


class TestFileNameCheckFunction(unittest.TestCase):

    def test_file_name_check_valid(self):
        file_name = "example.txt"
        expected = 'Yes'
        self.assertEqual(file_name_check(file_name), expected)

    def test_file_name_check_invalid_start(self):
        file_name = "1example.dll"
        expected = 'No'
        self.assertEqual(file_name_check(file_name), expected)

    def test_file_name_check_empty_before_dot(self):
        file_name = ".txt"
        expected = 'No'
        self.assertEqual(file_name_check(file_name), expected)

    def test_file_name_check_invalid_extension(self):
        file_name = "example.pdf"
        expected = 'No'
        self.assertEqual(file_name_check(file_name), expected)

    def test_file_name_check_multiple_dots(self):
        file_name = "example.txt.exe"
        expected = 'No'
        self.assertEqual(file_name_check(file_name), expected)

    def test_file_name_check_too_many_digits(self):
        file_name = "exa1234mple.txt"
        expected = 'No'
        self.assertEqual(file_name_check(file_name), expected)

    def test_file_name_check_empty_string(self):
        file_name = ""
        expected = 'No'
        self.assertEqual(file_name_check(file_name), expected)

    def test_file_name_check_no_extension(self):
        file_name = "example"
        expected = 'No'
        self.assertEqual(file_name_check(file_name), expected)

# if __name__ == '__main__':
#     unittest.main()