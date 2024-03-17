from modules.user_input import UserInputManager
from modules.game import Game
from modules.game_manager import GameManager
import random

def main():
    game = Game()
    number_of_players = UserInputManager.get_number_of_players()
    game.init_game(number_of_players)
    dead_players = 0
    murderer_found = False
    try:
        while dead_players < number_of_players - 1:
            # move the players to random places
            GameManager.players_visit_random_places(game)
            
            # get the murderer
            murderer = game.get_murderer()
            # check if the function returns the murderer properly
            if murderer is None:
                raise TypeError
            else:
                # get the murder place and weapon
                murder_place, murder_weapon = GameManager.murder(murderer)
                # generate the suspects list
                suspects_list = GameManager.suspect(game, murder_place, murder_weapon)
                random.shuffle(suspects_list)
                # ask user to choose which player to accuse
                accused_player = GameManager.accuse_player(suspects_list)
                dead_players += 1

                if accused_player.get_is_murderer():
                    print("The murdered has been found, good job")
                    murderer_found = True
                    break
                else:
                    print(f"The player {accused_player.get_name()} was not the murderer")
      
        if murderer_found:
            print("You have won the game")
        else:
            print("The murderer won the game")
    except TypeError:
            print("Error: there is no murderer")  
        

if __name__ == "__main__":
    main()