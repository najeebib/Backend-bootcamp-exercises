from modules.raffle import Raffle
from modules.person import Person
import pytest
class TestRaffle:
    # setup the class object to use it in tests 
    def setup_method(self):
        self.raffle = Raffle(5, 20, 10)
    # test if the max number of people is the same as specified in setup method
    def test_get_max_people(self):
        assert self.raffle.get_max_people() == 5
    # test if the function get_max_people returns an integer
    def test_max_people_int(self):
        assert type(self.raffle.get_max_people()) == int
    # test if the max number of tickets is the same as specified in setup method
    def test_get_max_tickets(self):
        assert self.raffle.get_max_tickets() == 20

    # test if the ticket price is the same as specified in setup method
    def test_get_ticket_price(self):
        assert self.raffle.get_ticket_price() == 10 
    # test if the function get_max_tickets returns an integer 
    def test_max_tickets_int(self):
        assert type(self.raffle.get_max_tickets()) == int
    # check the if the list of people is empty
    def test_get_people(self):
        assert len(self.raffle.get_people()) == 0
    # check the if the list of people has two people after two people buy tickets
    def test_get_people2(self):
        self.raffle.buy_ticket(Person("person 1"))
        self.raffle.buy_ticket(Person("person 2"))
        assert len(self.raffle.get_people()) == 2
    # test if the function get_people returns a list    
    def test_get_people_list(self):
        assert type(self.raffle.get_people()) == list
    # test if the number of tickets is 0 when no people have partcipated
    def test_get_tickets(self):
        assert self.raffle.get_tickets() == 0
     # test if the number of tickets is 2 have bought tickets
    def test_get_tickets2(self):
        self.raffle.buy_ticket(Person("person 1"))
        self.raffle.buy_ticket(Person("person 2"))
        assert self.raffle.get_tickets() == 2
    # test if the function get_tickets returns an integer    
    def test_get_tickets_int(self):
        assert type(self.raffle.get_tickets()) == int
    # test if the total earning is zero when no one bought tickets
    def test_get_earnings(self):
        assert self.raffle.get_total_earnings() == 0
    # test if the total earning is zero when no one bought tickets
    def test_get_earnings2(self):
        self.raffle.buy_ticket(Person("person 1"))
        self.raffle.buy_ticket(Person("person 2"))
        assert self.raffle.get_total_earnings() == 20
    # test if the function get_total_earnings returns an integer     
    def test_get_earnings_int(self):
        assert type(self.raffle.get_total_earnings()) == int
    # test if the buy function fails when it doesnt recieve a person
    def test_buy_fail(self):
        with pytest.raises(TypeError):
            self.raffle.buy_ticket("test")
    # test if the select_winner return None if people list is empty
    def test_get_winner(self):
        assert self.raffle.select_winner() == None
    # test if the select_winner returns an object of type Person 
    def test_get_winner2(self):
        self.raffle.buy_ticket(Person("person 1"))
        assert type(self.raffle.select_winner()) == Person
    # test if the select_winner returns a person that is in people list
    def test_get_winner3(self):
        self.raffle.buy_ticket(Person("person 2"))
        winner = self.raffle.select_winner()
        assert winner in self.raffle.get_people()


