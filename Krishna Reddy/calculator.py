# create a class with name calculator
#initialize two variables a,b on object creation 
# create methods for sum,substraction,division, multiplication
# create a program which will show promp:
#enter a :
#enter b :
#press 1 for addition 
#press 2 for substraction 
#press 3 for multiplication
#press 4 for division
#press  0 for restart
#press other key to exit 


class Calculator:

   
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def sum(self):
        return self.a + self.b
    def subtraction(self):
        return self.a - self.b
    def multiplication(self):
        return self.a * self.b
    def division(self):
        return self.a / self.b


while True:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))

    calc = Calculator(a, b)

    print("\nPress 1 for addition")
    print("Press 2 for subtraction")
    print("Press 3 for multiplication")
    print("Press 4 for division")
    print("Press 0 for restart")
    print("Press any other key to exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Addition:", calc.sum())

    elif choice == "2":
        print("Subtraction:", calc.subtraction())

    elif choice == "3":
        print("Multiplication:", calc.multiplication())

    elif choice == "4":
        if b != 0:
            print("Division:", calc.division())
        else:
            print("Error: Division by zero")

    elif choice == "0":
        continue   # restart the program

    else:
        print("Exiting program...")
        break
