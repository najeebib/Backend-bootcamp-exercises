from .ticket import Ticket
import random
import json
class TicketsGenerator:
    def __init__(self) -> None:
        self.path = "./data/tickets.json"
        self.events_list = ["Concert", "Sports Game", "Theater Show", "Movie Premiere"]
        self.price_range = (10, 35)

    def genrate_500_tickets(self):
        with open("../data/tickets.json", 'w') as f:
            tickets = []
            for i in range(500):
                price = random.randint(*self.price_range)
                event = random.choice(self.events_list)
                ticket = Ticket(i, price, event)
                tickets.append(ticket.ticket_json())
            json.dump(tickets, f, indent=2)