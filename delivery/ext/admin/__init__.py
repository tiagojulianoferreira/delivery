from flask_admin import Admin

admin = Admin()

def init_app(app):
    """Inicializa interface administrativa"""
    admin.name = "Codefoods"
    admin.template_mode = "bootstrap2"
    admin.init_app(app)