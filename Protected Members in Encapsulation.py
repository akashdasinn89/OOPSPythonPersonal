## publc member Example in Encapsulation
class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Employee Name",self.name)
        print("Employee Age",self.age)
s=Employee("Akash",21)
s.display()