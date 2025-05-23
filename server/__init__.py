from flask import Flask

def create_app(config_class=None):
    app = Flask(__name__)

    # Optional: load config from a class or object
    if config_class:
        app.config.from_object(config_class)
    else:
        app.config.from_pyfile("config.py")

    # Register blueprints
    from server.api.routes import api_blueprint
    app.register_blueprint(api_blueprint, url_prefix="/api")

    return app