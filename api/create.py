import secrets
from flask import Blueprint, jsonify, request
from db import db
from models.project import Project


"""
allows a person to create a project

returns
{
    "client_api": {client_api},
    "config_api": {config_api}
}
"""

create_bp: Blueprint = Blueprint(
    "create",
    __name__,
    url_prefix="/create",
)


@create_bp.route("/<string:name>")
def create_project_handler(name):
    project = Project(
        name=name,
        client_api=secrets.token_urlsafe(16),
        # in future --> hash the write key
        config_api=secrets.token_urlsafe(16),
    )
    db.session.add(project)
    db.session.commit()

    return (
        jsonify(
            client_api=project.client_api,
            config_api=project.config_api,
        ),
        200,
    )
