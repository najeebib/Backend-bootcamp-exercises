from fastapi import APIRouter, HTTPException, Depends, Request
import httpx

router = APIRouter()

@router.get('/pokemon/{name}')
async def get_pokemon(name:str):
    async with httpx.AsyncClient() as client:

        response = await client.get(f"https://pokeapi.co/api/v2/pokemon/{name.lower()}")
        if response.status_code != 200:
                    raise HTTPException(status_code=response.status_code, detail="Pokemon not found")
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
    
