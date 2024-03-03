class SpaceShip:
    def __init__(self, name, fuel, health):
        self.__name = name
        self.__fuel = fuel
        self.__health = health
    
    def __str__(self):
        return f"The spaceship name is {self.get_name()}, current fuel: {self.get_fuel()}, current health: {self.get_health()}"

    def get_name(self):
        return self.__name
    
    def get_fuel(self):
        return self.__fuel
    
    def get_health(self):
        return self.__health
    
    def set_fuel(self, fuel):
        self.__fuel = fuel

    def set_health(self, health):
        self.__health = health