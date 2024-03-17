import logging
class UserInputManager:
    def get_number_of_players():
        """ get the number of players from the user """
        while True:
            try:
                num = int(input(f"Enter the number of players:\n"))
                return num
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                logging.warning("Invalid input. Please enter a valid number.")

    def get_accused_number(limit: int):
        """ get the number of the player they want to accuse """
        while True:
            try:
                command = int(input(f"Enter the number of the player you want to accuse (between 1 - {limit}):\n"))
                if 1 <= command <= limit:
                    return command
                else:
                    print("Enter numbers the specified range")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                logging.warning("Invalid input. Please enter a valid number.")