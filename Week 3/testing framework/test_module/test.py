class Test:
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
            #for val in value:# Test().is_in_list([5,1,[7,[2]]], 7) return true but Test().is_in_list([5,1,[7,[2]]], 2) return False
                #if self.is_list(val):
                    #if other in val:# the reason for that is this doesnt check if the value is in a nested list inside the list
                        #return True
                #else:
                    #if other == val:
                        #return True
            #return False
            return self.is_number_in_nested_list(value, other)
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
