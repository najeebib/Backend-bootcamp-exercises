from modules.game_manager import GameManager
from modules.game import Game
from modules.player import Player

class TestGameManager:
    def setup_method(self):
        self.game_manager = GameManager()
        self.game = Game()
        self.game.init_game(8)
        self.game_manager.players_visit_random_places(self.game)
        self.murderer = self.game.get_murderer()
        self.murder_place, self.murder_weapon = self.game_manager.murder(self.murderer)
        self.suspects = self.game_manager.suspect(self.game, self.murder_place, self.murder_weapon)
    
    def test_murder(self):
        assert self.murder_place in self.murderer.get_visited_places() and self.murder_weapon in self.murderer.get_favorite_weapons()


    def test_suspect(self):
        assert type(self.game_manager.suspect(self.game, self.murder_place, self.murder_weapon)) == list

    def test_suspect_len(self):
        assert len(self.game_manager.suspect(self.game, self.murder_place, self.murder_weapon)) == 2

    def test_murderer_in_list(self):
        assert self.murderer in self.game_manager.suspect(self.game, self.murder_place, self.murder_weapon)

    def test_accuse_player(self):
        assert type(self.game_manager.accuse_player(self.suspects)) == Player
    
    def test_accuse_player_in_list(self):
        assert self.game_manager.accuse_player(self.suspects) in self.suspects
