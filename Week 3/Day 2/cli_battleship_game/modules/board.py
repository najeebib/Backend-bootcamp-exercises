class Board:
    def __init__(self):
        self.tiles = [[None for i in range(5)] for j in range(5)]
        self.ships = []
        self.tiles_hit = []

    def add_ship(self, ship, position):
        self.tiles[position[0]][position[1]] = ship
        self.ships.append(ship)

    def add_hit_at_position(self, position):
        self.tiles_hit.append(position)

    def get_tile(self, position):
        return self.tiles[position[0]][position[1]]
    
    def get_all_hit_position(self):
        return self.tiles_hit
    
    def get_ships_num(self):
        count = 0
        for ship in self.ships:
            if not ship.get_is_detroyed():
                count += 1
        return count
    
    def __str__(self):
        return f"There are {self.get_ships_num()} ships on the board"