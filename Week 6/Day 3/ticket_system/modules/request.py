class Request:
    def __init__(self, timestamp: str, event: str, number_of_tickets):
        self._timestamp = timestamp
        self._event = event
        self._number_of_tickets = number_of_tickets

    def get_timestamp(self):
        return self._timestamp

    def get_event(self):
        return self._event

    def get_number_of_tickets(self):
        return self._number_of_tickets
    
    def request_json(self):
        request_json = {"timestamp": self._timestamp, "tickets": self._number_of_tickets, "event": self._event}
        return request_json