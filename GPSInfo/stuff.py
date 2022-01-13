import click

@click.command(context_settings={"ignore_unknown_options": True})
@click.argument('files', nargs=-1, type=click.Path(exists=True, file_okay=True, dir_okay=True, resolve_path=True))
def hello(files):
    """Print all FILES file names."""
    for filename in files:
        click.echo(filename)

@click.version_option(version='2.0.0', prog_name='abc')
@click.group()
def cli():
    pass


if __name__ == '__main__':
    hello()