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

    def get_height_neck(self):
        return self.height
    
    def get_daily_routine(self):
        print("You need to give them" self.food "and" self.healthcare)
        return(0)      



