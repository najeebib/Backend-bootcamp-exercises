import random

materials = ["Wood","Steel","Glass","Plastic","Aluminum","Copper","Paper","Water","Rubber","Leather","Concrete","Ceramics","Stone","Gold","Silver","Titanium","Oil","Bronze","Uranium","Vibranium"]

alient_delegations = [{"name": "Tau Empire","Needed Materials":["Oil","Wood","Alumium"],"Number of sugestions": 6},
                      {"name": "Eldar","Needed Materials":["Concret","Silver","Leather"],"Number of sugestions": 3},
                      {"name": "Orc Hord","Needed Materials":["Uranium","Steel","Oil"],"Number of sugestions": 5},
                      {"name": "Space Dwarves","Needed Materials":["Glass","Wood","Paper"],"Number of sugestions": 8}]

delegations_num = len(alient_delegations)
success_count = 0
for i in range(delegations_num):
    suggestion = 0
    delegation = alient_delegations[i]
    is_there_material = False
    while suggestion < delegation["Number of sugestions"]:
        random_material = materials[random.randint(0,len(materials))]
        suggestion += 1
        if random_material in delegation["Needed Materials"]:
            is_there_material = True
            break
    if is_there_material:
        print(f"The United Nations of earth has reached an alliance agreement with the {delegation['name']}")
        success_count +=1
    else:
        print(f"The United Nations of earth has failed to reach an agreement with the {delegation['name']}")

rate = success_count/delegations_num
print(f"The negotiations success rate is: {rate}")
if rate > 0.7:
    print("The United Nations of earth has successfully formed a galactic empire\nFrom this day forth it shall be know as the Imperium of Man")
else:
    print("The United Nations of earth has failed to forme a galactic empire")