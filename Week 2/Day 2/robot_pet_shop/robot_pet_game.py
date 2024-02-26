import random

class Robot:
    def __init__(self, name, id, battery_type):
        self.name = name
        self.id = id
        self.battery_type = battery_type

class Employee(Robot):
    def __init__(self, name, id, battery_type, salary):
        super().__init__(name, id, battery_type)
        self.salary = salary

    def get_salary(self):
        return self.salary

class PetRobot(Robot):
    def __init__(self, name, id, battery_type, main_material, price, cost_to_fix_per_day, animal_type, status):
        super().__init__(name, id, battery_type)
        self.main_material = main_material
        self.price = price
        self.cost_to_fix_per_day = cost_to_fix_per_day
        self.animal_type = animal_type
        self.status = status
    
    def get_satus(self):
        return self.status

    def get_price(self):
        return self.price
    
    def print_pet(self):
        print(f"Pet name: {self.name} Id: {self.id} material: {self.main_material} animal type: {self.animal_type} battery type: {self.battery_type} price: {self.price}")

    def change_satus(self, status):
        self.status = status

    def get_cost(self):
        return self.cost_to_fix_per_day
class Store:
    def __init__(self):
        self.balance = 0
        self.emplyees = []
        self.robots = []
        id = 0
        battery_types = ["lithium", "alkaline"]
        animal_types = ["herbivore", "carnivore"]
        materials = ["iron", "steel"]
        for i in range(3):
            employee_name = f"robot-{i}"
            employee_battery_type = random.choice(battery_types)
            salary = random.randint(200,500)
            employee = Employee(employee_name, id, employee_battery_type, salary)
            self.emplyees.append(employee)
            id += 1

        for i in range(15):
            pet_name = f"pet-robot-{i}"
            pet_battery_type = random.choice(battery_types)
            pet_animal_type = random.choice(animal_types)
            material = random.choice(materials)
            price = random.randint(2000,3500)
            cost_to_fix_per_day = random.randint(100,200)
            pet = PetRobot(pet_name, id, pet_battery_type, material, price, cost_to_fix_per_day, pet_animal_type, "for sale")
            self.robots.append(pet)
            id += 1

    def print_for_sale(self, in_range=False, from_price=0, to_price=0):
        if in_range:
            for pet in self.robots:
                price = pet.get_price()
                if pet.get_satus() == "for sale" and price >= from_price and price <= to_price:
                    pet.print_pet()
        else:
            for pet in self.robots:
                if pet.get_satus() == "for sale":
                    pet.print_pet()
    
    def print_in_repair(self):
        for pet in self.robots:
            if pet.get_satus() == "in repair":
                pet.print_pet()

    def get_employees_cost(self):
        sum = 0
        for employee in self.emplyees:
            sum += employee.get_salary()
        return sum
    
    def print_balance(self):
        print(self.balance)

    def get_robot_by_id_name(self,input_given):
        if input_given.isnumeric():
            id = int(input_given)
            for pet in self.robots:
                if pet.id == id:
                    return pet
                    break
        else:
            for pet in self.robots:
                if pet.name == input_given:
                    return pet
                    break
        print("There is no robot with this id or name")
        return None

    def robot_sale(self, robot):
        price = robot.get_price()
        self.balance += price
        robot.change_satus("sold")

    def update_balance_day_end(self):
        employees_cost = self.get_employees_cost()
        self.balance -= employees_cost
        repirs_cost = 0
        for pet in self.robots:
            if pet.get_satus()  == "in repair":
                repirs_cost += pet.get_cost()
        self.balance -= repirs_cost

def main():
    pet_store = Store()
    keep_going = True
    days = 1
    while keep_going:
        print(f"Day {days}")
        user_input = input("Enter a number a number for what action do you want to be done:\n1. Print all pets available for sale\n2. Print print all pets in repair\n3. Print all pet for sale in range\n4. Print employees total salary cost per day\n5. print store balance\n6. print robot details based on id or name\n7. Buy a robot\n8. Break robot\n9. Move robot to repair\n10. End day\n11. Close\n")
        if user_input.isnumeric():
            command = int(user_input)
            match command:
                case 1:
                    pet_store.print_for_sale()
                case 2:
                    pet_store.print_in_repair()
                case 3:
                    from_str = input("Enter range from\n")
                    to_str = input("Enter range to\n")
                    if from_str.isnumeric() and to_str.isnumeric():
                        from_int = int(from_str)
                        to_int = int(to_str)
                        pet_store.print_for_sale(True, from_int, to_int)
                    else:
                        print("Invalid input entered")
                case 4:
                    print(pet_store.get_employees_cost())
                case 5:
                    pet_store.print_balance()
                case 6:
                    user_in = input("Enter id or name\n")
                    pet = pet_store.get_robot_by_id_name(user_in)
                    if pet:
                        pet.print_pet()
                
                case 7:
                    user_in = input("Enter id or name\n")
                    pet = pet_store.get_robot_by_id_name(user_in)
                    if pet:
                        pet_store.robot_sale(pet)
                case 8:
                    user_in = input("Enter id or name\n")
                    pet = pet_store.get_robot_by_id_name(user_in)
                    if pet:
                        pet.change_satus("broken")
                case 9:
                    user_in = input("Enter id or name\n")
                    pet = pet_store.get_robot_by_id_name(user_in)
                    if pet:
                        pet.change_satus("in repair")
                case 10:
                    pet_store.update_balance_day_end()
                    days +=1
                case 11:
                    keep_going = False

if __name__ == '__main__':
    main()