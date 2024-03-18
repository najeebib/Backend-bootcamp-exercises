from modules.person import Person
class TestPerson:
    def setup_method(self):
        self.person = Person("test person")

    def test_person_get_tickets(self):
        assert self.person.get_num_of_tickets() == 0
        
    def test_person_tickets_int(self):
        assert type(self.person.get_num_of_tickets()) == int

    def test_add_ticket(self):
        self.person.add_ticket()
        assert self.person.get_num_of_tickets() == 1