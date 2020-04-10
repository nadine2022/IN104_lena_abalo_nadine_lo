class Animal:
    def __init__(self,age,sex,weight):
        self.age=age
        self.sex=sex
        self.weight=weight

class Giraffe(Animal):
    def __init__(self, age,sex, weight, height,food,health):
        Animal.__init__(self,age,sex,weight)
        self.height=height
        self.food=food #score between 0 and 100 (typ int)
        self.healthcare=healthcare #score between 0 and 10 (type float)

    def get_height(self):
        return self.height
    
    def get_daily_check(self):
        if self.health<5.0:
            print("Call the vet immediately")
        if self.food<50 :
            print("Give him some supplements")
        else:
            if self.food<75:
                if self.weight<200: #above the animal should do a diet
                    print("Give him some supplements")

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
    Animal1=Giraffe(13,"female",120,5.2,70,4.0)
    Animal2=Elephant(12,"male",300,"Dumbo","African","Congo")
    print("What Animal1 need today ?")
    print(Animal1.get_daily_check())
    print("What is Animal2 ?")
    print(Animal2.presentation())
