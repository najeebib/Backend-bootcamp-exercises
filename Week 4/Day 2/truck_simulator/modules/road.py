class Road:
    def __init__(self, name, terrain_hardness, mental_effect, wheel_damage_effect):
        self._name = name
        self._terrain_hardness = terrain_hardness
        self._mental_effect = mental_effect
        self._wheel_damage_effect = wheel_damage_effect

    def get_name(self):
        return self._name
    
    def get_terrain_hardness(self):
        return self._terrain_hardness
    
    def get_mental_effect(self):
        return self._mental_effect
    
    def get_wheel_damage_effect(self):
        return self._wheel_damage_effect