"""CLI Personalizado"""

import click

from delivery.ext.db import db
from delivery.ext.site import models  # noqa


def init_app(app):
    """Incializa o CLI"""

    @app.cli.command("create-db")
    def create_db():
        """Este comando inicializa o banco de dados"""
        db.create_all()

    @app.cli.command("listar-pedidos")
    def listar_pedidos():
        """Este comando lista os pedidos"""
        click.echo("Lista de Pedidos")

    @app.cli.command("listar-usuarios")
    def listar_usuarios():
        """Este comando lista os usuários"""
        click.echo("Lista os Usuários")


