user_input = input("Enter your input\nInput format:number units, for example\n10 KG\n").lower().split()
if len(user_input) != 2:
    print("Invalid input")
else:
    if user_input[0].isnumeric():
        value = int(user_input[0])
        units = user_input[1]
        if units == "f" or units == "c":
            if units == "f":
                converted_value = (value - 32)*(5/9)
                print(f"Entered {round(value,3)} F which is {round(converted_value,3)} C")
            else:
                converted_value = value*(9/5) + 32
                print(f"Entered {round(value,3)} C which is {round(converted_value,3)} F")
        elif units == "mph" or units == "kph":
            if units == "kph":
                converted_value = 0.621371 * value
                print(f"Entered {value} KPH which is {round(converted_value,3)} MPH")
            else:
                converted_value = 1.609344 * value
                print(f"Entered {round(value,3)} MPH which is {round(converted_value,3)} KPH")
        elif units == "kg" or units == "stones" or units == "ibs":
            if units == "kg":
                stones_value = 0.157473 * value
                ibs_value = 2.204622 * value 
                print(f"Entered {round(value,3)} Kg which is {round(stones_value,3)} stones and {round(ibs_value,3)} pounds")
            elif units == "ibs":
                kg_value = 0.453592 *value
                stones_value = 0.0714286 * value
                print(f"Entered {round(value,3)} ponds which is {round(kg_value,3)} Kg and {round(stones_value,3)} stones")
            else:
                kg_value = 6.350294 * value
                ibs_value = 14 * value
                print(f"Entered {round(value,3)} stones which is {round(kg_value,3)} Kg and {round(ibs_value,3)} pounds")
        else:
            print("Invalid units entered")
    