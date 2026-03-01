from flask import Blueprint, jsonify
from utils.utils import parse_value
from models.project import Project
from models.remote_configs import RemoteConfig

client_bp: Blueprint = Blueprint("clients", __name__, url_prefix="/client")

"""
client requests a project's variables and is returned the
record if it exists and an error code otherwise
"""


@client_bp.route("/projects/<string:client_api>/config")
def config_request_handler(client_api: str):
    project = Project.query.filter_by(
        client_api=client_api,
    ).first()
    if project is None:
        return jsonify({"error": "invalid api"}), 404

    configs = RemoteConfig.query.filter_by(
        project_id=project.id,
    ).all()

    return jsonify({config.key: parse_value(config) for config in configs})
