class OutOfRangeError(ValueError):
    pass


class Errors: pass


class InvalidSyntax(Errors): pass


class Animal:
    def __init__(self, age, sex, weight):
        self.age = age
        self.sex = sex
        self.weight = weight


class Giraffe(Animal):
    def __init__(self, age, sex, weight, height, food, healthcare):
        Animal.__init__(self, age, sex, weight)
        self.height = height
        self.food = food  # score between 0 and 100 (typ int)
        self.healthcare = healthcare  # score between 0 and 10 (type float)

    def get_height(self):
        return self.height

    def add_food(self, foo):
        self.food += foo
        return self.food

    def get_daily_check(self):
        if self.healthcare < 5.0:
            print("Call the vet immediately")
        if self.food < 50:
            print("Give him some supplements")
        else:
            if self.food < 75:
                if self.weight < 200:  # above the animal should do a diet
                    print("Give him some supplements")


class Elephant(Animal):
    def __init__(self, age, sex, weight, name, species, origin, children):
        Animal.__init__(self, age, sex, weight)
        self.name = name
        self.species = species
        self.origin = origin
        self.children = children  # a list with the names of the children

    def new_birth(self, name):
        self.children = self.children + [name]
        print(self.name, "gave birth to", name)
        return (0)

    def get_children(self):
        return self.children

    def presentation(self):
        print("I am ", self.name, " and I am a ", self.species, " elephant from", self.origin)
        return (0)


if __name__ == "__main__":
    Animal1 = Giraffe(13, "female", 120, 5.2, 70, 4.0)
    Animal2 = Elephant(12, "male", 300, "Dumbo", "African", "Congo", "ch")
    print("What Animal1 need today ?")
    print(Animal1.get_daily_check())
    print("What is Animal2 ?")
    print(Animal2.presentation())
