# Unificando routas con controladores
from fastapi import APIRouter, Depends
# Importando servicios
from services.usuario import listar, obtener_x_id, crear, actualizar, eliminar, login
from common.res import verificar_token

rutas = APIRouter()

url = "/usuario"

#Create Read Update Delete

@rutas.get(url,
           response_model=[])
def lista_usuarios():
    resultado = listar()
    return resultado
    
@rutas.get(url + "/{id}")
def obtiene_usuario(id:str, token_usuario:str = Depends(verificar_token)):
    if token_usuario:
        resultado = obtener_x_id(int(id))
        return resultado
    else:
        return False

@rutas.post(url)
def registra_usuario(nombre:str, password:str, email:str, cuenta_github:str, celular:str):
    resultado = crear(nom=nombre, passw=password, ema=email, git=cuenta_github,cel=celular)
    return resultado

@rutas.put(url + "/{id}")
def actualiza_usuario(id:int, nombre:str, password:str, email:str, cuenta_github:str, celular:str):
    resultado = actualizar(int(id), nom=nombre, passw=password, ema=email, git=cuenta_github,cel=celular)
    return resultado

@rutas.delete(url + "/{id}")
def elimina_usuario(id:int):
    resultado = eliminar(int(id))
    return resultado

@rutas.post(url + "/login")
def iniciar_sesion(nombre:str, password:str):
    resultado = login(nombre=nombre, passw=password)
    if resultado:
        return {"token": resultado.id_usuario}
    else:
        return {"token": None}