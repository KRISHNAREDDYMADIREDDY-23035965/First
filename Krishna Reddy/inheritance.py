class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.tax="helloo"
    def getinfo(self):
        print(f"name: '{self.name}' and age: '{self.age},{self.tax}'")


student1 = Student("Krishna", 23)
student1.getinfo()
