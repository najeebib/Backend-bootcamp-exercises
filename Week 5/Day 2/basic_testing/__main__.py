from modules.person import Person
from modules.raffle import Raffle

def main():
    person = Person("person 1")
    raffle = Raffle(5,20,20)
    raffle.buy_ticket(person)
    raffle.buy_ticket(person)
    person2 = Person("person 2")
    raffle.buy_ticket(person2)
    raffle.buy_ticket(person2)
    raffle.buy_ticket(person2)
    raffle.buy_ticket(person2)
    raffle.select_winner()
    raffle.buy_ticket("person2")

if __name__ == "__main__":
    main()