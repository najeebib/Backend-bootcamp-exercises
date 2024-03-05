class Board:
    def __init__(self):
        # the board tiles
        self.tiles = [[None for i in range(5)] for j in range(5)]
        # all the ships on the board
        self.ships = []
        # what tiles have been hit by player
        self.tiles_hit = []
    # add a ship onto the board
    def add_ship(self, ship, position):
        self.tiles[position[0]][position[1]] = ship
        # add the ship to ships list
        self.ships.append(ship)
    # add the position the player hit to list
    def add_hit_at_position(self, position):
        self.tiles_hit.append(position)
    # return what is on the tile hit
    def get_tile(self, position):
        return self.tiles[position[0]][position[1]]
    # return all position that been hit
    def get_all_hit_position(self):
        return self.tiles_hit
    # count the ships on board
    def get_ships_num(self):
        count = 0
        for ship in self.ships:
            if not ship.get_is_detroyed():
                count += 1
        return count
    
    def __str__(self):
        return f"There are {self.get_ships_num()} ships on the board"