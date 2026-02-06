class Bank:

    def __init__(self, acc, addrs):
        self.acc=acc
        self.addrs=addrs
    def get_details(self):
        return self.acc,self.addrs

b1=Bank("2373382",'hyd')
print(b1.get_details())
    



