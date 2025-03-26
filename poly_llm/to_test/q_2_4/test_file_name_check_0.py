def test_file_name_check(file_name_check):
    assert file_name_check("example.txt") == 'Yes'
    assert file_name_check("1example.dll") == 'No'
    assert file_name_check('.txt') == 'No'# pragma: no cover
    assert file_name_check("example.py.dll") == 'No'
    assert file_name_check(".py.dll") == 'No'
    assert file_name_check("example.txt") == 'Yes'
    assert file_name_check("1example.dll") == 'No'
    assert file_name_check('.txt') == 'No'# pragma: no cover
