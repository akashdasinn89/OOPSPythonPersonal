from abc import ABC,abstractmethod
class car(ABC):
    def mileage(self):
        pass
class tesla(car):
    def mileage(self):
        print("The mileage is 30kmph")
class maruti(car):
    def mileage(self):
        print("The mileage is 50kmph")
class Renault(car):
    def mileage(self):
        print("The mileage is 15kmph")
t=tesla()
t.mileage()
r=Renault()
r.mileage()
p=maruti()
p.mileage()