import random
def getDamageMultiplier(atacker_type, defender_type):
    damage_multiplier = 1
    match atacker_type:
        case "water":
            if defender_type == "fire" or defender_type == "earth":
                damage_multiplier = 2
        case "fire":
            if defender_type == "water" or defender_type == "wind":
                damage_multiplier = 2
        case "earth":
            if defender_type == "fire" or defender_type == "wind":
                damage_multiplier = 2
        case "wind":
            if defender_type == "water":
                damage_multiplier = 2
    return damage_multiplier

def atack(attacker,defender, attacker_random_num):
    damage_multiplier = getDamageMultiplier(attacker["type"],defender["type"])
    damage = damage_multiplier * (attacker_random_num + attacker["strength"])
    defender["life"] -= damage
    if defender["life"] < 0:
        defender["life"] = 0
    print(f"{attacker['name']} atacks {defender['name']}. deals {damage} damage. {defender['name']} now has {defender['life']} amount of life after the attack")

def joinFight(player_pokemons, player_pokemon_index, player_pokemon_alive):
    player_pokemon = player_pokemons[player_pokemon_index]
    print(f"{player_pokemon['name']} has joined the fight")
    return player_pokemon

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

player1_pokemon_index = random.randint(0, 4)
player2_pokemon_index = random.randint(0, 4)

pokemon1 = joinFight(player1_pokemons, player1_pokemon_index, player1_pokemon_alive)
pokemon2 = joinFight(player2_pokemons, player2_pokemon_index, player2_pokemon_alive)
while player1_pokemon_alive > 0 and player2_pokemon_alive > 0:
    player1_rand_num = random.randint(1,20)
    player2_rand_num = random.randint(1,20)
    pokemon1 = player1_pokemons[player1_pokemon_index]
    pokemon2 = player2_pokemons[player2_pokemon_index]

    pokemon1_score= player1_rand_num + pokemon1["speed"]
    pokemon2_score= player2_rand_num + pokemon2["speed"]
    
    if pokemon1_score > pokemon2_score:
        #pokemon 1 start first
        atack(pokemon1,pokemon2,player1_rand_num)
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
        atack(pokemon2,pokemon1,player2_rand_num)
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