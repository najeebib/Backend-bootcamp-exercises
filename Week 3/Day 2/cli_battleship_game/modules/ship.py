class Ship:
    def __init__(self, position):
        self._position = position
        # boolean for if the ship has been detroyed by player
        self._is_detroyed = False

    def get_is_detroyed(self):
        return self._is_detroyed
    
    def set_is_detroyed(self):
        self._is_detroyed = True