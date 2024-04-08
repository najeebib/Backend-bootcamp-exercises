from modules.profanity_filter import ProfanityFilter
""" test the student class """
class TestProfanityFilter:
    def setup_method(self):
        self.filter = ProfanityFilter()

    def test_filter1(self):
        message = "Hello there"
        assert self.filter.censor(message) == message

    def test_filter2(self):
        message = "fuck you"
        assert self.filter.censor(message) == "**** you"