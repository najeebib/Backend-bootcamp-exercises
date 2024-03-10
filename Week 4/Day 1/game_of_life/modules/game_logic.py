from .cell import Cell
from .board import Board
import copy
import logging

def get_rounds_from_user():
    """ Ask the user to enter game's number of rounds and return it """
    while True:
        try:
            rounds_num = int(input(f"Enter the number of rounds you want the game to have\n"))
            if rounds_num > 0:
                return rounds_num
            else:
                print("Enter a positive number")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            logging.warning("Invalid input. Please enter a valid number.")

def get_position_from_user():
    """ Ask the user to enter the positon of the cell that will be made alive and return it """
    while True:
        try:
            row = int(input(f"Enter the number between (0 - 7)\n"))
            column = int(input(f"Enter the number between (0 - 7)\n"))
            if 0 <= row < 8 and 0 <= column < 8 :
                return (row, column)
            else:
                print("Enter numbers the specified range")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            logging.warning("Invalid input. Please enter a valid number.")

def ask_user_enter_cells():
    """ Ask the user to enter if they want to continue to enter cells and return it """
    while True:
        user_input = input(f"Do you want to keep entering cells? (y/n)\n")
        if user_input == "y":
            return True
        elif user_input == "n":
            return False
        else:
            print("Enter y or n")
            logging.warning("Invalid input. Please enter y or n.")

def count_alive_neighbors(board: Board, cell: Cell):
    """ Count the number of alive neighbors that the cell has and return it
    :param board: the game board
    :param cell: the cell we are counting their neighbors
    """
    cell_position = cell.get_position()
    
    count = 0
    for i in range(cell_position[0]-1,cell_position[0]+2):
        for j in range(cell_position[1]-1,cell_position[1]+2):
            if 0 <= i < 8 and 0 <= j < 8:
                neighbor_position = (i, j)
                if neighbor_position != cell_position:
                    neighbor = board.get_cell(neighbor_position)
                    if neighbor.get_status() == "alive":
                        count += 1
    return count

def round(board: Board):
    """ Simulate one game round, check each cell for how many alive neighbors they have and change their stautus according to game rules   
    :param board: the game board
    """
    # here i copy the original board before i change the statuses of the cells so that when i change a cell's status and go to its neighbor i take in account the previous value
    # for example (0,5) is alive = (0,6) has an alive neighbor -> (0,5) is now dead (0,6) will still have one alive neighbor but next round it will not
    # the reason why i did this is for example lets say the player selects (0,5), (0,6) and (0,7) as alive then (0,6) will have two alive neighbors, but when i didn't use a copy (0,5) became dead
    # so when the program reached (0,6) it has only 1 alive neighbor 
    board_copy = copy.deepcopy(board)
    for i in range(8):
        for j in range(8):
            cell = board.get_cell((i, j))
            cell_neighbors = count_alive_neighbors(board=board_copy, cell=cell)
            cell_status = cell.get_status()
            if cell_status == "alive":
                if cell_neighbors < 2 or cell_neighbors > 3:
                    cell.change_status("dead")
            else:
                if cell_neighbors == 3:
                    cell.change_status("alive")
    board.set_cells(board_copy.get_cells()) 