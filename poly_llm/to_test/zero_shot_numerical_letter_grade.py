import unittest

def numerical_letter_grade(grades):
    """It is the last week of the semester and the teacher has to give the grades
    to students. The teacher has been making her own algorithm for grading.
    The only problem is, she has lost the code she used for grading.
    She has given you a list of GPAs for some students and you have to write
    a function that can output a list of letter grades using the following table:
            GPA       |    Letter grade
            4.0                A+
            > 3.7                A
            > 3.3                A-
            > 3.0                B+
            > 2.7                B
            > 2.3                B-
            > 2.0                C+
            > 1.7                C
            > 1.3                C-
            > 1.0                D+
            > 0.7                D
            > 0.0                D-
            0.0                E
    Example:
    grade_equation([4.0, 3, 1.7, 2, 3.5]) ==> ['A+', 'B', 'C-', 'C', 'A-']
    """
    letter_grade = []
    for gpa in grades:
        if gpa == 4.0:
            letter_grade.append("A+")
        elif gpa > 3.7:
            letter_grade.append("A")
        elif gpa > 3.3:
            letter_grade.append("A-")
        elif gpa > 3.0:
            letter_grade.append("B+")
        elif gpa > 2.7:
            letter_grade.append("B")
        elif gpa > 2.3:
            letter_grade.append("B-")
        elif gpa > 2.0:
            letter_grade.append("C+")
        elif gpa > 1.7:
            letter_grade.append("C")
        elif gpa > 1.3:
            letter_grade.append("C-")
        elif gpa > 1.0:
            letter_grade.append("D+")
        elif gpa > 0.7:
            letter_grade.append("D")
        elif gpa > 0.0:
            letter_grade.append("D-")
        else:
            letter_grade.append("E")
    return letter_grade


class TestNumericalLetterGradeFunction(unittest.TestCase):

    def test_numerical_letter_grade_example(self):
        grades = [4.0, 3, 1.7, 2, 3.5]
        expected = ['A+', 'B', 'C-', 'C', 'A-']
        self.assertEqual(numerical_letter_grade(grades), expected)

    def test_numerical_letter_grade_a_plus(self):
        grades = [4.0]
        expected = ['A+']
        self.assertEqual(numerical_letter_grade(grades), expected)

    def test_numerical_letter_grade_a(self):
        grades = [3.8]
        expected = ['A']
        self.assertEqual(numerical_letter_grade(grades), expected)

    def test_numerical_letter_grade_a_minus(self):
        grades = [3.4]
        expected = ['A-']
        self.assertEqual(numerical_letter_grade(grades), expected)

    def test_numerical_letter_grade_b_plus(self):
        grades = [3.1]
        expected = ['B+']
        self.assertEqual(numerical_letter_grade(grades), expected)

    def test_numerical_letter_grade_b(self):
        grades = [2.8]
        expected = ['B']
        self.assertEqual(numerical_letter_grade(grades), expected)

    def test_numerical_letter_grade_b_minus(self):
        grades = [2.4]
        expected = ['B-']
        self.assertEqual(numerical_letter_grade(grades), expected)

    def test_numerical_letter_grade_c_plus(self):
        grades = [2.1]
        expected = ['C+']
        self.assertEqual(numerical_letter_grade(grades), expected)

    def test_numerical_letter_grade_c(self):
        grades = [1.8]
        expected = ['C']
        self.assertEqual(numerical_letter_grade(grades), expected)

    def test_numerical_letter_grade_c_minus(self):
        grades = [1.4]
        expected = ['C-']
        self.assertEqual(numerical_letter_grade(grades), expected)

    def test_numerical_letter_grade_d_plus(self):
        grades = [1.1]
        expected = ['D+']
        self.assertEqual(numerical_letter_grade(grades), expected)

    def test_numerical_letter_grade_d(self):
        grades = [0.8]
        expected = ['D']
        self.assertEqual(numerical_letter_grade(grades), expected)

    def test_numerical_letter_grade_d_minus(self):
        grades = [0.1]
        expected = ['D-']
        self.assertEqual(numerical_letter_grade(grades), expected)

    def test_numerical_letter_grade_e(self):
        grades = [0.0]
        expected = ['E']
        self.assertEqual(numerical_letter_grade(grades), expected)

    def test_numerical_letter_grade_empty_list(self):
        grades = []
        expected = []
        self.assertEqual(numerical_letter_grade(grades), expected)

    def test_numerical_letter_grade_negative_gpa(self):
        grades = [-1.0]
        expected = ['E']
        self.assertEqual(numerical_letter_grade(grades), expected)

# if __name__ == '__main__':
#     unittest.main()