from config.db import session
from models.usuario import Usuario

def listar():    
    lista = session.query(Usuario)
    return lista.all()

def obtener_x_id(id:int):
    one = session.query(Usuario).filter(Usuario.id_usuario == id)
    return one.first()

def crear(nom:str, passw:str, ema:str, git:str, cel:str):
    tmp = Usuario(nombre = nom, password=passw, email=ema, cuenta_github=git, celular=cel)
    session.add(tmp)
    session.commit()
    session.refresh(tmp)
    return tmp

def actualizar(id:int, nom:str, passw:str, ema:str, git:str, cel:str):
    tmp = obtener_x_id(id)
    if tmp:
        tmp.nombre = nom
        tmp.password = passw
        tmp.email = ema
        tmp.cuenta_github = git
        tmp.celular = cel
        session.add(tmp)
        session.commit()
        return {"respuesta":True}
    else:
        return {"respuesta":False}

def eliminar(id:int):
    tmp = obtener_x_id(id)
    if tmp:
        session.delete(tmp)
        session.commit()
        return {"respuesta":True}
    else:
        return {"respuesta":False}
    
def login(nombre:str, passw: str):
    one = session.query(Usuario).filter(Usuario.nombre == nombre and Usuario.password == passw)
    return one.first()