class Item:
    def __init__(self, name, weight, is_electronic):
        self.name = name
        self.weight = weight
        self.is_electronic = is_electronic

    def get_weight(self):
        return self.weight
    def get_name(self):
        return self.name
    def get_is_electronic(self):
        return self.is_electronic

class Electronic:
    def __init__(self, brand, size, OS, storage, display, camera, cpu, ram, gpu, battery_life, fitness_features, connectivity):
        self.brand = brand
        self.size = size
        self.OS = OS
        self.storage = storage
        self.display = display
        self.camera = camera
        self.cpu = cpu
        self.ram = ram
        self.battery_life = battery_life
        self.gpu = gpu
        self.fitness_features = fitness_features
        self.connectivity = connectivity
    
    def print_item(self):
        print(f"Name: {self.name} Weight: {self.weight} Brand: {self.brand}")
    
class Accessory:
    def __init__(self,color, origin,materials,price,  new, accuracy, case):
        self.color = color
        self.origin = origin
        self.materials = materials
        self.price = price
        self.new = new
        self.accuracy = accuracy
        self.case = case
    
    def print_item(self):
        print(f"Name: {self.name} Weight: {self.weight} Origin: {self.origin}")

class Charger(Item):
    def __init__(self,name, color, price, weight, size, brand):
        super().__init__(name, weight,True)
        electronic = Electronic(brand, size, "", "", "", "", "", "", "", "" , "", "")
        accessory = Accessory(color, "", "", price, "", "", "")
        self.price = accessory.price
        self.size = electronic.size
        self.brand = electronic.brand
        self.color = accessory.color

    def print_item(self):
        print(f"Name: {self.name} Weight: {self.weight} Price: {self.price} Size: {self.size} Brand: {self.brand} Color: {self.color}")

class Passport(Item):
    def __init__(self,name, weight, color, price, origin):
        super().__init__(name, weight,False)
        accessory = Accessory(color, origin, "", price, "", "","")
        self.price = accessory.price
        self.origin = accessory.origin
        self.color = accessory.color
            
    def print_item(self):
        print(f"Name: {self.name} Weight: {self.weight} Price: {self.price} origin: {self.origin} Color: {self.color}")

class Sunglasses(Item):
    def __init__(self,name, weight,color, case, origin):
        super().__init__(name, weight,False)
        accessory = Accessory(color, origin, "", 0, "", "", case)
        self.origin = accessory.origin
        self.color = accessory.color
        self.case = accessory.case
            
    def print_item(self):
        print(f"Name: {self.name} Weight: {self.weight} Has case: {self.case} origin: {self.origin} Color: {self.color}")

class Sneakers(Item):
    def __init__(self,name, weight, brand, used, origin):
        super().__init__(name, weight,False)
        electronic = Electronic(brand, 0, "", "","", "", "", "", "", "", "", "")
        accessory = Accessory("", origin, "", 0, used, "", "")
        self.brand = electronic.brand
        self.used = accessory.new
        self.origin = accessory.origin
            
    def print_item(self):
        print(f"Name: {self.name} Weight: {self.weight} Brand: {self.brand} Used: {self.used} Origin: {self.origin}")


class Smartphone(Item):
    def __init__(self,name, weight, brand, OS, storage, display, camera, materials):
        super().__init__(name, weight,True)
        electronic = Electronic(brand, 0, OS, storage,display, camera, "", "", "", "", "", "")
        accessory = Accessory("", "", materials, 0, "", "", "")
        self.brand = electronic.brand
        self.OS = electronic.OS
        self.storage = electronic.storage
        self.display = electronic.display
        self.camera = electronic.camera
        self.materials = accessory.materials
            
    def print_item(self):
        print(f"Name: {self.name} Weight: {self.weight} Brand: {self.brand} OS: {self.OS} Storage: {self.storage} Display: {self.display} Camera: {self.camera} Materials: {self.materials}")

class Laptop(Item):
    def __init__(self,name, weight, brand, cpu, ram, storage, gpu):
        super().__init__(name, weight,True)
        electronic = Electronic(brand, 0, "", storage, "", "", cpu, ram, gpu, "", "", "")
        self.brand = electronic.brand
        self.cpu = electronic.cpu
        self.ram = electronic.ram
        self.storage = electronic.storage
        self.gpu = electronic.gpu
            
    def print_item(self):
        print(f"Name: {self.name} Weight: {self.weight} Brand: {self.brand} CPU: {self.cpu} RAM: {self.ram} Storage: {self.storage} GPU: {self.gpu}")

class Smartwatch(Item):
    def __init__(self,name, weight, brand,display, battery_life, fitness_features, connectivity):
        super().__init__(name, weight,True)
        electronic = Electronic(brand, 0, "", "",display, "", "", "", "", battery_life, fitness_features, connectivity)
        self.brand = electronic.brand
        self.display = electronic.display
        self.battery_life = electronic.battery_life
        self.fitness_features = electronic.fitness_features
        self.connectivity = electronic.connectivity
        
            
    def print_item(self):
        print(f"Name: {self.name} Weight: {self.weight} Brand: {self.brand} Display: {self.display} Battery life: {self.battery_life} Fitness features: {self.fitness_features} Connectivity: {self.connectivity}")

