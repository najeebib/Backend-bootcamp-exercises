class Astroid:
    def __init__(self, id, name, min_diameter, max_diameter, speed_kmh, miss_distance):
        # all the relevant astroid data
        self._id = id
        self._name = name
        self._min_diameter = min_diameter
        self._max_diameter = max_diameter
        self._speed_kmh = speed_kmh
        self._miss_distance = miss_distance

    def get_id(self):
        return self._id
    
    def get_name(self):
        return self._name
    
    def get_min_diameter(self):
        return self._min_diameter
    
    def get_max_diameter(self):
        return self._max_diameter

    def get_speed_kmh(self):
        return self._speed_kmh
    
    def get_miss_distance(self):
        return self._miss_distance
    
    def get_json(self):
        return {"id": self._id ,"name": self._name, "min_diameter": self._min_diameter, "max_diameter": self._max_diameter, "miss_distance": self._speed_kmh, "speed_kmh": self._miss_distance}