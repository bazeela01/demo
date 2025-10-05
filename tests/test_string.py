import pytest



@pytest.mark.parametrize("str",['test','mom','amonm'])
def test_palindrome(str):
    assert str[::-1] == str