class Campus(Item):
    def __init__(self,name,weight, brand, accuracy, price, materials):
        super().__init__(name, weight,False)
        electronic = Electronic(brand, 0, "", "","", "", "", "", "", "", "", "")
        accessory = Accessory("", "", materials, price, "", accuracy, "")
        self.brand = electronic.brand
        self.price = accessory.price
        self.accuracy = accessory.accuracy
        self.materials = accessory.materials
            
    def print_item(self):
        print(f"Name: {self.name} Weight: {self.weight} Brand: {self.brand} Accuracy: {self.accuracy} Price: {self.price} Materials: {self.materials}")

class Inventory:
    def __init__(self):
        self.items = []
        self.items_num = 0
    
    def add_item(self, item):
        self.items.append(item)
        self.items_num += 1

    def get_items_num(self):
        return self.items_num
    
    def print_category(self, category):
        match category:
            case 1:
                for item in self.items:
                    if item.get_is_electronic():
                        item.print_item()
            case 2:
                for item in self.items:
                    if not item.get_is_electronic():
                        item.print_item()
    def print_by_category(self):
        for i in range(1,3):
            if i == 1:
                print("electronic items")
                self.print_category(i)
            else:
                print("Accessory items")
                self.print_category(i)

    def find_item(self, name):
        for item in self.items:
            if item.get_name() == name:
                return item
        print("No item in inventory with this name")
        return None

        
class Bag(Inventory):
    def __init__(self):
        super().__init__()
        self.total_weight = 0
        self.max_items = 6
        self.max_weight = 80
    
    def add_item(self, item):
        num_of_items = len(self.items)
        item_weight = item.get_weight()

        if num_of_items < self.max_items and item_weight + self.total_weight <= self.max_weight:
            self.items.append(item)
            self.total_weight += item_weight
            print(f"Item: {item.get_name()} has been added to the bag")
        else:
            print("Couldn't add item to bag")

    def remove_item(self, item):
        if item in self.items:
            item_weight = item.get_weight()

            self.items.remove(item)
            self.total_weight -= item_weight
            print(f"Item: {item.get_name()} has been removed from the bag")
        else:
            print("This item isn't in the bag")

    def print_all_items(self):
        for item in self.items:
            item.print_item()
    
    

def init_store():
    store_inventory = Inventory()
    charger = Charger("universal charger", "black", 50, 12, 50, "lenovo")
    store_inventory.add_item(charger)
    passport = Passport("passport", 1, "blue", 50, "USA")
    store_inventory.add_item(passport)
    sunglasses = Sunglasses("sunglasses", 10, "black", True, "Italy")
    store_inventory.add_item(sunglasses)
    sneakers = Sneakers("sneakers", 14, "New Balance", False, "Spain")
    store_inventory.add_item(sneakers)
    smartphone = Smartphone("smartphone", 10, "Apple", "IOS", "128 GB", "AMOLED", "Dual lens", "lithium, plastic")
    store_inventory.add_item(smartphone)
    laptop = Laptop("laptop", 60, "Dell", "Intel i7", "16 GB", "512 GB SSD", "NVIDIA GeForce4")
    store_inventory.add_item(laptop)
    smartwatch = Smartwatch("smartwatch", 44,"Samsung", "Touchscreen", "3 Days", "Heart rate monitor", "Bluetooth")
    store_inventory.add_item(smartwatch)
    campus = Campus("campus", 4, "Samsung", "high", 50, "iron, plastic")
    store_inventory.add_item(campus)
    
    return store_inventory

bag = Bag()
def main():
    store_inventory = init_store()
    
    keep_going = True
    while keep_going:
        user_input = input("Enter a number a number for what action do you want to be done:\n1. Print all items in inventory\n2. Print items from a certain category\n3. Add item to bag\n4. Remove item from bag\n5. Print all items from bag\n6. Close\n")
        if user_input.isnumeric():
            command = int(user_input)
            match command:
                case 1:
                    store_inventory.print_by_category()
                case 2:
                    category = input("Enter a category:\n1. Electronic devices\n2. Accessory item\n")
                    if category.isnumeric():
                        category = int(category)
                        store_inventory.print_category(category)
                    else:
                        print("Enter valid input")
                case 3:
                    name = input("Enter item name\n")
                    item = store_inventory.find_item(name)
                    if item:
                        bag.add_item(item)
                case 4:
                    name = input("Enter item name\n")
                    item = store_inventory.find_item(name)
                    if item:
                        bag.remove_item(item)
                case 5:
                    bag.print_all_items()
                case 6:
                    keep_going = False

if __name__ == '__main__':
    main()