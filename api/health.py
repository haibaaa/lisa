from flask import Blueprint, jsonify
from sqlalchemy import text
from db import db

health_bp = Blueprint("health", __name__)


@health_bp.route("/health/db")
def db_health():
    try:
        _ = db.session.execute(text("SELECT 1"))
        return jsonify(status="ok", db="reachable")
    except Exception as e:
        return jsonify(status="error", error=str(e)), 500
