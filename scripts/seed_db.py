# scripts/seed_db.py
from dotenv import load_dotenv
import secrets
from flask import Flask

load_dotenv()

from app import create_app
from db import db
from models.project import Project
from models.remote_configs import RemoteConfig, ValueType


def seed():
    app: Flask = create_app()
    with app.app_context():
        db.create_all()

        if Project.query.first():
            print("already seeded")
            return

        # later add checks if generated string has conflicts
        # ignore lsp errors on parameters
        project = Project(
            name="stub_project",
            client_api=secrets.token_urlsafe(16),
            write_api=secrets.token_urlsafe(16),
        )
        db.session.add(project)
        db.session.flush()  # get project.id before committing

        configs = [
            RemoteConfig(
                project_id=project.id,
                key="enable_dark_mode",
                value="true",
                value_type=ValueType.boolean,
            ),
            RemoteConfig(
                project_id=project.id,
                key="max_retries",
                value="3",
                value_type=ValueType.number,
            ),
            RemoteConfig(
                project_id=project.id,
                key="welcome_message",
                value="welcome to the app!",
                value_type=ValueType.string,
            ),
            RemoteConfig(
                project_id=project.id,
                key="feature_flags",
                value='{"new_checkout": false, "referral_program": true}',
                value_type=ValueType.json,
            ),
        ]

        db.session.add_all(configs)
        db.session.commit()
        print(f"seeded project '{project.name}' with {len(configs)} remote configs")


if __name__ == "__main__":
    seed()
