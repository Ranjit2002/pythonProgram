class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print(f"Sound made by the animal")


class Dog(Animal):
    def init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.name = name
        self.breed = breed

    def make_sound(self):
        print("Bark")


a = Dog('Dog', 'Dobber')
a.make_sound()

b = Animal("Cat", "Animal")
b.make_sound()
