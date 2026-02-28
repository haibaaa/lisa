import os


class Config:
    SQLALCHEMY_DATABASE_URI: str = os.environ["DATABASE_URL"]
