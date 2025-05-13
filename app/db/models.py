from sqlalchemy import Table, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db.db import metadata

users = Table(
    "users", metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String, unique=True, index=True, nullable=False),
    Column("hashed_password", String, nullable=False),
    Column("is_active", Boolean, default=True),
    Column("role_id", Integer, ForeignKey("roles.id")),
)

roles = Table(
    "roles", metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, unique=True, nullable=False),
)