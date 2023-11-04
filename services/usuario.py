from config.db import cnx, meta
from models.usuario import usuarios

def listar_usuarios():
    return cnx.execute(usuarios.select()).fetchall()

def obtener_usuario_x_id(id:int):
    return cnx.execute(usuarios.select().where(usuarios.c.id_usuario == id)).first()