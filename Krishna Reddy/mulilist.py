class Student:
    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks
    def display_info(self):
        print(f"name: {self.name} and age: {self.age} and marks: {self.marks}")

    def get_result(self):
        if self.marks > 40:
            return "PASS"
        else:
            return "FAIL"

students = []

while True:
    n = input("Enter name: ")
    age = int(input("Enter age: "))
    marks = int(input("Enter marks: "))

    s1 = Student(n, age, marks)
    students.append(s1)

    print("Result:", s1.get_result())

    g = int(input("Enter 0 to exit, any other number to continue: "))
    if g == 0:
        break

print("\n--- Student Records ---")
for s in students:
    s.display_info()
   
    #print("Result:", s.get_result())



print("totol no of students:",len(students))

