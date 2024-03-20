from modules.record import Record
from datetime import datetime
class TestRecord:
    def setup_method(self):
        self.record = Record(datetime.now().strftime("%d/%m/%Y, %H:%M:%S"), 11, 34)
        
    def test_get_timestamp(self):
        assert type(self.record.get_timestamp()) == str

    def test_get_deaths(self):
        assert type(self.record.get_deaths()) == int

    def test_get_births(self):
        assert type(self.record.get_births()) == int

    def test_get_deaths2(self):
        assert self.record.get_deaths() == 11

    def test_get_births2(self):
        assert self.record.get_births() == 34