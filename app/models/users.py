from sqlalchemy import MetaData, Table, Column, Integer, String, Boolean, sql, text, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID

metadata = MetaData()

users_table = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(100)),
    Column("email", String(40), unique=True, index=True),
    Column("hashed_password", String()),
    Column("is_active", Boolean(),
           server_default=sql.expression.true(),
           nullable=False,
           ),
)

tokens_table = Table(
    "tokens",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("token",
           UUID(as_uuid=False),
           server_default=text("uuid_generate_v4()"),
           unique=True,
           nullable=False,
           index=True,
           ),
    Column("expires", DateTime()),
    Column("user_id", ForeignKey("users.id")),
)
