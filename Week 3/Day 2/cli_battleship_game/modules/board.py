class Board:
    def __init__(self):
        self.tiles = [[None for i in range(5)] for j in range(5)]
        self.ships = []
        self._ships_num = 5
        self.tiles_hit = []

    def add_ship(self, ship, position):
        self.tiles[position[0]][position[1]] = ship

    def add_hit_at_position(self, position):
        self.tiles_hit.append(position)

    def get_tile(self, position):
        return self.tiles[position[0]][position[1]]
    
    def get_all_hit_position(self):
        return self.tiles_hit
    
    def get_ships_num(self):
        return self._ships_num
    
    def decrease_ships_num(self):
        self._ships_num -= 1

    def __str__(self):
        return f"There are {self._ships_num} ships on the board"