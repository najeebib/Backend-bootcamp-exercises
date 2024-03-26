from ticket import Ticket
import random
import json
class TicketsGenerator:
    def __init__(self) -> None:
        self.path = "./data/tickets.json"
        self.events_list = ["Concert", "Sports Game", "Theater Show", "Movie Premiere"]
        self.price_range = (10, 35)

    def genrate_500_tickets(self):
        tickets = {}
        for event in self.events_list:
             tickets[event] = 0
        for i in range(500):
                price = random.randint(*self.price_range)
                event = random.choice(self.events_list)
                ticket = Ticket(i, price, event)
                tickets[event] += 1
        for i in range(1,3):
             path = f"../data/tickets.json"
             with open(path, 'w') as f:
                  json.dump(tickets, f, indent=2)


if __name__ == "__main__":
     ticket_gen = TicketsGenerator()
     ticket_gen.genrate_500_tickets()