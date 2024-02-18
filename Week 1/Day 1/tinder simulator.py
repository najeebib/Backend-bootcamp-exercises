user1 = "Annie Edison"
user1_age = 21
user1_gender = "f"
user1_profession = "fbi_agent"
user1_favorit_food = "Pizza"
user1_favorit_show = "Broklyn_99"

user2 = "Abed Nader"
user2_age = 24
user2_gender = "m"
user2_profession = "movie_director"
user2_favorit_food = "Flafel"
user2_favorit_show = "Doctore_who"

user3 = "Jeff Winger"
user3_age = 31
user3_gender = "m"
user3_profession = "Lawer"
user3_favorit_food = "BBQ"
user3_favorit_show = "Law_and_Order"

user4 = "Shirley Bennet"
user4_age = 42
user4_gender = "f"
user4_profession = "Chef"
user4_favorit_food = "Chicken"
user4_favorit_show = "Master_Chef"

user_inputs = input("Enter your user details in this format (withot any spaces in in the profession, show or food): \"age\" \"gender\" \"profession\" \"favorit food\" \"favorit show\"\n").split()
gender_rule = input("Enter gender rule (f or m)\n")
age = input("Enter age rule (from to) for example: 20 30\n").split()
if age[0].isnumeric() and  age[1].isnumeric():
    age_low = int(age[0])
    age_high = int(age[1])
    profession_rule = input("Enter profession rule\n")
    food_rule = input("Enter food rule\n")
    show_rule = input("Enter show rule\n")

    if user1_age >= age_low and user1_age <age_high and user1_gender == gender_rule and user1_profession == profession_rule and user1_favorit_food == food_rule and user1_favorit_show == show_rule:
        print(f"match with  {user1}")
    elif user2_age >= age_low and user2_age <age_high and user2_gender == gender_rule and user2_profession == profession_rule and user2_favorit_food == food_rule and user2_favorit_show == show_rule:
        print(f"match with  {user2}")
    elif user3_age >= age_low and user3_age <age_high and user3_gender == gender_rule and user3_profession == profession_rule and user3_favorit_food == food_rule and user3_favorit_show == show_rule:
        print(f"match with  {user3}")
    elif user4_age >= age_low and user4_age <age_high and user4_gender == gender_rule and user4_profession == profession_rule and user4_favorit_food == food_rule and user4_favorit_show == show_rule:
        print(f"match with  {user4}")
    else:
        print("no matches")
else:
    print("error, enter valid numbers for age")
