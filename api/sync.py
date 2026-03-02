from flask import Blueprint, jsonify, request
from models.project import Project
from models.remote_configs import RemoteConfig
from utils.enums import ValueType
from db import db

sync_bp: Blueprint = Blueprint(
    "sync",
    __name__,
    url_prefix="/sync",
)

"""
user can sync configuration variables with the server
using the write api
expects a raw json blob with the config params
{
    "config_var_1" : {"value": {value}, "value_type": {type}},
    "config_var_2" : {"value": {value}, "value_type": {type}}
     ...
}
"""


@sync_bp.route("/<string:config_api>", methods=["POST"])
def sync_request_handler(config_api: str):
    request_config: dict[str, dict] = request.get_json()

    project: Project | None = Project.query.filter_by(config_api=config_api).first()
    if project is None:
        return jsonify({"error": "invalid api"}), 400

    raw_configs: list[RemoteConfig] = RemoteConfig.query.filter_by(
        project_id=project.id
    ).all()
    server_configs: dict[str, RemoteConfig] = {c.key: c for c in raw_configs}

    added: list[str] = []
    updated: list[str] = []
    deleted: list[str] = []

    for key, payload in request_config.items():
        try:
            value: str = payload["value"]
            value_type: ValueType = ValueType(payload["value_type"])
        except (KeyError, ValueError):
            return jsonify({"error": f"invalid payload for key '{key}'"}), 400

        # add new config params
        if key not in server_configs:
            db.session.add(
                RemoteConfig(
                    project_id=project.id,
                    key=key,
                    value=value,
                    value_type=value_type,
                )
            )
            added.append(key)
        # update old params
        elif (
            server_configs[key].value != value
            or server_configs[key].value_type != value_type
        ):
            server_configs[key].value = value
            server_configs[key].value_type = value_type
            updated.append(key)

    # bulk delete
    keys_to_delete: list[str] = [
        key for key in server_configs if key not in request_config
    ]
    if keys_to_delete:
        RemoteConfig.query.filter(
            RemoteConfig.project_id == project.id,
            RemoteConfig.key.in_(keys_to_delete),
        ).delete(synchronize_session=False)
        deleted.extend(keys_to_delete)

    db.session.commit()

    return jsonify({"added": added, "updated": updated, "deleted": deleted}), 200
