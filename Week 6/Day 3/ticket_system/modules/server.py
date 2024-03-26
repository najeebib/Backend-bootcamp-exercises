import time
import json
from .request import Request
class Server:
    def __init__(self, tickets_file, requests_threshold_delay=2, max_concurrent_requests=3):
        with open(tickets_file, 'r') as f:
            self.tickets_db = json.load(f)
        self.requests_time = time.time()
        self.requests_threshold_delay = requests_threshold_delay
        self.max_concurrent_requests = max_concurrent_requests
        self.current_concurrent_requests = 0
    
    def sell_ticket(self, event, num_of_tickets):
        if event not in self.tickets_db or (self.tickets_db[event] - num_of_tickets) <= 0:
            print(f"No tickets available for {event}.")
            return False
        if self.current_concurrent_requests >= self.max_concurrent_requests:
            raise Exception("Server overloaded. Please try again later.")
        self.tickets_db[event] -= num_of_tickets
        print(f"Sold {num_of_tickets} ticket for {event}. Remaining: {self.tickets_db[event]}")
        return True

    def show_unsold_tickets(self):
        print("Unsold tickets:")
        for event, tickets in self.tickets_db.items():
            if tickets > 0:
                print(f"{event}: {tickets} tickets available.")

    def process_request(self, request: Request):
        # Check if the number of requests exceeds the threshold
        if self.current_concurrent_requests > self.max_requests_per_time:
            current_time = time.time()
            elapsed_time = current_time - self.requests_time
            if elapsed_time < 10:  # Y time unit (adjust as needed)
                print("Too many requests. Delaying response.")
                time.sleep(self.requests_threshold_delay)
            else:
                self.requests_time = current_time
        self.current_concurrent_requests += 1
        # Simulate processing time
        time.sleep(0.5)
        self.sell_ticket(request.get_event(), request.get_number_of_tickets())
        self.current_concurrent_requests -= 1