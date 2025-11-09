"""
I don't like writing classes like this:

class Animal:
    def __init__(self, name, species, age, health, weight, color):
        self.name = name
        self.species = species
        self.age = age
        self.health = health
        self.weight = weight
        self.color = color
Give me the power to create a similar class like this:

Animal = make_class("name", "species", "age", "health", "weight", "color")
"""


def make_class(*attributes):
    class DynamicClass:
        def __init__(self, *args):
            if len(args) != len(attributes):
                raise ValueError(f"Expected {len(attributes)} arguments, got {len(args)}")

            for attr, value in zip(attributes, args):
                setattr(self, attr, value)

        def __repr__(self):
            attr_values = ', '.join(f"{attr}={getattr(self, attr)!r}" for attr in attributes)
            return f"{self.__class__.__name__}({attr_values})"

    return DynamicClass

# Teste

class Animal:
    def __init__(self, name, species, age, health, weight, color):
        self.name = name
        self.species = species
        self.age = age
        self.health = health
        self.weight = weight
        self.color = color

Animel = make_class("name", "species", "age", "health", "weight", "color")

dog1 = Animal("Bob", "Dog", 5, "good", "50lb", "brown")
dog2 = Animel("Bob", "Dog", 5, "good", "50lb", "brown")

print(dog1.name)
print(dog2.name)