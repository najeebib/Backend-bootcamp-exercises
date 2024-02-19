import random

player1_pokemons = [
    {"name": "Charizard", "level": 35, "strength": 8, "speed": 4, "type": "fire", "life": 120},
    {"name": "Blastoise", "level": 40, "strength": 7, "speed": 3, "type": "water", "life": 120},
    {"name": "Venusaur", "level": 38, "strength": 6, "speed": 2, "type": "earth", "life": 120},
    {"name": "Pidgeot", "level": 32, "strength": 5, "speed": 5, "type": "wind", "life": 120},
    {"name": "Gyarados", "level": 45, "strength": 9, "speed": 1, "type": "water", "life": 120}
]
player2_pokemons = [
    {"name": "Arcanine", "level": 42, "strength": 9, "speed": 3, "type": "fire", "life": 120},
    {"name": "Vaporeon", "level": 37, "strength": 8, "speed": 4, "type": "water", "life": 120},
    {"name": "Rhydon", "level": 39, "strength": 7, "speed": 2, "type": "earth", "life": 120},
    {"name": "Dragonite", "level": 50, "strength": 10, "speed": 5, "type": "wind", "life": 120},
    {"name": "Lapras", "level": 44, "strength": 6, "speed": 1, "type": "water", "life": 120}
]
player1_pokemon_alive = len(player1_pokemons)
player2_pokemon_alive = len(player2_pokemons)
player1_pokemon_index = random.randint(0,4)
player2_pokemon_index = random.randint(0,4)
print(f"Pokemon1 {player1_pokemons[player1_pokemon_index]['name']} has joined the fight")
print(f"Pokemon2 {player2_pokemons[player2_pokemon_index]['name']} has joined the fight")
while player1_pokemon_alive > 0 and player2_pokemon_alive > 0:
    player1_rand_num = random.randint(1,20)
    player2_rand_num = random.randint(1,20)
    pokemon1 = player1_pokemons[player1_pokemon_index]
    pokemon2 = player2_pokemons[player2_pokemon_index]

    pokemon1_score= player1_rand_num + pokemon1["speed"]
    pokemon2_score= player2_rand_num + pokemon2["speed"]
    
    if pokemon1_score > pokemon2_score:
        #pokemon 1 start first
        damage_multiplier = 1
        type2 = pokemon2["type"]
        match pokemon1["type"]:
            case "water":
                if type2 == "fire" or type2 == "earth":
                    damage_multiplier = 2
            case "fire":
                if type2 == "water" or type2 == "wind":
                    damage_multiplier = 2
            case "earth":
                if type2 == "fire" or type2 == "wind":
                    damage_multiplier = 2
            case "wind":
                if type2 == "water":
                    damage_multiplier = 2
        damage = damage_multiplier * (player1_rand_num + pokemon1["strength"])
        pokemon2["life"] -= damage
        if pokemon2["life"] < 0:
            pokemon2["life"] = 0
        print(f"{pokemon1['name']} atacks {pokemon2['name']}. deals {damage} damage. {pokemon2['name']} now has {pokemon2['life']} amount of life after the attack")
        if pokemon2["life"] <= 0:
            print(f"Pokemon2: {pokemon2['name']} has died")
            player2_pokemons.pop(player2_pokemon_index)
            if len(player2_pokemons) == 0:
                player2_pokemon_alive = 0
            else:
                player2_pokemon_index = random.randint(0,len(player2_pokemons)-1)
                player2_pokemon_alive -=1
                pokemon2 = player2_pokemons[player2_pokemon_index]
                print(f"Pokemon2: {pokemon2['name']} joined the fight")
    elif pokemon1_score < pokemon2_score:
        #pokemon 2 start first
        damage_multiplier = 1
        type1 = pokemon1["type"]
        match pokemon2["type"]:
            case "water":
                if type1 == "fire" or type1 == "earth":
                    damage_multiplier = 2
            case "fire":
                if type1 == "water" or type1 == "wind":
                    damage_multiplier = 2
            case "earth":
                if type1 == "fire" or type1 == "wind":
                    damage_multiplier = 2
            case "wind":
                if type1 == "water":
                    damage_multiplier = 2
        damage = damage_multiplier * (player2_rand_num + pokemon2["strength"])
        pokemon1["life"] -= damage
        if pokemon1["life"] < 0:
            pokemon1["life"] = 0
        print(f"{pokemon2['name']} atacks {pokemon1['name']}. deals {damage} damage. {pokemon1['name']} now has {pokemon1['life']} amount of life after the attack")
        if pokemon1["life"] == 0:
            print(f"Pokemon1: {pokemon1['name']} has died")
            player1_pokemons.pop(player1_pokemon_index)
            if len(player1_pokemons) == 0:
                player1_pokemon_alive = 0
            else:
                player1_pokemon_index = random.randint(0,len(player1_pokemons)-1)
                player1_pokemon_alive -=1
                pokemon1 = player1_pokemons[player1_pokemon_index]
                print(f"Pokemon1: {pokemon1['name']} joined the fight")
    else:
        pass
if player2_pokemon_alive == 0 and player1_pokemon_alive > 0:
    print("Player 1 has won")
else:
    print("Player 2 has won")