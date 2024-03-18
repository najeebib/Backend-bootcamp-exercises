from modules.person import Person
class TestPerson:
    # setup the class object to use it in tests
    def setup_method(self):
        self.person = Person("test person")
    # test the number of tickets
    def test_person_get_tickets(self):
        assert self.person.get_num_of_tickets() == 0
    # test the number of tickets type
    def test_person_tickets_int(self):
        assert type(self.person.get_num_of_tickets()) == int
    # test the number of tickets has been update
    def test_add_ticket(self):
        self.person.add_ticket()
        assert self.person.get_num_of_tickets() == 1