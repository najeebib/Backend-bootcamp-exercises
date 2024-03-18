from modules.raffle import Raffle
from modules.person import Person
import pytest
class TestRaffle:
    def setup_method(self):
        self.raffle = Raffle(5, 20, 10)

    def test_get_max_people(self):
        assert self.raffle.get_max_people() == 5
        
    def test_max_people_int(self):
        assert type(self.raffle.get_max_people()) == int

    def test_get_max_tickets(self):
        assert self.raffle.get_max_tickets() == 20
        
    def test_max_tickets_int(self):
        assert type(self.raffle.get_max_tickets()) == int
    
    def test_get_people(self):
        assert len(self.raffle.get_people()) == 0
        
    def test_get_people_list(self):
        assert type(self.raffle.get_people()) == list

    def test_get_tickets(self):
        assert self.raffle.get_tickets() == 0
        
    def test_get_tickets_int(self):
        assert type(self.raffle.get_tickets()) == int

    def test_get_earnings(self):
        assert self.raffle.get_total_earnings() == 0
        
    def test_get_earnings_int(self):
        assert type(self.raffle.get_total_earnings()) == int

    def test_buy_fail(self):
        with pytest.raises(TypeError):
            self.raffle.buy_ticket("test")

    def test_get_winner(self):
        assert self.raffle.select_winner() == None

    def test_get_winner2(self):
        self.raffle.buy_ticket(Person("person 1"))
        assert type(self.raffle.select_winner()) == Person

    def test_get_winner3(self):
        self.raffle.buy_ticket(Person("person 2"))
        winner = self.raffle.select_winner()
        assert winner in self.raffle.get_people()


