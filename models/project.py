import uuid
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from db import db

"""
schema for project
each project corresponds to one client app
multiple users from multiple platforms maybe accessing
this project db for configuration variables

what must the schema have
"""


class Project(db.Model):
    __tablename__ = "projects"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4,
    )

    name: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
    )

    client_api: Mapped[str] = mapped_column(
        String(64),
        unique=True,
        nullable=False,
        index=True,
    )
