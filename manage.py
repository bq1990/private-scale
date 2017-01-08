import os

import click
from flask.cli import FlaskGroup

from weigh_in.database import db
from weigh_in.settings import common, prod, test


def this_app(info):
    from weigh_in.app import create_app
    if os.getenv('ENV') == 'prod':
        config = prod
    elif os.getenv('ENV') == 'test':
        config = test
    else:
        config = common
        print('dev')
    return create_app(config)


@click.group(cls=FlaskGroup, create_app=this_app)
def cli():
    pass


@cli.command()
def create_all():
    db.create_all()
    click.echo('db created')


@cli.command()
def drop_all():
    db.drop_all()
    click.echo('db dropped')


if __name__ == '__main__':
    cli()
