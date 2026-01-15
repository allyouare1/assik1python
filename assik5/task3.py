class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if not name:
            raise ValueError("Name cannot be empty")
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age < 0:
            raise ValueError("Age cannot be negative")
        self.__age = age

    def info(self):
        return f"Person: {self.__name}, {self.__age} years old"


class Student(Person): 
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def info(self): 
        return f"Student: {self.get_name()}, {self.get_age()} years old, ID: {self.student_id}"


p = Person("Ali", 25)
s = Student("Amina", 17, "S-101")

objects = [p, s]
for obj in objects:
    print(obj.info())  