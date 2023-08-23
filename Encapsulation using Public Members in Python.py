class Person:
    def __init__(self, name, age, _id):
        self.name = name
        self.age = age
        self._id = _id


    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("ID:", self._id)



class Student(Person):
    def __init__(self, name, age, _id, marks):
        super().__init__(name, age, _id)
        self.marks = marks


    def display(self):
        super().display()
        print("Marks:", self.marks)
person=Person("Akash",25,12345)
student=Student("Jane",20,54321,97)
person.display()
student.display()