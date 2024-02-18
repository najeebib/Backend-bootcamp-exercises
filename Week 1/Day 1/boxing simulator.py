# jab = 1
# cross = 2
# hook = 3
# upercut = 4
# jab > upercut > hook > cross > jab 

import random
while True:
    user_input = int(input("Select a number from 1-4\n"))
    random_choice = random.randint(1, 4)
    print(f"user move: {user_input} computer move: {random_choice}")
    if user_input == random_choice:
        print("draw")
    else:
        match user_input:
            case 1:
                if random_choice == 4:
                    print("user wins")
                else:
                    print("computer wins")
            case 2:
                if random_choice == 1:
                    print("user wins")
                else:
                    print("computer wins")
            case 3:
                if random_choice == 2 or random_choice == 1:
                    print("user wins")
                else:
                    print("computer wins")
            case 4:
                if random_choice == 3 or random_choice == 2:
                    print("user wins")
                else:
                    print("computer wins")