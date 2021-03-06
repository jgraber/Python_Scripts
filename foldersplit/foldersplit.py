import click
import os
import shutil
from datetime import datetime
from pathlib import Path
import progressbar

def split_folder(folder, split_by):
    click.echo(f"work with folder: {folder} - split by {split_by}")

    move = []
    with os.scandir(folder) as it:
        for entry in it:
            if not entry.name.startswith('.') and entry.is_file():
                stat = entry.stat()
                dt_object = datetime.fromtimestamp(stat.st_ctime)
                subfolder = _get_subfolder(dt_object, split_by)
                path = Path(folder, subfolder, entry.name)
                move.append((entry.path, str(path)))

    for old, new in progressbar.progressbar(move):
        dir_name, _ = os.path.split(new)
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)

        print(f"{old} -> {new}")
        shutil.move(old, new)
        

def _get_subfolder(create_date, split_by):
    """Creates a name for a subfolder depending on the date and how you want to split it."""
    if split_by == 'month':
        return "_" + create_date.strftime('%Y-%m')

    return "_" + create_date.strftime('%Y-%m-%d')


@click.command()
@click.option('--split-by',
              type=click.Choice(['day', 'month'], 
              case_sensitive=False),
              default='day')
@click.argument('folder', type=click.Path(exists=True))
@click.version_option(version='1.0.0')
def split(folder, split_by):
    """Splits the files inside a folder into subfolders (by date or month)"""
    split_folder(folder, split_by)


if __name__ == '__main__':
    split()