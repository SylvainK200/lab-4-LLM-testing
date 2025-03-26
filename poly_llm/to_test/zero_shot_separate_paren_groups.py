import unittest
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    result = []
    current_string = []
    current_depth = 0

    for c in paren_string.replace(' ', ''):
        if c == '(':
            current_depth += 1
            current_string.append(c)
        elif c == ')':
            current_depth -= 1
            current_string.append(c)

            if current_depth == 0:
                result.append(''.join(current_string))
                current_string.clear()

    return result


class TestSeparateParenGroupsFunction(unittest.TestCase):

    def test_separate_paren_groups_example(self):
        paren_string = '( ) (( )) (( )( ))'
        expected = ['()', '(())', '(()())']
        self.assertEqual(separate_paren_groups(paren_string), expected)

    def test_separate_paren_groups_empty_string(self):
        paren_string = ''
        expected = []
        self.assertEqual(separate_paren_groups(paren_string), expected)

    def test_separate_paren_groups_single_group(self):
        paren_string = '( )'
        expected = ['()']
        self.assertEqual(separate_paren_groups(paren_string), expected)

    def test_separate_paren_groups_multiple_groups(self):
        paren_string = '( ) (( )) (( )( ))'
        expected = ['()', '(())', '(()())']
        self.assertEqual(separate_paren_groups(paren_string), expected)

    def test_separate_paren_groups_nested_groups(self):
        paren_string = '( () ) (( () ))'
        expected = ['(())', '((()))']
        self.assertEqual(separate_paren_groups(paren_string), expected)

    def test_separate_paren_groups_spaces(self):
        paren_string = '( )  ( ( ) )  ( )'
        expected = ['()', '(())', '()']
        self.assertEqual(separate_paren_groups(paren_string), expected)

    def test_separate_paren_groups_unbalanced(self):
        paren_string = '( ) ( ('
        with self.assertRaises(ValueError):
            separate_paren_groups(paren_string)

    def test_separate_paren_groups_invalid_input(self):
        paren_string = 'a b c'
        expected = []
        self.assertEqual(separate_paren_groups(paren_string), expected)

    def test_separate_paren_groups_single_parenthesis(self):
        paren_string = '('
        with self.assertRaises(ValueError):
            separate_paren_groups(paren_string)

    def test_separate_paren_groups_multiple_single_parentheses(self):
        paren_string = '('
        with self.assertRaises(ValueError):
            separate_paren_groups(paren_string)

# if __name__ == '__main__':
#     unittest.main()