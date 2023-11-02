from config.db import cnx, meta
from models.usuario import usuarios

def listar_usuarios():
    return cnx.execute(usuarios.select()).fetchall()
