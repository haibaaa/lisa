# scripts/seed_db.py
import secrets
from flask import Flask

from app import create_app
from db import db
from models.project import Project


def seed():
    app: Flask = create_app()

    with app.app_context():
        db.create_all()

        if Project.query.first():
            print("already seeded")
            return

        seed_data = Project(
            name="stub project",
            api_identifier=secrets.token_urlsafe(64),
        )

        db.session.add(seed_data)
        db.session.commit()

        print("seeded")


if __name__ == "__main__":
    seed()
