from pytest_demo import string_counts

def test_string_counts():
    dct = string_counts()
    assert dct['ERROR'] == 3
    assert dct['WARNING'] == 11
    assert dct['INFO'] == 50