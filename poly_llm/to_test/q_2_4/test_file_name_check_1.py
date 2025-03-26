def test_file_name_check(file_name_check):
    assert file_name_check("hello.exe") == 'Yes'
    assert file_name_check("hello.dll") == 'Yes'
    assert file_name_check("hello.exe") == 'Yes'
    assert file_name_check("hello.dll") == 'Yes'
    assert file_name_check("hello.exe") == 'Yes'
    assert file_name_check("hello.dll") == 'Yes'
