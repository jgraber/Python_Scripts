def test_1_is_printed_as_001():
    index = 1
    assert format_numer(index) == '001'

def test_1000_is_printed_as_1000():
    index = 1000
    assert format_numer(index) == '1000'

def format_numer(number):
    # https://python-reference.readthedocs.io/en/latest/docs/str/rjust.html
    return str(number).rjust(3, '0')