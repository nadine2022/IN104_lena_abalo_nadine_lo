class OutOfRangeError(ValueError):
    pass

class Animal:
    def __init__(self,age,sex,weight):
        self.age=age
        self.sex=sex
        self.weight=weight

class Giraffe(Animal):
    def __init__(self, age,sex, weight, height,food,healthcare):
        Animal.__init__(self,age,sex,weight)
        self.height=height
        self.food=food #score between 0 and 100 (typ int)
        self.healthcare=healthcare #score between 0 and 10 (type float)

    def get_height(self):
        if self.height<0:
            raise OutOfRangeError('Height must be a positive number')
        return self.height
    
    def add_food(self, foo):
        self.food += foo
        return self.food

    def get_daily_check(self):
        if not(0<=self.food<=100):
            raise OutOfRangeError('Food must be between 0 and 100')
        if self.healthcare<5.0:
            print("Call the vet immediately")
        if self.food<50 :
            print("Give him some supplements")
        else:
            if self.food<75:
                if self.weight<200: #above the animal should do a diet
                    print("Give him some supplements")


