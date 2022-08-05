"""CLI Personalizado"""

import click

from delivery.ext.auth.models import User
from delivery.ext.db import models  # noqa
from delivery.ext.db import db


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
        users = User.query.all()
        click.echo(f"Listados os usuários {users}")
        

    @app.cli.command("add-user")
    @click.option("--email", "-e")
    @click.option("--passwd", "-p")
    @click.option("--admin", "-a", is_flag=True, default=False)

    def add_user(email, passwd, admin):
        """Cli para adicionar novo usuário"""
        user = User(
            email=email,
            passwd=passwd,
            admin=admin
        )
        db.session.add(user)
        db.session.commit()

        click.echo(f"Usuário {email} adicionado com sucesso!")

