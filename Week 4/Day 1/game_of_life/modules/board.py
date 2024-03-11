from .cell import Cell
class Board:
    def __init__(self) -> None:
        """ Construct the board class
        
        initilze the board cells using the Cell class
        make a 8x8 list that will have all cells
        all cells are dead at the begining
        """
        self._cells = [[Cell("dead", (j, i)) for i in range(8)] for j in range(8)]
    def get_cells(self):
        return self._cells
    
    def set_cells(self, cells):
        self._cells = cells
        
    def get_cell(self, position: tuple):
        """ return the cell in the given position, if it is a valid position on the board

        :param position a tuple with two value, the first one is the row and the second one is the column
        """
        if position[0] < 8 and position[0] >= 0 and position[1] < 8 and position[1] >= 0:
            return self._cells[position[0]][position[1]]
        return None
    def get_alive_cells_count(self):
        """ return the number of alive cells on the board """
        count = 0
        for i in range(8):
            for j in range(8):
                cell = self.get_cell((i, j))
                if cell.get_status() == "alive":
                    count += 1
        return count
    def __str__(self) -> str:
        return f"There are {self.get_alive_cells_count()} cells that are alive this round"