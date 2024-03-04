class Player:
    def __init__(self, rockets=10):
        self._rockets = rockets
        self._hits = 0
        self._missed = 0

    def fire_rocket(self,position, board):
        if board.get_tile(position) != None:
            ship = board.get_tile(position)
            ship.set_destroyed()
            self.decrease_rockets()
            self.increase_hits()
            print(f"Player hit ship at position {position}")
        else:
            self.decrease_rockets()
            self.increase_missed()
            print(f"Player missed at position {position}")

    def decrease_rockets(self):
        self.rockets -= 1

    def increase_hits(self):
        self.hits += 1

    def increase_missed(self):
        self.missed += 1

    def __str__(self):
        return f"The player has {self._rockets},  {self._hits} had hit a ship and {self._missed} missed its target"