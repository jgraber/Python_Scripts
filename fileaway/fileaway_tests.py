def test_1_is_printed_as_001():
    index = 1
    formated = (str(index).rjust(3, '0'))
    assert formated == '001'

def test_1000_is_printed_as_1000():
    index = 1000
    formated = (str(index).rjust(3, '0'))
    assert formated == '1000'