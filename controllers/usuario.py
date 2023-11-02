# Unificando routas con controladores
from fastapi import APIRouter
# Importando servicios
from services.usuario import listar_usuarios

rutas = APIRouter()

url = "/usuario"

#Create Read Update Delete

@rutas.get(url)
def lista_usuarios():
    resultado = listar_usuarios()
    print(resultado)
    return resultado

@rutas.get(url + "/{id}")
def obtiene_usuario(id:int):
    return {}

@rutas.post(url)
def registra_usuario(elemento:object):
    return {}

@rutas.put(url + "/{id}")
def actualiza_usuario(id:int, elemento:object):
    return {}

@rutas.delete(url + "/{id}")
def elimina_usuario(id:int):
    return {}