userInput = input("Enter your input\nInput format:number units, for example\n10 KG\n").lower().split()
if len(userInput) != 2:
    print("Invalid input")
else:
    value = int(userInput[0])
    units = userInput[1]
    if units == "f" or units == "c":
        if units == "f":
            converted_value = (value - 32)*(5/9)
            print(f"Entered {value} F which is {converted_value} C")
        else:
            converted_value = value*(9/5) + 32
            print(f"Entered {value} C which is {converted_value} F")
    elif units == "mph" or units == "kph":
        if units == "kph":
            converted_value = 0.621371 * value
            print(f"Entered {value} KPH which is {converted_value} MPH")
        else:
            converted_value = 1.609344 * value
            print(f"Entered {value} MPH which is {converted_value} KPH")
    elif units == "kg" or units == "stones" or units == "ibs":
        if units == "kg":
            stones_value = 0.157473 * value
            ibs_value = 2.204622 * value 
            print(f"Entered {value} Kg which is {stones_value} stones and {ibs_value} pounds")
        elif units == "ibs":
            kg_value = 0.453592 *value
            stones_value = 0.0714286 * value
            print(f"Entered {value} ponds which is {kg_value} Kg and {stones_value} stones")
        else:
            kg_value = 6.350294 * value
            ibs_value = 14 * value
            print(f"Entered {value} stones which is {kg_value} Kg and {ibs_value} pounds")
    else:
        print("Invalid units entered")
    