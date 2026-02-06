class A:
    def __init__(self):
        print("constructor_1")
class B(A):
    
    def __init__(self):
        super().__init__()
        print("constructor_2")
a=A()
b=B()
b1=B()
a1=A()
