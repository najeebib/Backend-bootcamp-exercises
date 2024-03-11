from utils import load_roads
class Traversal_calculator:
    def __init__(self):
        self.roads = load_roads()

    def can_travel(self, truck, distance, road):
        if road in self.roads:
            return self.roads[road](distance, truck)
        else:
            print("Road not found")
            return False