''' Functions are used to organize code
    not for solving problems like operators, if, for, while

functions are created using keyword def, followed by fnctions name():

'''
def name():
    print("Aisyah")

def sayHello():
    print("Hello World!")

sayHello(), name()

print("=" * 50)

def greeting(name):
    print("Good day", name, "!!")

greeting("Aisyah")

print("=" * 50)

def total(x, y, z):
    result = x + y + z
    print("Result: ", result)

total(10, 20, 30)

print("=" * 50)

def buyLunch(eat, drink):
    prices = []
    for food in eat:
        if (food == "rice"):
            prices.append(2.00)     #append is a method
        elif (food == "chicken"):
            prices.append(3.50)

    for water in drink:
        if (water == "fruit juice"):
            prices.append(4.00)     #append is a method
        elif (water == "sky juice"):
            prices.append(1.50)
    #print(prices)
    return prices

itemprice = buyLunch(["rice", "chicken"], ["fruit juice", "sky juice"])
total = 0
for price in itemprice:
    total += price
print(f"Amount to be paid: RM {total:.2f}")
print("+" * 50)

# can make rate parameter as optional by aving default value
def calculateSimpleInterest (principle, period = 1, rate = 6):
    interest = (principle * period * rate) / 100
    return interest

print(calculateSimpleInterest(1000))
print(calculateSimpleInterest(1000, 3))

print("+" * 50)

def findTotal(givenNumber):
    total = 0
    for givenNum in givenNumber:
        total += givenNum
    return total
    
print(findTotal([10, 20, 30, 40]))
print(findTotal([10, 20, 30, 40, 50, 60]))

print("+" * 50)

def findTotal(*givenNumber):        #to accept all arguments, doesnt mind the quantity
    total = 0
    for givenNum in givenNumber:
        total += givenNum
    return total
    
print(findTotal(10, 20, 30, 40))
print(findTotal(10, 20, 30, 40, 50, 60))

print("+" * 50)

def listSixLetterFruit (*fruits):
    for fruit in fruits:
        if len(fruit) >= 6:
            print(fruit)
            
listSixLetterFruit("apple", "orange", "mango", "banana", "durian", "grapes", "rambutan", "mangosteen")


print("+" * 50)

def listSixLetterFruit (*fruits):
    for fruit in fruits:
        print(fruit)
            
listSixLetterFruit("apple", 20, 1.40, "orange", 8, 1.50, "mango", 3, 2.60)

