import filedate
from pathlib import Path

def test_create_files():
    a = 'test_data/aa.txt'
    Path(a).write_text("")
    a_file = filedate.File(a)
    a_file.set(
        created = "2022.01.01 13:00:00",
        modified = "2022.01.01 14:00:00",
        accessed = "2022.01.01 15:00:00"
    )

    b = 'test_data/bb.txt'
    Path(b).write_text("")
    b_file = filedate.File(b)
    b_file.set(
        created = "2022.01.02 13:00:00",
        modified = "2022.01.02 14:00:00",
        accessed = "2022.01.02 15:00:00"
    )