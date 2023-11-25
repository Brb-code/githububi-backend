from config.db import engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuario"
    id_usuario = Column("id_usuario", Integer, primary_key=True)
    nombre = Column("nombre", String(150), nullable=False)
    password = Column("password", String(255), nullable=False)
    email = Column("email", String(150))
    cuenta_github = Column("cuenta_github", String(100))
    celular = Column("celular", String(20))

Base.metadata.create_all(engine)