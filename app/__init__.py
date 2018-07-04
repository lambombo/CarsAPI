import os

from flask import Flask
from config import config

def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # Initialize flask extensions



    # Register Blueprints

    from .status import status as status_blueprint
    app.register_blueprint(status_blueprint)

    from .cars import cars as cars_blueprint
    app.register_blueprint(cars_blueprint, url_prefix='/cars')

    return app
