import click
import os

def split_folder(folder, split_by):
    click.echo(f"work with folder: {folder} - split by {split_by}")

    files = os.listdir(folder)
    for file in files:
        print(file)
        # https://stackoverflow.com/questions/11348953/how-can-i-set-the-last-modified-time-of-a-file-from-python

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