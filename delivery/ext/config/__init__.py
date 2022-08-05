def init_app(app):
    app.config['SECRET_KEY'] = 'codeshow'
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///delivery.db'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    app.config["FLASK_ADMIN_SWATCH"] = "superhero"

    # DEBUG
    if app.debug:
        app.config['DEBUG_TB_ENABLED'] = True
        app.config['SQLALCHEMY_RECORD_QUERIES'] = True
        app.config['DEBUG_TB_PROFILER_ENABLED'] = True

        app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
    
        
    