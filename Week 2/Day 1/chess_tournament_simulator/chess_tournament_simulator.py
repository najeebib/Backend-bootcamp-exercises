import random

def get_matchups(players,rounds_num, matches_per_round):
    matchups = []
    for i in range(rounds_num):
        matches = []
        for j in range(matches_per_round):
            player1 = players[j]
            player2 = players[len(players) - 1 - j]
            matches.append([player1,player2])
        matchups.append({"round": i+1,"matches":matches})
        players = [players[0]] + [players[-1]] + players[1:-1]
    return matchups

def odds_of_winning(player1, player2):
    player1_elo = player1["elo"]
    player2_elo = player2["elo"]
    ratio = player1_elo/player2_elo
    revers_ratio = 1 - ratio
    player1_odds = 0.4 - revers_ratio
    return player1_odds
def calculate_elo(player1, player2):
    player1_elo = player1["elo"]
    player2_elo = player2["elo"]
    player1_probability = round((1 - (1/(1+10**((player2_elo-player1_elo) / 400)))) * 20)
    player2_probability = round((1 - (1/(1+10**((player1_elo-player2_elo) / 400)))) * 20)
    return player1_probability, player2_probability

def winner(player1_odds, player1, player2):
    rand = random.random()
    player1_probability, player2_probability = calculate_elo(player1, player2)
    if rand < 0.2:
        print ("Tie")
        player1["total_points"] += 1
        player2["total_points"] += 1
    elif rand < player1_odds + 0.2:
        print(f"{player1['name']} win")
        player1["total_points"] += 3
        player1["elo"] +=  player1_probability
        player2["elo"] -=  player1_probability
    else:
        print(f"{player2['name']} win")
        player2["total_points"] += 3
        player2["elo"] +=  player2_probability
        player1["elo"] -=  player2_probability


players = []
for i in range(4):
    player = {"name": f"player-{i}", "elo": random.randint(1500,2000),"total_points": 0}
    players.append(player)
print(players)
rounds_num = len(players) - 1
matches_per_round =   int(len(players) / 2)
matchups = get_matchups(players, rounds_num, matches_per_round)
for i in range(rounds_num):
    round_matches = matchups[i]["matches"]
    for j in range(matches_per_round):
        player1 = round_matches[j][0]
        player2 = round_matches[j][1]

        player1_odds = odds_of_winning(player1=player1, player2=player2)
        winner(player1_odds, player1, player2)

index = 0
highest_ponts = 0
for i in range(len(players)):
    player = players[i]
    if player["total_points"] > highest_ponts:
        highest_ponts = player["total_points"]
        index = i

print(f"Player: {players[index]['name']} has won the tournament with {highest_ponts} points total.\n")
print(players)