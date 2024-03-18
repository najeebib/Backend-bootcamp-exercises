class Person:
    def __init__(self, name):
        """ initilize the person class

            attribute:
            num_of_tickets: number of tickets this person has
            name: name of the person

            class methods:
            get methods for each attribute and an add function to increase ticket count
        """
        self._num_of_tickets = 0
        self._name = name
    
    def get_num_of_tickets(self):
        return self._num_of_tickets
    
    def get_name(self):
        return self._name
    
    def add_ticket(self):
        self._num_of_tickets += 1