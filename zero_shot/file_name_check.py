import unittest

class TestFileNameCheck(unittest.TestCase):
    def test_valid_file_name(self):
        self.assertEqual(file_name_check("example.txt"), 'Yes')
        self.assertEqual(file_name_check("example.exe"), 'Yes')
        self.assertEqual(file_name_check("example.dll"), 'Yes')

    def test_invalid_file_name_more_than_three_digits(self):
        self.assertEqual(file_name_check("1234example.txt"), 'No')

    def test_invalid_file_name_no_dot(self):
        self.assertEqual(file_name_check("exampletxt"), 'No')

    def test_invalid_file_name_multiple_dots(self):
        self.assertEqual(file_name_check("example.txt.dll"), 'No')

    def test_invalid_file_name_empty_before_dot(self):
        self.assertEqual(file_name_check(".txt"), 'No')

    def test_invalid_file_name_non_latin_alphabet_start(self):
        self.assertEqual(file_name_check("1example.txt"), 'No')
        self.assertEqual(file_name_check("_example.txt"), 'No')

    def test_invalid_file_name_invalid_suffix(self):
        self.assertEqual(file_name_check("example.pdf"), 'No')

    def test_edge_cases(self):
        self.assertEqual(file_name_check(""), 'No')
        self.assertEqual(file_name_check("."), 'No')
        self.assertEqual(file_name_check(".txt"), 'No')
        self.assertEqual(file_name_check("example"), 'No')
        self.assertEqual(file_name_check("example."), 'No')

if __name__ == '__main__':
    unittest.main()