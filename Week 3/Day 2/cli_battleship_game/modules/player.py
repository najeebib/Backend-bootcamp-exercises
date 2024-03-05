class Player:
    def __init__(self, rockets=10):
        self._rockets = rockets
        self._hits = 0
        self._missed = 0

    def get_rockets(self):
        return self._rockets
    # fire the rocket at the position player choose
    def fire_rocket(self,position, board):
        hit_positions = board.get_all_hit_position()
        # check if the player already hit this position
        if position in hit_positions:
                print("Can't hit same position twice")
        else:
            board.add_hit_at_position(position)
            ship = board.get_tile(position)
            # check if the position that been hit is a ship or no
            if  ship != None:
                # if it is a ship increas player hits and destroy ship
                self.decrease_rockets()
                self.increase_hits()
                ship.set_is_detroyed()
                print(f"Player hit ship at position {position}")
            else:
                # if it isn't a ship increas player missed
                self.decrease_rockets()
                self.increase_missed()
                print(f"Player missed at position {position}")
    def decrease_rockets(self):
        self._rockets -= 1

    def increase_hits(self):
        self._hits += 1

    def increase_missed(self):
        self._missed += 1

    def get_hits(self):
        return self._hits
    
    def get_missed(self):
        return self._missed
    
    def __str__(self):
        return f"The player has {self._rockets} rockets,  {self._hits} rockets had hit a ship and {self._missed} rockets missed its target"