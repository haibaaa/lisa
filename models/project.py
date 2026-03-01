import uuid
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from db import db

"""
schema for project
each project corresponds to one client app
multiple users from multiple platforms maybe accessing
this project db for configuration variables
"""


class Project(db.Model):
    __tablename__ = "projects"

    client_api: Mapped[str] = mapped_column(
        String(64),
        unique=True,
        nullable=False,
        index=True,
    )

    write_api: Mapped[str] = mapped_column(
        String(64),
        unique=True,
        nullable=False,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
    )

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4,
    )
