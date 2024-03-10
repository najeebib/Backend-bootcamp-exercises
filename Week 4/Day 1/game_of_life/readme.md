# game of life   

# modules  
## Cell  
A class that will represent a cell on the board  
_status = the status of the cell (alive/dead)  
_position = position of the cell on the board    

## Board  
A class that will represent the board itself  
cells

get_cell(position): return the cell at the given position  
get_alive_cells_count(): return the number of alive cells on board  

## game_logic
A module that has all the function for the game logic  
get_rounds_from_user():  Ask the user to enter game's number of rounds  
get_position_from_user(): Ask the user to enter the positon of the cell  
ask_user_enter_cells(): Ask the user to enter if they want to continue to enter cells  
count_alive_neighbors(board, cell): cont the number of alive neighbor the cell has on board  
round(board): Simulate one game round, check each cell for how many alive neighbors they have and change their stautus according to game rules  


# main
in main ask the user to enter the number of rounds  
Then ask them for which cells they want to be alive   
Then go through each round and change the cells according to the rules  
