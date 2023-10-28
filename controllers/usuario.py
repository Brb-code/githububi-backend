# Unificando routas con controladores
from fastapi import APIRouter

rutas = APIRouter()

url = "/usuario"

#Create Read Update Delete

@rutas.get(url)
def lista_usuarios():
    return []

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