from fastapi import FastAPI

app = FastAPI()

animes = [
    {
        "id": 1,
        "nome": "Death Note",
        "genero": "Investigação"
    },
    {
        "id": 2,
        "nome": "Demons of shadow halm",
        "genero": "Ação"
    }
]

# rota inicial
@app.get("/")
def home():
    return {"mensagem": "API de animes funcionando!"}

# listar animes
@app.get("/animes")
def listar_animes():
    return animes

# buscar anime por id
@app.get("/animes/{anime_id}")
def buscar_anime(anime_id: int):

    for anime in animes:
        if anime["id"] == anime_id:
            return anime

    return {"erro": "Anime não encontrado"}

# criar anime
@app.post("/animes")
def criar_anime(anime: dict):

    animes.append(anime)

    return {
        "mensagem": "Anime criado com sucesso",
        "anime": anime
    }

# atualizar anime
@app.put("/animes/{anime_id}")
def atualizar_anime(anime_id: int, anime_atualizado: dict):

    for anime in animes:

        if anime["id"] == anime_id:

            anime["nome"] = anime_atualizado["nome"]
            anime["genero"] = anime_atualizado["genero"]

            return {
                "mensagem": "Anime atualizado com sucesso"
            }

    return {"erro": "Anime não encontrado"}

# deletar anime
@app.delete("/animes/{anime_id}")
def deletar_anime(anime_id: int):

    for anime in animes:

        if anime["id"] == anime_id:

            animes.remove(anime)

            return {
                "mensagem": "Anime deletado com sucesso"
            }

    return {"erro": "Anime não encontrado"}