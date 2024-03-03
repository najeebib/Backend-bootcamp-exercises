from test_module.test import Test
def check_in_list(test, list, number):
    return test.is_in_list(list, number)

def check_if_key(test, dict, value):
    return test.is_a_key(dict, value)
def check_if_value(test, dict, value):
    return test.is_a_value(dict, value)

test = Test()
print(test.is_greater_or_smaller(10, 1))
if not check_in_list(test,[5,1,[7,[2]]], 9):
    print("The input number isn't in the list")
if check_in_list(test,[5,1,[7,[2]]], 5):
    print("The input number is in the list")
if check_in_list(test,[5,1,[7,[2]]], 7):
    print("The input number is in the list")
if check_in_list(test,[5,1,[7,[2]]], 2):
    print("The input number is in the list")

nested_dict = {'a': 1, 'b': {'c': 2, 'd': {'e': 3, 'f': 4}}}
if check_if_key(test, nested_dict, 'f'):
    print("Input is a key in dictionary")
if not check_if_key(test, nested_dict, 'p'):
    print("Input isn't a key in dictionary")
if check_if_value(test, nested_dict, 2):
    print("Input is a value in dictionary")
if not check_if_value(test, nested_dict, 9):
    print("Input isn't a value in dictionary")