from fastapi import FastAPI

app = FastAPI(title="Pokémon TCG Wishlist")

@app.get("/")
def raiz():
    return {"mensagem": "API funcionando!"}