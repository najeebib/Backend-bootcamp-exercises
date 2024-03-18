class Person:
    def __init__(self, name):
        self._num_of_tickets = 0
        self._name = name
    
    def get_num_of_tickets(self):
        return self._num_of_tickets
    
    def get_name(self):
        return self._name
    
    def add_ticket(self):
        self._num_of_tickets += 1