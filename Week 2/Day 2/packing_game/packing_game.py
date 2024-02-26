class Item:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def get_weight(self):
        return self.weight
    def get_name(self):
        return self.name

class Electronic(Item):
    def __init__(self, name, weight, brand):
        super().__init__(name, weight)
        self.brand = brand
    
    def print_item(self):
        print(f"Name: {self.name} Weight: {self.weight} Brand: {self.brand}")
    
class Accessory(Item):
    def __init__(self, name, weight, origin):
        super().__init__(name, weight)
        self.origin = origin
    
    def print_item(self):
        print(f"Name: {self.name} Weight: {self.weight} Origin: {self.origin}")

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
                    if isinstance(item, Electronic):
                        item.print_item()
            case 2:
                for item in self.items:
                    if isinstance(item, Accessory):
                        item.print_item()
    def print_by_category(self):
        for i in range(1,3):
            if i == 1:
                print("Elctronic items")
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
    elcetronic_devices = [{"name": "Universal charger", "weight": 12, "brand": "Lenovo"}, {"name": "smartphone", "weight": 6, "brand": "Apple"}, {"name": "Laptop", "weight": 60, "brand": "Dell"}, {"name": "Smartwatch", "weight": 44, "brand": "Samsung"}]

    accessory_items = [{"name": "Passport", "weight": 1, "origin": "USA"}, {"name": "Sunglasses", "weight": 10, "origin": "Italy"}, {"name": "Sneakers", "weight": 14, "origin": "Spain"}, {"name": "Campus", "weight": 4, "origin": "Unknown"}]
    store_inventory = Inventory()
    for item in elcetronic_devices:
        new_item = Electronic(item["name"], item["weight"], item["brand"])
        store_inventory.add_item(new_item)

    for item in accessory_items:
        new_item = Accessory(item["name"], item["weight"], item["origin"])
        store_inventory.add_item(new_item)
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