from flask import Flask

from api.client import client_bp
from config import Config
from db import db


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    app.register_blueprint(client_bp)
    return app
