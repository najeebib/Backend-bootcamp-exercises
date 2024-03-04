class Board:
    def __init__(self):
        self.tiles = [[None for i in range(5)] for j in range(5)]
        self.ships = []

    def add_ship(self, ship, position):
        self.tiles[position[0]][position[1]] = ship
    def get_tile(self, position):
        return self.tiles[position[0]][position[1]]