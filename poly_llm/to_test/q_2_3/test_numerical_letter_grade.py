def test_numerical_letter_grade(numerical_letter_grade):
    assert numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]) == ['A+', 'B', 'C-', 'C', 'A-']# pragma: no cover
    assert numerical_letter_grade([1.2]) == ['D+']# pragma: no cover
    assert numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]) == ['A+', 'B', 'C-', 'C', 'A-']# pragma: no cover
    assert numerical_letter_grade([1.2]) == ['D+']# pragma: no cover
