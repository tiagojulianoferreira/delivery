def init_app(app):
    app.config['SECRET_KEY'] = 'codeshow'
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///delivery.db'
    