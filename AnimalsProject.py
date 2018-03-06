class Animal:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return(self.name)


class Two_legs(Animal):
    def __init__(self, name, legs=2):
        super().__init__(name)
        self.legs = legs

    def bird(self):
        print(self.name, "has", self.legs, "legs.")


class Four_legs(Animal):
    def __init__(self, name, legs=4):
        super().__init__(name)
        self.legs = legs

    def cattle(self):
        print(self.name, "has", self.legs, "legs.")

duck = Two_legs("Duck")
chicken = Two_legs("Chicken")
goose = Two_legs("Goose")
duck.bird()
chicken.bird()
goose.bird()

cow = Four_legs("Cow")
goat = Four_legs("Goat")
pig = Four_legs("Pig")
sheep = Four_legs("Sheep")
cow.cattle()
goat.cattle()
pig.cattle()
sheep.cattle()
