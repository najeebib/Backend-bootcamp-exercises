from modules.board import Board
from modules.player import Player
from modules.ship import Ship
import random
# add 5 ships to the board
def add_5_ships(board):
    elements = []
    # choose 5 random locations on the board
    for i in range(5):
        for j in range(5):
            # generate all possible position in a 5*5 board
            elements.append([i,j])
    # choose 5 random position
    random_pairs = random.sample(elements, 5)
    # add them to board
    for position in random_pairs:
        ship = Ship(position)
        board.add_ship(ship, position)


board = Board()
add_5_ships(board)

player = Player(10)
# keep the game going untill all ships are detroyed or player ran out of rockets
while player.get_rockets() > 0 and board.get_ships_num() > 0:
    print(player)
    print(board)
    # ask the player to enter what position to hit
    user_input = input("Enter what position to hit\n(format: number number)\n").split()
    position = []
    # check if the user entered an empty input or not enough numbers
    if len(user_input) > 1:
        # check if the user entered numbers
        if user_input[0][0].isnumeric() and user_input[1][0].isnumeric():
            position = [int(user_input[0][0]), int(user_input[1][0])]
            # check if the numbers entered are valid positions on the board
            if position[0] < 5 and position[1] <5 and position[1] >= 0 and position[0] >= 0:
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