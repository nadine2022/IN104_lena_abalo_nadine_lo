#zoo1.py
class InvalidSyntax(ValueError) : pass
class InvalidData(ValueError) : pass

class Animal:
    def __init__(self,age,sex,weight):
        self.age=age
        self.sex=sex
        self.weight=weight


class Elephant(Animal):
    def __init__(self, age,sex, weight, name, species, origin, children):
        Animal.__init__(self,age,sex,weight)
        self.name=name
        self.species=species
        self.origin=origin
        self.children = children #a list with the names of the children
        
    def new_birth(self,name):

        if isinstance(name,str)==False:
            raise InvalidSyntax("the name should be a string")
        if name=="":
            self.children=[]
        else:
            self.children = self.children + [name]
        #print (self.name, "gave birth to", name)
        #return (0)

    def get_children(self):
        return self.children
        
        
    def presentation(self):

        if self.species not in ("Asian","African"):
            raise InvalidData("Just two species exist : Asian and African")

        if (self.age<0) or (isinstance(self.age,int)==False):
            raise InvalidData("age is a positive int")
        
        print ("I am ", self.name, " and I am a ", self.species, " elephant from", self.origin)
        self.age+=1
        print("Today is my birthday, so I am",self.age)
        return (0)



