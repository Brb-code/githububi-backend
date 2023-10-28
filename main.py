from fastapi import FastAPI

# Importando rutas y controladores
import controllers.usuario as usuarioController

app = FastAPI()

@app.get("/")
def test():
    return {"estado": "Funcionando Israel"}

app.include_router(usuarioController.rutas)
