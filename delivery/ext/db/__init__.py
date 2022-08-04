from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app(app):
    """Função que inicializa o banco de dados"""
    db.init_app(app)
