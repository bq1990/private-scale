import click
from flask.cli import FlaskGroup

from private_scale.database import db


def create_app(info):
    from private_scale.app import create_app
    return create_app()


@click.group(cls=FlaskGroup, create_app=create_app)
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
