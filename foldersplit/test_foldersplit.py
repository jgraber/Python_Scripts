import filedate
from pathlib import Path
import os
import foldersplit
import datetime
from glob import glob
import shutil

def test_create_files():
    os.makedirs('test_data',exist_ok=True)
    folders = glob('test_data/_*', recursive = True)
    for folder in folders:
        shutil.rmtree(folder)
    # a = 'test_data/aa.txt'
    # Path(a).write_text("")
    # a_file = filedate.File(a)
    # a_file.set(
    #     created = "2022.01.01 13:00:00",
    #     modified = "2022.01.01 14:00:00",
    #     accessed = "2022.01.01 15:00:00"
    # )
    create_file_with_date('test_data/aa.txt', "2022.01.01 13:00:00")
    create_file_with_date('test_data/bb.txt', "2022.01.02 13:00:00")


def test_correct_folder_for_day():
    file_date = datetime.date(2021, 3, 4)
    name = foldersplit._get_subfolder(file_date, 'day')
    assert name == '_2021-03-04'

def test_correct_folder_for_month():
    file_date = datetime.date(2021, 3, 4)
    name = foldersplit._get_subfolder(file_date, 'month')
    assert name == '_2021-03'

def create_file_with_date(path, date):
    Path(path).write_text("")
    new_file = filedate.File(path)
    new_file.set(
        created = date,
        modified = date,
        accessed = date
    )