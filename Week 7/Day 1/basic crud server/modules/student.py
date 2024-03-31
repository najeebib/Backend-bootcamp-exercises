class Student:
    """ a class to represent the student
    """
    def __init__(self, name: str, id: int, age:int, classes: list):
        """ initilize the student object

        :param name: name of student
        :param id: id of student
        :param age: age of student
        :param classes: list of student's classes
        """
        self._name = name
        self._id = id
        self._age = age
        self._classes = classes

    def get_name(self):
        return self._name
    
    def get_id(self):
        return self._id
    
    def get_age(self):
        return self._age
    
    def get_classes(self):
        return self._classes
