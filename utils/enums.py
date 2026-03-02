# utils/enums.py
import enum


class ValueType(str, enum.Enum):
    string = "string"
    boolean = "boolean"
    number = "number"
    json = "json"
