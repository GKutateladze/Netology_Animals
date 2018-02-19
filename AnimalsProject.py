#  improved with PEP8

class Animal:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class TwoLegs(Animal):
    def __init__(self, name, legs=2):
        super().__init__(name)
        self.legs = legs

    def bird(self):
        print(self.name, "has", self.legs, "legs.")


class FourLegs(Animal):
    def __init__(self, name, legs=4):
        super().__init__(name)
        self.legs = legs

    def cattle(self):
        print(self.name, "has", self.legs, "legs.")


duck = TwoLegs("Duck")
chicken = TwoLegs("Chicken")
goose = TwoLegs("Goose")
duck.bird()
chicken.bird()
goose.bird()

cow = FourLegs("Cow")
goat = FourLegs("Goat")
pig = FourLegs("Pig")
sheep = FourLegs("Sheep")
cow.cattle()
goat.cattle()
pig.cattle()
sheep.cattle()
