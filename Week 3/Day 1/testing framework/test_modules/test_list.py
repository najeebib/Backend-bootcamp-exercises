class TestList:
    def __init__(self):
        pass

    def validate_number(self, value):
        numeric_values = (int, float)
        self_type = type(value)
        if self_type not in numeric_values:
            return False
        else:
            return True
        

    def is_list(self, value):
        if isinstance(value, list):
            return True
        else:
            return False
    
    
    
    def is_number_in_nested_list(self, value, other):
        for val in value:
            if self.is_list(val):
                if self.is_number_in_nested_list(val, other):
                    return True
            elif other == val:
                return True
        return False
    def is_in_list(self, value, other):
        if not self.is_list(value):
            print("Test value isn't a list")
            return False
        elif not self.validate_number(other):
            print("Input value isn't a number")   
            return False
        else:
            return self.is_number_in_nested_list(value, other)
