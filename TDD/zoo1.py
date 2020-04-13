class InvalidSyntax(ValueError):
    pass


class InvalidData(ValueError):
    pass


class Animal:
    def __init__(self, age, sex, weight):
        self._age = age
        self.sex = sex
        self.weight = weight

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if self._age < 0:
            raise Exception("age cannot be negative.")
        self._age = value


class Elephant(Animal):
    def __init__(self, age, sex, weight, name, species, origin, children):
        Animal.__init__(self, age, sex, weight)
        self.name = name
        self.species = species
        self.origin = origin
        self.children = children  # a list with the names of the children

    def new_birth(self, name):
        if not isinstance(name, str):
            raise InvalidSyntax("the name should be a string")
        if name == "":
            self.children = []
        else:
            self.children = self.children + [name]

    def presentation(self):
        if self.species not in ("Asian", "African"):
            raise InvalidData("Just two species exist : Asian and African")

        if (self.age < 0) or not (isinstance(self.age, int)):
            raise InvalidData("age is a positive int")

        print("I am ", self.name, " and I am a ", self.species, " elephant from", self.origin)
        self.age += 1
        print("Today is my birthday, so I am", self.age)
        return 0


if __name__ == '__main__':
    el = Elephant(12, "male", 300, "Dumbo", "European", "Congo", ["Simba", "Coco"])
    print(el.age)
