class Class:
    def __init__(self, name: str, id: int, teacher: str, topics: list):
        self._name = name
        self._id = id
        self._teacher = teacher
        self._topics = topics
    
    def get_name(self):
        return self._name
    
    def get_id(self):
        return self._id
    
    def get_teacher(self):
        return self._teacher
    
    def get_topics(self):
        return self._topics