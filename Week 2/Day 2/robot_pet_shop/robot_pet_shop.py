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
        # list to hold all employees
        self.emplyees = []
        # list to hold all pet robots
        self.robots = []
        id = 0
        battery_types = ["lithium", "alkaline"]
        animal_types = ["herbivore", "carnivore"]
        materials = ["iron", "steel"]
        # add 3 employees to list
        for i in range(3):
            employee_name = f"robot-{i}"
            employee_battery_type = random.choice(battery_types)
            salary = random.randint(200,500)
            employee = Employee(employee_name, id, employee_battery_type, salary)
            self.emplyees.append(employee)
            id += 1
        # add some pet robots
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
    # print all or some robots that are on sale
    def print_for_sale(self, in_range=False, from_price=0, to_price=0):
        # if the user want to print robots in a price range
        if in_range:
            for pet in self.robots:
                price = pet.get_price()
                # check if robot is for sale and price is in range
                if pet.get_satus() == "for sale" and price >= from_price and price <= to_price:
                    pet.print_pet()
        else:
            # print all robots
            for pet in self.robots:
                if pet.get_satus() == "for sale":
                    pet.print_pet()
    # print all robots in repaid
    def print_in_repair(self):
        for pet in self.robots:
            if pet.get_satus() == "in repair":
                pet.print_pet()
    # sum up all employees costs
    def get_employees_cost(self):
        sum = 0
        for employee in self.emplyees:
            sum += employee.get_salary()
        return sum
    
    def print_balance(self):
        print(self.balance)
    # get robots id or name then return the robot if it exists
    def get_robot_by_id_name(self,input_given):
        if input_given.isnumeric():
            id = int(input_given)
            for pet in self.robots:
                if pet.id == id:
                    return pet
        else:
            for pet in self.robots:
                if pet.name == input_given:
                    return pet
        print("There is no robot with this id or name")
        return None
    # sell robot and update balance
    def robot_sale(self, robot):
        price = robot.get_price()
        self.balance += price
        robot.change_satus("sold")
    # update balance when day ends, dedce employee salary and robot maintanance
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
        # ask user to enter action command
        user_input = input("Enter a number a number for what action do you want to be done:\n1. Print all pets available for sale\n2. Print print all pets in repair\n3. Print all pet for sale in range\n4. Print employees total salary cost per day\n5. print store balance\n6. print robot details based on id or name\n7. Buy a robot\n8. Break robot\n9. Move robot to repair\n10. End day\n11. Close\n")
        if user_input.isnumeric():
            command = int(user_input)
            match command:
                case 1:
                    # print all robots for sales
                    pet_store.print_for_sale()
                case 2:
                    # print all robots in repair
                    pet_store.print_in_repair()
                case 3:
                    # ask user to enter price range, then print all robots for sale in that range
                    from_str = input("Enter range from\n")
                    to_str = input("Enter range to\n")
                    if from_str.isnumeric() and to_str.isnumeric():
                        from_int = int(from_str)
                        to_int = int(to_str)
                        pet_store.print_for_sale(True, from_int, to_int)
                    else:
                        print("Invalid input entered")
                case 4:
                    # print employyes costs
                    print(pet_store.get_employees_cost())
                case 5:
                    #print store balance
                    pet_store.print_balance()
                case 6:
                    # print a specific robot if it exists
                    user_in = input("Enter id or name\n")
                    pet = pet_store.get_robot_by_id_name(user_in)
                    if pet:
                        pet.print_pet()
                
                case 7:
                    # ask user to enter id or name of a robot that they want to buy
                    user_in = input("Enter id or name\n")
                    pet = pet_store.get_robot_by_id_name(user_in)
                    if pet:
                        pet_store.robot_sale(pet)
                case 8:
                    # change a robot's status to broken
                    user_in = input("Enter id or name\n")
                    pet = pet_store.get_robot_by_id_name(user_in)
                    if pet:
                        pet.change_satus("broken")
                case 9:
                    # send a robot to repair
                    user_in = input("Enter id or name\n")
                    pet = pet_store.get_robot_by_id_name(user_in)
                    if pet:
                        pet.change_satus("in repair")
                case 10:
                    # end day and update balance
                    pet_store.update_balance_day_end()
                    days +=1
                case 11:
                    # close cli
                    keep_going = False

if __name__ == '__main__':
    main()