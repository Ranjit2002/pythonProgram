class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def show(self):
        print(f"Name: {self.name}\nSpecies: {self.species}")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, 'Dog')
        self.breed = breed

    def show(self):
        Animal.show(self)
        print(f"Breed: {self.breed}")


class GoldenRetriever(Dog):
    def __init__(self, name, color):
        super().__init__(name, 'Golden Retriever')
        self.color = color

    def show(self):
        Dog.show(self)
        print(f"Color: {self.color}")


a = GoldenRetriever('Tommy', 'Black')
a.show()
print(GoldenRetriever.mro())
