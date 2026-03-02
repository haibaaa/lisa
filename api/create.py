import secrets
from flask import Blueprint, jsonify, request
from db import db
from models.project import Project


create_bp: Blueprint = Blueprint(
    "create",
    __name__,
    url_prefix="/create",
)
"""
create a project and return client and write keys
"""


@create_bp.route("/project", methods=["POST"])
def create_project_handler():
    # add validation later --> error out on missing fields
    params = request.get_json()
    if not params or "name" not in params:
        return (
            jsonify(
                {
                    "error": "expected project name",
                }
            ),
            400,
        )

    project = Project(
        name=params["name"],
        client_api=secrets.token_urlsafe(16),
        # in future --> hash the write key
        write_api=secrets.token_urlsafe(16),
    )
    db.session.add(project)
    db.session.commit()

    return (
        jsonify(
            client_api=project.client_api,
            write_api=project.write_api,
        ),
        200,
    )
