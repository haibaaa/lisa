from flask import Flask

from api import client, create, sync
from config import Config
from db import db


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    app.register_blueprint(client.client_bp)
    app.register_blueprint(create.create_bp)
    app.register_blueprint(sync.sync_bp)
    return app
