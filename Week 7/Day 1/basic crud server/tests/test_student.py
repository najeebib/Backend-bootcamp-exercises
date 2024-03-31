from modules.student import Student
""" test the student class """
class TestStudent:
    def setup_method(self):
        self.student = Student("najeeb", 319051066, 25, ["operating systems", "physics 2", "calculus 2"])
    # test if the get_name methode returns a string
    def test_name_type(self):
        assert type(self.student.get_name()) == str
    # test if the get_name methode returns the correct name
    def test_name(self):
        assert self.student.get_name() == "najeeb"
    # test if the get_id methode returns an int
    def test_id_type(self):
        assert type(self.student.get_id()) == int
    # test if the get_id methode returns the correct id
    def test_id(self):
        assert self.student.get_id() == 319051066
    # test if the get_age methode returns an int
    def test_age_type(self):
        assert type(self.student.get_age()) == int
    # test if the get_age methode returns the correct age
    def test_age(self):
        assert self.student.get_age() == 25
    # test if the get_classes methode returns a list
    def test_classes_type(self):
        assert type(self.student.get_classes()) == list
    # test if the get_classes methode returns the correct list of classes
    def test_classes(self):
        assert self.student.get_classes() == ["operating systems", "physics 2", "calculus 2"]
    