import click

@click.command()
@click.option('--count', default=1, help='number of greetings')
@click.argument('name')
def hello(count, name):
    for x in range(count):
        click.echo(f"Hello {name}!")

@click.command()
@click.argument('folder', type=click.Path(exists=True))
def split(folder):
    print(f"work with folder: {folder}")

if __name__ == '__main__':
    split()