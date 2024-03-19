from modules.player import Player
class TestPlayer:
    def setup_method(self):
        self.player = Player("person 1" , ["knife", "dagger"])

    def test_get_name(self):
        assert self.player.get_name() == "person 1"
    
    def test_get_name_type(self):
        assert type(self.player.get_name()) == str
    
    def test_get_visited_places_type(self):
        assert type(self.player.get_visited_places()) == list

    def test_get_visited_places(self):
        assert self.player.get_visited_places() == []

    def test_add_visited_place(self):
        self.player.add_visited_place("Haifa")

        assert self.player.get_visited_places() == ["Haifa"]
        
    def test_get_favorite_weapons_type(self):
        assert type(self.player.get_favorite_weapons()) == list

    def test_get_favorite_weapons(self):
        assert self.player.get_favorite_weapons() == ["knife", "dagger"]

    def test_get_is_dead(self):
        assert self.player.get_is_dead() == False

    def test_set_is_dead(self):
        self.player.set_is_dead()
        assert self.player.get_is_dead() == True

    def test_get_is_murderer(self):
        assert self.player.get_is_murderer() == False

    def test_set_is_murderer(self):
        self.player.set_is_murderer()
        assert self.player.get_is_murderer() == True
