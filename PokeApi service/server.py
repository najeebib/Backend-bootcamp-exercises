from fastapi import FastAPI,APIRouter, HTTPException, Depends, Request
import requests
from routes import routes
import uvicorn
app = FastAPI()

app.include_router(routes.router)

@app.middleware("http")
async def log_req(request:Request, call_next):
    print(f'got req. to: {request.url}, method: {request.method}')
    response = await call_next(request)

    return response

@app.get("/")
def root():
    return "hi from fast api"

@app.get('/pokemon/{name}')
def get_pokemon(name:str):
    # todo: add async await to this, read HTTPX docoummentation and how to do it
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}")

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Couldn't retrieve pokemon")
    
    data = response.json()

    pokemon_info = {
        "name": data["name"].capitalize(),
        "id": data["id"],
        "types": [type_data["type"]["name"] for type_data in data["types"]],
        "abilities": [ability_data["ability"]["name"] for ability_data in data["abilities"]],
        "moves": [moves_data["move"]["name"] for moves_data in data["moves"]],
        "species": data["species"]["name"],
        "stats": {
            "hp":  data["stats"][0]["base_stat"],
            "attack":  data["stats"][1]["base_stat"],
            "defense":  data["stats"][2]["base_stat"],
            "special-attack":  data["stats"][3]["base_stat"],
            "special-defense":  data["stats"][4]["base_stat"],
            "speed":  data["stats"][5]["base_stat"],

        }
    }

    return pokemon_info
