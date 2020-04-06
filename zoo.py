class Animal:
    def __init__(self,age,sex,weight):
        self.age=age
        self.sex=sex
        self.weight=weight

class Giraffe(Animal):
    def __init__(self, age,sex, weight, height,food,healthcare):
        Animal.__init__(self,age,sex,weight)
        self.height=height
        self.food=food
        self.healthcare=healthcare

    def get_height(self):
        return self.height
    
    def get_daily_routine(self):
        print("You need to give them ", self.food," and ", self.healthcare)
        return(0)      

class Elephant(Animal):
    def __init__(self, age,sex, weight, name, species, origin):
        Animal.__init__(self,age,sex,weight)
        self.name=name
        self.species=species
        self.origin=origin
        
        
    def presentation(self):
        print ("I am ", self.name, " and I am a ", self.species, " elephant from", self.origin)
        return (0)

    def tusks(self):
        print("I have two tusks!")
        return(0)

if __name__=="__main__":
    Animal1=Giraffe(13,"female",120,5.2,"acacia","vaccine")
    Animal2=Elephant(12,"male",300,"Dumbo","African","Congo")
    print("What Animal1 need today ?")
    print(Animal1.get_daily_routine())
    print("What is Animal2 ?")
    print(Animal2.presentation())
