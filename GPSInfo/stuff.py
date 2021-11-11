import click

# @click.command()
# @click.argument('name')
# def hello(name):
#     click.echo(f'Hello {name}')

@click.command(context_settings={"ignore_unknown_options": True})
@click.argument('files', nargs=-1, type=click.Path(exists=True, file_okay=True, dir_okay=True, resolve_path=True))
def hello(files):
    """Print all FILES file names."""
    for filename in files:
        click.echo(filename)

if __name__ == '__main__':
    hello()