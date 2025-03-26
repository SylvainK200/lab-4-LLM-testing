def test_numerical_letter_grade(numerical_letter_grade):
    assert numerical_letter_grade([4.0, 3.0, 2.0, 1.0, 0.0]) == ['A+', 'B', 'C', 'D+', 'E']
    assert numerical_letter_grade([4.0, 3.0, 2.0, 1.0, 0.0]) == ['A+', 'B', 'C', 'D+', 'E']
