import click


@click.group()
@click.version_option(version='1.0.0')
def greet():
    pass


@greet.command()
def hello(**kwargs):
    pass


@greet.command()
def goodbye(**kwargs):
    pass

if __name__ == '__main__':
    greet()