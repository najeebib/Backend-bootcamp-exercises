class Ticket:
    def __init__(self, id: int, price: int, event: str):
        self._id = id
        self._price = price
        self._event = event
        self._is_sold = False

    def get_id(self):
        return self._id
    
    def get_price(self):
        return self._price
    
    def get_event(self):
        return self._event
    
    def get_is_sold(self):
        return self._is_sold
    
    def set_is_sold(self):
        self._is_sold = True
    