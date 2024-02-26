import random
import os
import time

class Tile:
    def __init__(self, value, position):
        self.value = value
        self.position = position
        self.hidden = True

    def get_value(self, guess=False):
        if self.hidden and not guess:
            return 0
        else:
            return(self.value)

    def change_hidden(self, boolean):
        self.hidden = boolean
class Board:
    def __init__(self):
        self.tiles = []
        values =  []
        for i in range(18):
            values.append(i)
            values.append(i)
        random.shuffle(values)
        index = 0
        for i in range(6):
            for j in range(6):
                position = [i, j]
                value = values[index]
                index += 1
                tile = Tile(value, position)
                self.tiles.append(tile)

    def print_board(self):
        for i in range(6):
            for j in range(6):
                tile_num = i * 6 + j
                print(self.tiles[tile_num].get_value(), end=" ")
            print("")

    def get_tile(self, position):
        place_in_tiles_list = position[0] * 6 + position[1]
        return self.tiles[place_in_tiles_list]
correct_count = 0
board = Board()
while correct_count < 18:
    os.system('cls')
    board.print_board()
    guess1 = input("Enter a guess (format: number, number. this is guess 1)\n").split()
    position1 = [int(guess1[0][0]), int(guess1[1][0])]
    tile1 = board.get_tile(position1)
    tile1.change_hidden(False)
    os.system('cls')
    board.print_board()
    guess2 = input("Enter a guess (format: number, number. this is guess 2)\n").split()
    position2 = [int(guess2[0][0]), int(guess2[1][0])]
    if position1 != position2:
        value1 = tile1.get_value(True)

        tile2 = board.get_tile(position2)
        tile2.change_hidden(False)
        os.system('cls')
        board.print_board()
        time.sleep(2)
        value2 = tile2.get_value(True)
        if value1 == value2:
            correct_count += 1
            print("correct guess")
        else:
            tile1.change_hidden(True)
            tile2.change_hidden(True)
            os.system('cls')
            board.print_board()
            time.sleep(2)
            
    else: 
        print("Don't enter same position twice")

if correct_count == 18:
    print("Congrats you won")