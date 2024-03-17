class Player:
    def __init__(self, name: str, favorite_weapons: list):
        """ Initilize the player

        :param name: name of the player
        :param favorite_weapons: a list of strings that has the player's favorite weapons

        class attributes:
        _name: name of the player
        _favorite_weapons: a list of strings that has the player's favorite weapons
        _visited_places: list of strings that has all the places the player visited
        _is_dead: a boolean to check if the player is dead or not
        _is_murderer: a boolean to check if the player is the murderer or not

        class functions:
        each attribute has a get and set method
        __str__: print the object data as a string
        """
        self._name = name
        self._visited_places = []
        self._favorite_weapons = favorite_weapons
        self._is_dead = False
        self._is_murderer = False
    
    def get_name(self):
        return self._name
    
    def get_visited_places(self):
        return self._visited_places
    
    def add_visited_place(self, place: str):
        self._visited_places.append(place)
    
    def get_favorite_weapons(self):
        return self._favorite_weapons
    
    def get_is_dead(self):
        return self._is_dead
    
    def set_is_dead(self):
        self._is_dead = True

    def get_is_murderer(self):
        return self._is_murderer
    
    def set_is_murderer(self):
        self._is_murderer = True

    def __str__(self):
        return f"Player name: {self._name}, visited locations {self._visited_places}, avorite weapons {self._favorite_weapons}, is the player dead?: {self._is_dead}, is the player the murderer?: {self._is_murderer}"