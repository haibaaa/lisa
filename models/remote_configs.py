# models/remote_config.py
from sqlalchemy import String, Text, Enum, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column
from db import db
from utils.enums import ValueType
import uuid


class RemoteConfig(db.Model):
    __tablename__ = "remote_configs"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4,
    )
    project_id: Mapped[int] = mapped_column(
        ForeignKey("projects.id", ondelete="CASCADE"),
        nullable=False,
    )
    key: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )
    value: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )
    value_type: Mapped[ValueType] = mapped_column(
        Enum(ValueType),
        nullable=False,
        default=ValueType.string,
    )
    # if implemmenting logging in the future

    # created_at: Mapped[datetime] = mapped_column(
    #     DateTime,
    #     server_default=func.now(),
    # )
    # updated_at: Mapped[datetime] = mapped_column(
    #     DateTime,
    #     server_default=func.now(),
    #     onupdate=func.now(),
    # )
    # project: Mapped[Project] = relationship(
    #     "Project",
    #     back_populates="remote_configs",
    # )

    __table_args__ = (
        UniqueConstraint(
            "project_id",
            "key",
            name="uq_project_key",
        ),
    )

    def __repr__(self) -> str:
        return f"<RemoteConfig project_id={self.project_id} key={self.key!r} type={self.value_type.value}>"
