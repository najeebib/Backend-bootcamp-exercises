from .player import Player
import random

class Game:
    def __init__(self):
        """ initilze the game class

        class attributes:
        _places: list of strings that has all the places in the game
        _weapons: list of strings that has all the weapons in the game
        _players: list of objects type Player that has all the players in the game

        class methods:
        for each attribute there is a get method as well as a function that adds a place/weapon/player to the list
        get_murderer: return the player object of the murderer
        """
        self._places = []
        self._weapons = []
        self._players = []
    
    def get_places(self):
        return self._places
    
    def get_weapons(self):
        return self._weapons
    
    def get_players(self):
        return self._players
    
    def add_place(self, place: str):
        self._places.append(place)

    def add_weapon(self, weapon: str):
        self._weapons.append(weapon)

    def add_player(self, player: Player):
        self._players.append(player)

    def get_murderer(self):
        for player in self._players:
            if player.get_is_murderer():
                return player
        return None
    
    def init_game(self, number_of_players):
        """ this function initilizes the game

        it generates 20 random places and 10 random guns, a X number of players (X is given by the user)
        the function then generate that amount of players with a random name and random weapons from the weapons list
        then the function chooses a random player and makes them the murderer
        """

        # todo: add places and weapons from text files instead of randomly generated values

        for i in range(20):
            place = f"place-{i+1}"
            self.add_place(place)

        for i in range(10):
            weapon = f"weapon-{i+1}"
            self.add_weapon(weapon)

        weapons = self.get_weapons()
        for i in range(number_of_players):
            name = f"Player-{i+1}"
            random_number_of_weapons = random.randint(1,3)
            favorite_weapons = random.choices(weapons, k=random_number_of_weapons)
            player = Player(name, favorite_weapons)
            self.add_player(player)

        players = self.get_players()
        random_murdered_index = random.randint(0,len(players)-1)
        players[random_murdered_index].set_is_murderer()