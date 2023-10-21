from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"estado": "Funcionando Israel"}


#@app.post("/")

#@app.put("/")

#@app.patch("/")

""" @app.delete("/")
asdsad
asdsa
d
sad
sad
as
dsad
 """