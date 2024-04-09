from modules.school_class import SchoolClass
""" test the student class """
class TestStudent:
    def setup_method(self):
        self.class_ = SchoolClass("math",1, "salem", ["algebra", "statistics"])
    # test if the get_name methode returns a string
    def test_name_type(self):
        assert type(self.class_.get_name()) == str
    # test if the get_name methode returns the correct name
    def test_name(self):
        assert self.class_.get_name() == "math"
    # test if the get_id methode returns an int
    def test_id_type(self):
        assert type(self.class_.get_id()) == int
    # test if the get_id methode returns the correct id
    def test_id(self):
        assert self.class_.get_id() == 1
    # test if the get_teacher methode returns an int
    def test_teacher_type(self):
        assert type(self.class_.get_teacher()) == str
    # test if the get_teacher methode returns the correct age
    def test_teacher(self):
        assert self.class_.get_teacher() == "salem"
    # test if the get_topics methode returns a list
    def test_topics_type(self):
        assert type(self.class_.get_topics()) == list
    # test if the get_topics methode returns the correct list of classes
    def test_topics(self):
        assert self.class_.get_topics() == ["algebra", "statistics"]
