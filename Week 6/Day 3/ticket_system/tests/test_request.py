from modules.request import Request
class TestRequest:
    def setup_method(self):
        self.request = Request('2024-03-26 11:50:00', "Concert", 2)

    def test_get_timestamp_type(self):
        assert type(self.request.get_timestamp()) == str

    def test_get_timestamp(self):
        assert self.request.get_timestamp() == '2024-03-26 11:50:00'

    def test_get_event_type(self):
        assert type(self.request.get_event()) == str

    def test_get_event(self):
        assert self.request.get_event() == "Concert"

    def test_number_of_tickets_type(self):
        assert type(self.request.get_number_of_tickets()) == int

    def test_number_of_tickets(self):
        assert self.request.get_number_of_tickets() == 2