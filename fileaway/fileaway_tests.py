from fileaway import *

def test_1_is_printed_as_001():
    index = 1
    assert format_number(index) == '001'


def test_1000_is_printed_as_1000():
    index = 1000
    assert format_number(index) == '1000'


def test_collector_finds_files():
    data = collector("testdata/demo")
    assert len(data) == 8


def test_transform_renames_single_file():
    data = set()
    data.add("\\a\\b\\c.txt")

    result = transform(data, "test_rename")

    assert result == {"\\a\\b\\c.txt": "test_rename_a_b_001.txt"}


def test_transform_renames_multiple_files_in_same_folder():
    data = set()
    data.add("\\a\\b\\c.txt")
    data.add("\\a\\b\\d.jpg")
    data.add("\\a\\b\\f.png")

    expected = {
        "\\a\\b\\c.txt": "test_rename_a_b_001.txt",
        "\\a\\b\\d.jpg": "test_rename_a_b_002.jpg",
        "\\a\\b\\f.png": "test_rename_a_b_003.png"
    }

    result = transform(data, "test_rename")

    assert result == expected


def test_transform_renames_multiple_files_in_multiple_folder():
    data = set()
    data.add("\\a\\b\\c.txt")
    data.add("\\a\\c\\d.jpg")
    data.add("\\a\\d\\f.png")

    expected = {
        "\\a\\b\\c.txt": "test_rename_a_b_001.txt",
        "\\a\\c\\d.jpg": "test_rename_a_c_001.jpg",
        "\\a\\d\\f.png": "test_rename_a_d_001.png"
    }

    result = transform(data, "test_rename")

    assert result == expected
