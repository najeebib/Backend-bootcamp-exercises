from .player import Player
from .game import Game
from modules.user_input import UserInputManager
import logging
import random

class GameManager:
    def players_visit_random_places(game: Game):
        """ each round each player visits 1-3 places, this functions adds for each player 1-3 random visited places """
        players = game.get_players()
        places = game.get_places()
        # add to each player new visited places
        for player in players:
            if not player.get_is_dead():
                # choose random places
                number_of_places = random.randint(1,3)
                new_places = random.choices(places, k=number_of_places)
                # add each place to player
                for place in new_places:
                    player.add_visited_place(place)

    def murder(murderer: Player):
        """ a murder happens on one of the places that the murderer visited with one of their favorit weapons
            this function gets the murderer and return a random place they visited that the murder took place at and a random weapon that was used for the murder
        """
        visited_places = murderer.get_visited_places()
        favorite_weapons = murderer.get_favorite_weapons()
        murder_place = random.choice(visited_places)
        murder_weapon = random.choice(favorite_weapons)
        print(f"A murder has happend in {murder_place}, murder weapon is {murder_weapon}")

        return murder_place, murder_weapon

    def suspect(game: Game, murder_place: str, murder_weapon: str):
        """ the place of the murder and weapon are given, the function will generate a list of all suspected player 
            a suspect is a player that visited the place where the murder took place and has the murder weapon as one of their favorite weapons
        """
        suspects = []
        players = game.get_players()
        for player in players:
            # check if the player visited the murder place and has the murder weapon as one of their favorite weapons
            if murder_place in player.get_visited_places() and murder_weapon in  player.get_favorite_weapons() and not player.get_is_dead():
                suspects.append(player)
        if len(suspects) < 2:
            # if there is only one suspect add a random player to suspect list
            while True:
                random_player = random.choice(players)
                if not random_player in suspects:
                    suspects.append(random_player)
                    break
        if len(suspects) == 2:
            return suspects
        return random.choices(suspects, k=2)
        
    def accuse_player(suspects: list):
        """ get the list of suspects and ask the user to choose which one to acuse
            when a player is accused they are killed (by ejecting them from the ship like in Among us)
        """
        num_of_suspects = len(suspects)
        for i in range(num_of_suspects):
            # print all suspects data
            suspect = suspects[i]
            places_visited = suspect.get_visited_places()
            favorite_weapons = suspect.get_favorite_weapons()
            two_places = random.choices(places_visited, k=2)
            one_weapon = random.choices(favorite_weapons, k=1)[0]
            name = suspect.get_name()
            print(f"Suspect number {i + 1} name: {name}, visited places: {two_places} and favorite weapon: {one_weapon}")
            
        accused_number = UserInputManager.get_accused_number(num_of_suspects)
        accused_player = suspects[accused_number - 1]
        accused_player.set_is_dead()
        print(f"Player: {accused_player.get_name()} has been accused of being the murderer, they were ejected from the station")

        return accused_player