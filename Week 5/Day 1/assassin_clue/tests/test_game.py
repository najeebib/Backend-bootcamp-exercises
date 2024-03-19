from modules.game import Game
from modules.player import Player

class TestGame:
    def setup_method(self):
        self.game = Game()

    def test_get_places(self):
        assert type(self.game.get_places()) == list

    def test_get_places_type(self):
        assert self.game.get_places() == []

    def test_add_place(self):
        self.game.add_place("haifa")
        assert self.game.get_places() == ["haifa"]

    def test_get_weapons(self):
        assert type(self.game.get_weapons()) == list

    def test_get_weapons_type(self):
        assert self.game.get_weapons() == []

    def test_add_weapon(self):
        self.game.add_weapon("knife")
        assert self.game.get_weapons() == ["knife"]

    def test_get_players(self):
        assert type(self.game.get_players()) == list

    def test_get_players_type(self):
        assert self.game.get_players() == []

    def test_add_player(self):
        person = Player("person 1", ["knife"])
        self.game.add_player(person)
        assert self.game.get_players() == [person]