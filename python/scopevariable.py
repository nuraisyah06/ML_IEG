def add(a,b):
    # result is a local variable
    # a variable created inside the function
    # this variable cannot be accessed outside the function
    result = a + b
    return result

#print result
x = 10

def printX():
    print(x)
    
printX()

def modifyX():
    x = 15
    print("Inside modifyX",x)
    
modifyX()
print(x)

def traditionalModifyX():
    x = 20
    print("Inside TraditionalModifyX",x)
    return x
    
x = traditionalModifyX()
print(x)

def pythonModifyX():
    global x
    x = 25
    print("Inside the function(pthonModifyX): ", x)
    
pythonModifyX()
print(x)

def SimpleInterest(principle, period, rate):
    result = 0
    def printSimpleInterest():
        temp = 0
        print("Simple Interest:", result)
        print("Principle", principle)
        print("Period: ", period)
        print("Rate ; ", rate)
        
    result += 50
    result = (principle * period * rate)
    printSimpleInterest()
    print("Result: ", result)
    
SimpleInterest(1000, 1, 6)