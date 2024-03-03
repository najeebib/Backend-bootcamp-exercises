from test_modules.test_numbers import TestNumbers
from test_modules.test_list import TestList
from test_modules.test_dictionary import TestDictionary
def check_in_list(test, list, number):
    return test.is_in_list(list, number)

def check_if_key(test, dict, value):
    return test.is_a_key(dict, value)
def check_if_value(test, dict, value):
    return test.is_a_value(dict, value)

test_numbers = TestNumbers()
print(test_numbers.is_greater_or_smaller(10, 1))
test_list = TestList()
if not check_in_list(test_list,[5,1,[7,[2]]], 9):
    print("The input number isn't in the list")
if check_in_list(test_list,[5,1,[7,[2]]], 5):
    print("The input number is in the list")
if check_in_list(test_list,[5,1,[7,[2]]], 7):
    print("The input number is in the list")
if check_in_list(test_list,[5,1,[7,[2]]], 2):
    print("The input number is in the list")
test_dict = TestDictionary()
nested_dict = {'a': 1, 'b': {'c': 2, 'd': {'e': 3, 'f': 4}}}
if check_if_key(test_dict, nested_dict, 'f'):
    print("Input is a key in dictionary")
if not check_if_key(test_dict, nested_dict, 'p'):
    print("Input isn't a key in dictionary")
if check_if_value(test_dict, nested_dict, 2):
    print("Input is a value in dictionary")
if not check_if_value(test_dict, nested_dict, 9):
    print("Input isn't a value in dictionary")