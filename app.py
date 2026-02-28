import os
from flask import Flask

# from .config import Config
from .db import db
from .api.health import health_bp


def create_app() -> Flask:
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DATABASE_URL"]

    db.init_app(app)

    app.register_blueprint(health_bp)
    return app
