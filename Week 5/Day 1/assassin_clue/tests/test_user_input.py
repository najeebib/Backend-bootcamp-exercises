from modules.user_input import UserInputManager

def test_get_number_of_players():
    assert type(UserInputManager.get_number_of_players()) == int

def test_get_accused_number():
    assert type(UserInputManager.get_accused_number(2)) == int