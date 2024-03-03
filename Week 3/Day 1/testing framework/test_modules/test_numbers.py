class TestNumbers:
    def __init__(self):
        pass

    def validate_number(self, value):
        numeric_values = (int, float)
        self_type = type(value)
        if self_type not in numeric_values:
            return False
        else:
            return True
    def is_greater_or_smaller(self, value, other):
        if not self.validate_number(value):
            return "Test value isn't a number"
        elif not self.validate_number(other):
            return "Input value isn't a number"
        else:
            if value > other:
                return "Input is smaller than test value"
            elif value < other:
                return "Input is bigger than test value"
            else:
                return "Both numbers are equal"
        
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
