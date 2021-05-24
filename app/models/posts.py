from sqlalchemy import MetaData, Table, Column, Integer, String, Text, ForeignKey, DateTime
from app.models.users import users_table

metadata = MetaData()

posts_table = Table(
    "posts",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", ForeignKey(users_table.c.id)),
    Column("created_at", DateTime()),
    Column("title", String(100)),
    Column("content", Text()),
)
