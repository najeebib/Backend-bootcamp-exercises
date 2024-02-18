# jab = 1
# cross = 2
# hook = 3
# upercut = 4
# jab > upercut > hook > cross > jab 
rounds_num = int(input("Enter number of rounds\n"))
if rounds_num < 0:
    print("print valid number of rounds")
current_round = 0
import random
while current_round < rounds_num:
    current_round += 1
    user_input = int(input("Select a number from 1-4\n"))
    if user_input > 4 or user_input < 0:
        current_round -= 1
        print("Enter valid number (between 1 and 4)")
    random_choice = random.randint(1, 4)
    print(f"user move: {user_input} computer move: {random_choice}")
    if user_input == random_choice:
        print(f"draw round {current_round}")
    else:
        match user_input:
            case 1:
                if random_choice == 4:
                    print(f"user wins round {current_round}")
                else:
                    print(f"computer wins round {current_round}")
            case 2:
                if random_choice == 1:
                    print(f"user wins round {current_round}")
                else:
                    print(f"computer wins round {current_round}")
            case 3:
                if random_choice == 2 or random_choice == 1:
                    print(f"user wins round {current_round}")
                else:
                    print(f"computer wins round {current_round}")
            case 4:
                if random_choice == 3 or random_choice == 2:
                    print(f"user wins round {current_round}")
                else:
                    print(f"computer wins round {current_round}")