# function can have inner function

def sum(a, b):
    return a + b

x = 10
            
def authenticate(username, password):                   # Outer function
    def calculateSI(principle, period, rate):           # Inner function
        result = (principle * period * rate) / 100
        return result
    if (username == "admin" and password == "pwd123"):
        # call th einner function in outer function block
        # print("Simple Interest : ", calculateSI(1000, 1, 6))
        return calculateSI # address of the function is located
    
authenticate("admin", "pwd123")
# cannot cal inner funtion just like this
#calculateSI(1000, 1, 6) 

# Annonymous function assigned to a variable = functions without name
# 
''' sum = def (a,b)
            return a + b'''
            
add = lambda a, b: a + b
fahrenheitvalues = [32, 33, 34, 35, 36, 37, 38, 39, 40]
def fahrenheitToClesius(fahrenheitvalue):
    return (fahrenheitvalue - 32) * 5/9

celsiusvalues = map(fahrenheitToClesius, fahrenheitvalues)
print(list(celsiusvalues))

#using lambda function
'''
Step 1: Create annonymous function
def (fahrenheitvalue): return (fahrenheitvalue - 32)* 5/9
Step 2: Assign to a variable
fahrenheitToCelsius = def (fahrenheitvalue): return (fahrenheitvalue - 32)* 5/9
Step 3: Renaame def to lambda 
fahrenheitToCelsius = lambda (fahrenheitvalue): return (fahrenheitvalue - 32)* 5/9
Step 4: remove() at parameter and return keywword
fahrenheitToCelsius = lambda fahrenheitvalue: return (fahrenheitvalue - 32)* 5/9

'''
celsiusvalues = map(fahrenheitToClesius, lambda value: (value - 32) * 5/9)
print(list(celsiusvalues))