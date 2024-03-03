class TestDictionary:
    def __init__(self):
        pass

    def is_dict(self, value):
        if isinstance(value, dict):
            return True
        else:
            return False
        
    def is_a_key(self, value, other):
        for key, item in value.items():
            if key == other:
                return True
            elif self.is_dict(item):
                if self.is_a_key(item, other):
                    return True
        return False
    
    def is_a_value(self, value, other):
        for key, item in value.items():
            if item == other:
                return True
            elif self.is_dict(item):
                if self.is_a_value(item, other):
                    return True
        return False