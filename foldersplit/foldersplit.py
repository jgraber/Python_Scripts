import click

@click.command()
@click.option('--count', default=1, help='number of greetings')
@click.argument('name')
def hello(count, name):
    for x in range(count):
        click.echo(f"Hello {name}!")

@click.command()
@click.option('--split-by',
              type=click.Choice(['day', 'month'], 
              case_sensitive=False),
              default='day')
@click.argument('folder', type=click.Path(exists=True))
@click.version_option(version='1.0.0')
def split(folder,split_by):
    """Splits the files inside a folder into subfolders (by date or month)"""
    click.echo(f"work with folder: {folder} - split by {split_by}")

if __name__ == '__main__':
    split()