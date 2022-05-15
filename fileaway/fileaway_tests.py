import pytest
import os

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
                          (['a/a.txt', 'b/a.txt'], ['a_001.txt','b_001.txt']),
                          (['a/b/c.txt'], ['a_b_001.txt']),
                         ])
def test_file_names_are_correctly_translated(input, expected, monkeypatch: pytest.MonkeyPatch):
    # monkeypatch.chdir(os.path.dirname(os.path.dirname(__file__)))
    workingDir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    for file in input:
        test_file_path = os.path.join(
            os.path.relpath(
                workingDir + 
                '/correct_translated/'), 
            file)
        print(f"{file} -> {os.path.abspath(test_file_path)}")
    
    # assert expected == input
    print(f"{input}: {expected}")