from config.db import meta, engine
from sqlalchemy import Table, Column, Integer, String

usuarios = Table(
    "usuario",
    meta,
    Column("id_usuario", Integer, primary_key=True),
    Column("nombre", String(150), nullable=False),
    Column("password", String(255), nullable=False),
    Column("email", String(150)),
    Column("cuenta_github", String(100)),
    Column("celular", String(20))
)

meta.create_all(engine)