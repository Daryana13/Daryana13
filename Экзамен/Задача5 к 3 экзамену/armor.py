class Armor:

    def __init__(self, name, strength, weight):
        self.name = name
        self.strength = strength
        self.weight = weight

    def __repr__(self):
        return f"{self.name} has strength {self.strength} and its mass {self.weight} kg"
