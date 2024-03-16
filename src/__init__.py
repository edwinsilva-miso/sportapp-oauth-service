from flask import Flask

# Routes
from .routes import AuthRoutes
from .routes import AlertRoutes

app = Flask(__name__)


def init_app(config):
    # Configuration
    app.config.from_object(config)

    # Blueprints
    app.register_blueprint(AuthRoutes.main, url_prefix='/oauth/token')
    app.register_blueprint(AlertRoutes.main, url_prefix='/api/alerts')

    return app
