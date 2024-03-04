class Ship:
    def __init__(self, position):
        self.position = position
        self.is_destroyed  = False

    def set_destroyed(self):
        self.is_destroyed = True