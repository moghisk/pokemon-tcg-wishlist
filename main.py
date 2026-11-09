from fastapi import FastAPI

app = FastAPI(title="Pokémon TCG Wishlist")

@app.get("/")
def raiz():
    return {"mensagem": "API funcionando!"}

@app.get("/saude")
def saude():
    return {"status": "ok"}