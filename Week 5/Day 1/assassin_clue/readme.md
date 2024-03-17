# Assassin Clue Game

Assassin Clue is a text-based murder mystery game inspired by the board game Clue and the video game Among Us. In this game, players move around different locations, collect weapons, and try to identify the murderer among them.

## Modules

### `__main.py__`

This module contains the main game loop and orchestrates the gameplay. It interacts with the user through the console, manages the game state, and controls the flow of the game.

### `game.py`

#### Classes:
- **Game:** Represents the game environment.
  - **Attributes:**
    - `_places`: List of strings containing all the places in the game.
    - `_weapons`: List of strings containing all the weapons in the game.
    - `_players`: List of Player objects representing all the players in the game.
  - **Methods:**
    - `get_places()`: Returns the list of places.
    - `get_weapons()`: Returns the list of weapons.
    - `get_players()`: Returns the list of players.
    - `add_place(place: str)`: Adds a new place to the game.
    - `add_weapon(weapon: str)`: Adds a new weapon to the game.
    - `add_player(player: Player)`: Adds a new player to the game.
    - `get_murderer()`: Returns the player object of the murderer, if any.

### `hame_manager.py`

#### Classes:
- **GameManager:** Manages player actions and game events.
  - **Methods:**
    - `players_visit_random_places(game: Game)`: Assigns random places for players to visit.
    - `murder(murderer: Player)`: Simulates a murder event and returns the murder place and weapon.
    - `suspect(game: Game, murder_place: str, murder_weapon: str)`: Identifies potential suspects based on the murder place and weapon.
    - `accuse_player(suspects: list)`: Prompts the user to accuse a player and handles the outcome.

### `player.py`

#### Classes:
- **Player:** Represents a player in the game.
  - **Attributes:**
    - `_name`: Name of the player.
    - `_visited_places`: List of strings containing all the places visited by the player.
    - `_favorite_weapons`: List of strings containing the player's favorite weapons.
    - `_is_dead`: Boolean indicating whether the player is dead or alive.
    - `_is_murderer`: Boolean indicating whether the player is the murderer.
  - **Methods:**
    - `get_name()`: Returns the player's name.
    - `get_visited_places()`: Returns the list of visited places.
    - `add_visited_place(place: str)`: Adds a visited place to the player's list.
    - `get_favorite_weapons()`: Returns the list of favorite weapons.
    - `get_is_dead()`: Returns True if the player is dead, False otherwise.
    - `set_is_dead()`: Sets the player's status to dead.
    - `get_is_murderer()`: Returns True if the player is the murderer, False otherwise.
    - `set_is_murderer()`: Sets the player as the murderer.

### `user_input.py`

#### Classes:
- **UserInputManager:** Handles user input validation and retrieval.
  - **Methods:**
    - `get_number_of_players()`: Prompts the user to enter the number of players.
    - `get_accused_number(limit: int)`: Prompts the user to enter the number of the player they want to accuse.
