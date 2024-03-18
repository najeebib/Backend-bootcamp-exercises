from .person import Person
import random
class Raffle:
    def __init__(self, max_people, max_tickets, ticket_price):
        self._people = []
        self._tickets = 0
        self._max_people = max_people
        self._max_tickets = max_tickets
        self._total_earnings = 0
        self._ticket_price = ticket_price 

    def get_people(self):
        return self._people
    
    def get_tickets(self):
        return self._tickets
    
    def get_max_people(self):
        return self._max_people
    
    def get_max_tickets(self):
        return self._max_tickets
    
    def get_total_earnings(self):
        return self._total_earnings
    
    def get_ticket_price(self):
        return self._ticket_price
    
    def buy_ticket(self, person: Person):
        if type(person) != Person:
            raise TypeError
        
        if self._tickets < self._max_tickets:
            person.add_ticket()
            if not person in self._people:
                self._people.append(person)
            self._tickets += 1
            self._total_earnings += self._ticket_price
        else:
            print("No more tickets left")

    def select_winner(self):
        if not self._people:
            print("No participants in the raffle")
            return None
        
        all_tickets = []
        for person in self._people:
            num_tickets = person.get_num_of_tickets()
            all_tickets.extend([person] * num_tickets)
        winner = random.choice(all_tickets)
        print(f"The winner is {winner.get_name()}")
        return winner