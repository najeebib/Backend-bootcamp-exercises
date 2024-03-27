import random
import time
from .request import Request
class RequestGenerator:
    def __init__(self):
        self.events_range = (1, 5)  # Range of events to generate
        self.time_range = (0.5, 2)  # Range of time intervals between event generation (in seconds)
        self.event_list = ["Concert", "Sports Game", "Theater Show", "Movie Premiere"]
    def remove_event(self, event: str):
        self.event_list.remove(event)
    def generate_requests(self):
        while True:
            num_events = random.randint(*self.events_range)
            for _ in range(num_events):
                if len(self.event_list) == 0:
                    return
                timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
                event = random.choice(self.event_list)
                tickets = random.randint(1, 10)  # Assuming a ticket range from 1 to 10
                request = Request(timestamp, event, tickets)
                yield request
            time.sleep(random.uniform(*self.time_range))