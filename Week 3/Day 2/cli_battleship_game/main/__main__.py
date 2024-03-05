from modules.board import Board
from modules.player import Player
from modules.ship import Ship
import random

def add_5_ships(board):
    elements = []
    for i in range(5):
        for j in range(5):
            elements.append([i,j])
    random_pairs = random.sample(elements, 5)
    for position in random_pairs:
        ship = Ship(position)
        board.add_ship(ship, position)


board = Board()
add_5_ships(board)

player = Player(25)
while player.get_rockets() > 0 and board.get_ships_num() > 0:
    print(player)
    print(board)
    user_input = input("Enter what position to hit\n(format: number number)\n").split()
    position = []
    if len(user_input) > 1:
        if user_input[0][0].isnumeric() and user_input[1][0].isnumeric():
            position = [int(user_input[0][0]), int(user_input[1][0])]
            if position[0] < 5 and position[1] <5:
                player.fire_rocket(position, board)
            else:
                print("The position you entered is outside the board")
        else:
            print("Invalid input")
    else:
        print("Enter input according to aforementioned format")

print(f"The player has sunk {5-board.get_ships_num()} ships")
print(f"Player hit accuracy: {player.get_hits()/(player.get_hits() + player.get_missed())}")
if board.get_ships_num() == 0:
    print("Player win")
else:
    print("CPU win")