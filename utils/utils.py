# utils/utils.py
import json
from utils.enums import ValueType
from models.remote_configs import RemoteConfig


"""
helper to parse values according to their value types
"""


def parse_value(config: RemoteConfig):
    if config.value_type == ValueType.boolean:
        return config.value.lower() == "true"
    if config.value_type == ValueType.number:
        return float(config.value) if "." in config.value else int(config.value)
    if config.value_type == ValueType.json:
        return json.loads(config.value)

    return config.value
