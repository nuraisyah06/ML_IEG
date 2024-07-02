class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def add(self):
        return self.x + self.y
    
    def subtract(self):
        return self.x - self.y

    
mycalculator = Calculator(10, 20)
print(mycalculator.add())
print(mycalculator.subtract())

class Utility:
    def add(x,y):
        return x + y
    
    def subtract(x,y):
        return x - y

print(Utility.add(100, 200))

class Customer:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        
    def getFullname(firstname, lastname):
        return firstname + lastname
    
    def __str__(self):
        return Customer.getFullname(self.firstname, self.lastname)
    
myCustomer = Customer("John", "David")
print(myCustomer)