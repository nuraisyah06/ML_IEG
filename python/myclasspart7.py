# Multiple inheritance

class Card:
    def __init__(self) :
        pass
    def doSomething(self):
        print("Inside Card Class")
        
class AtmCard(Card):
    def __init__(self):
        pass
    def doSomething(self):
        print("Inside ATMCard Class")
        
class CreditCard(Card):
    def __init__(self):
        pass
    def doSomething(self):
        print("Inside Credit Card Class")
        
class DebitCard(Card):
    def __init__(self):
        pass
    def doSomething(self):
        print("Inside Debit Card Class")
        
class BankCard(AtmCard, CreditCard, DebitCard):
    def __init__(self):
        pass
    def doSomething(self):
        print("Inside Bank Card Class")
        
# create instance
bankCard = BankCard()
bankCard.doSomething()
































''' Biggest Conclusion
Every class created in Python is inherite from a class called object
class object:
    def __init__():
        pass
    def __str__():
        print(memory address)
        
'''
#class Student(object):
class Student:
    def __str__ (self):
        return "Student"
    
class Alumni(Student):
    pass
    #def __str__(self):
        #return "Alumni"
        
alumni = Alumni()
print(alumni)

