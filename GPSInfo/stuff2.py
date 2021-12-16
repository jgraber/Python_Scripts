# see Comparing Python Command-Line Parsing Libraries – Argparse, Docopt, and Click
# https://realpython.com/comparing-python-command-line-parsing-libraries-argparse-docopt-click/

import click

@click.group()
@click.version_option(version='1.0.0')
def greet():
    pass


@greet.command()
@click.argument('name')  # add the name argument
def hello(**kwargs):
    print('Hello, {0}!'.format(kwargs['name']))


@greet.command()
@click.argument('name')
def goodbye(**kwargs):
    print('Goodbye, {0}!'.format(kwargs['name']))

if __name__ == '__main__':
    greet()