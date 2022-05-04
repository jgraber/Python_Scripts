import pytest

def test_1_is_printed_as_001():
    index = 1
    assert format_numer(index) == '001'

def test_1000_is_printed_as_1000():
    index = 1000
    assert format_numer(index) == '1000'

def format_numer(number):
    # https://python-reference.readthedocs.io/en/latest/docs/str/rjust.html
    return str(number).rjust(3, '0')

@pytest.mark.parametrize("input, expected",
                         [(['a/a.txt'], ['a_001.txt']),
                          (['a/a.txt', 'a/b.txt'], ['a_001.txt','a_002.txt']),
                          (['a/a.txt', 'b/b.txt'], ['a_001.txt','b_001.txt']),
                          (['a/a.txt', 'b/a.txt'], ['a_001.txt','b_001.txt'])
                         ])
def test_file_names_are_correctly_translated(input, expected):
    assert expected == input
    print(f"{input}: {expected}")