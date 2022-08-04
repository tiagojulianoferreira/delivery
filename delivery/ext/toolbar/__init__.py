from flask_debugtoolbar import DebugToolbarExtension


def init_app(app):
    """Incializa a barra de ferramentas para dev do Flask"""
    DebugToolbarExtension(app)