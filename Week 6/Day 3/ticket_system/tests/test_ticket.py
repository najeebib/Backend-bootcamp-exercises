from modules.ticket import Ticket
class TestTicket:
    def setup_method(self):
        self.ticket = Ticket(1, 20, "Concert")

    def test_get_id_type(self):
        assert type(self.ticket.get_id()) == int
    
    def test_get_id_(self):
        assert self.ticket.get_id() == 1

    def test_get_price_type(self):
        assert type(self.ticket.get_price()) == int
    
    def test_get_price_(self):
        assert self.ticket.get_price() == 20
    
    def test_get_event_type(self):
        assert type(self.ticket.get_event()) == str
    
    def test_get_event(self):
        assert self.ticket.get_event() == "Concert"

    def test_get_is_sold_type(self):
        assert type(self.ticket.get_is_sold()) == bool

    def test_get_is_sold(self):
        assert self.ticket.get_is_sold() == False
    
    def test_set_is_sold(self):
        self.ticket.set_is_sold()
        assert self.ticket.get_is_sold() == True

    def test_ticket_json_type(self):
        assert type(self.ticket.ticket_json()) == dict

    def test_ticket_json(self):
        assert self.ticket.ticket_json() == {"id": 1, "price": 20, "event": "Concert", "sold": False}