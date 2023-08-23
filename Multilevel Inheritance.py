class Superclass:
    def supermethod(self):
        print("Super Class Method Called")
class DerivedClass1(Superclass):
    def derivedmethod1(self):
        print("Derived Class 1 method called")
class DerivedClass2(DerivedClass1):
    def derivedmethod2(self):
        print("Derived Class 2 method called")
d2=DerivedClass2()
d2.supermethod()
d2.derivedmethod1()
d2.derivedmethod2()
