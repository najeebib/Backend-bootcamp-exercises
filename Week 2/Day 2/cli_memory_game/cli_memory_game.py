import random
import os
import time

class Tile:
    def __init__(self, value, position):
        self.value = value
        self.position = position
        self.hidden = True
    # if the user is guessing show the value, otherwise show 0
    def get_value(self, guess=False):
        if self.hidden and not guess:
            return 0
        else:
            return(self.value)
    # change tile status 
    def change_hidden(self, boolean):
        self.hidden = boolean

class Board:
    def __init__(self):
        # list to hold the tiles
        self.tiles = []
        values =  []
        for i in range(18):
            values.append(i)
            values.append(i)
        random.shuffle(values)
        index = 0
        # make a 6x6 board
        for i in range(6):
            for j in range(6):
                position = [i, j]
                value = values[index]
                index += 1
                tile = Tile(value, position)
                self.tiles.append(tile)
    # print the values on board
    def print_board(self):
        for i in range(6):
            for j in range(6):
                tile_num = i * 6 + j
                print(self.tiles[tile_num].get_value(), end=" ")
            print("")
    # the function gets a position [a, b] and returns the value of the tile
    def get_tile(self, position):
        place_in_tiles_list = position[0] * 6 + position[1]
        return self.tiles[place_in_tiles_list]

def main():
    correct_count = 0
    board = Board()
    while correct_count < 18:
        # clear the console
        os.system('cls')
        # print the board
        board.print_board()
        # ask user for first guess
        guess1 = input("Enter a guess (format: number, number. this is guess 1)\n").split()
        # get the position numbers from input
        position1 = []
        if guess1[0][0].isnumeric() and guess1[1][0]:
            position1 = [int(guess1[0][0]), int(guess1[1][0])]
        else:
            print("Enter valid input")
            continue
        tile1 = board.get_tile(position1)
        # show the tile status to show it
        tile1.change_hidden(False)
        os.system('cls')
        board.print_board()
        # ask user for second guess
        guess2 = input("Enter a guess (format: number, number. this is guess 2)\n").split()
        position2 = []
        if guess2[0][0].isnumeric() and guess2[1][0].isnumeric():
            position2 = [int(guess2[0][0]), int(guess2[1][0])]
        else:
            print("Enter valid input")
            continue
        # check if the user entered same position twice
        if position1 != position2:
            # get the value
            value1 = tile1.get_value(True)

            tile2 = board.get_tile(position2)
            tile2.change_hidden(False)
            os.system('cls')
            board.print_board()
            # show the board for 2 seconds
            time.sleep(2)
            value2 = tile2.get_value(True)
            if value1 == value2:
                # increse count by 1
                correct_count += 1
                print("correct guess")
            else:
                # hide the tile if they aren't the same
                tile1.change_hidden(True)
                tile2.change_hidden(True)
                os.system('cls')
                board.print_board()
                time.sleep(2)
                
        else: 
            print("Don't enter same position twice")

    if correct_count == 18:
        print("Congrats you won")

if __name__ == '__main__':   
    main()