def test_file_name_check(file_name_check):
    assert file_name_check("example.txt") == 'Yes' # pragma: no cover
    assert file_name_check("1example.dll") == 'No' # pragma: no cover
    assert file_name_check('.txt') == 'No'# pragma: no cover
    assert file_name_check("example.txt") == 'Yes'
    assert file_name_check("1example.dll") == 'No'
    assert file_name_check('.txt') == 'No'
    assert file_name_check("example.txt") == 'Yes' # pragma: no cover
    assert file_name_check("1example.dll") == 'No' # pragma: no cover
    assert file_name_check('.txt') == 'No'# pragma: no cover
    assert file_name_check("example.txt") == 'Yes'
    assert file_name_check("1example.dll") == 'No'
    assert file_name_check('.txt') == 'No'
    assert file_name_check("example.txt") == 'Yes' # pragma: no cover
