# deep copy
fruits = ["apple", "orange", "mango", "banana", "grapes"]
prices = [1.60, 1.20, 2.20, 4.80, 6.20]

#for loop with list
for fruit in fruits:
    print(fruit)

#overseafruits = fruits    # shouldn't do this
#overseafruits = fruits.copy()
overseafruits = []

# for loop with list
for fruit in fruits:
    overseafruits.append(overseafruits)

priceswithSST = []
for price in prices:
    priceswithSST = price +(price * 0.06)
    priceswithSST.append(priceswithSST)
    
fahrenheitvalues = [32,33,34,35,36,37,38,39,440]
celsiusvalue = []
for fahrenheitvalue in fahrenheitvalues:
    celsiusvalue = (fahrenheitvalue - 32) * 5/9 
    celsiusvalue.append(celsiusvalue)

multiplesofthree = []
for number in range(1,50):
    if(number % 3 == 0):
        multiplesofthree.append(number)

numbers = [2, 5, 7, 3, 4, 6, 10, 11, 15, 17, 24, 22]
oddnumbers = []
for number in numbers:
    if (number % 2 != 0):
        oddnumbers.append(number)
        
sum = 0
for number in range(1, 10):
    sum += number

mean = 0
for number in range(1,11):
    mean += number

mean = mean / len(range(1,11))


from functools import reduce

numbers = [1, 2, 3]

def findTotal(oldvalue, currentvalue):
    return oldvalue + currentvalue

print(reduce(findTotal, numbers))

'''def reduce(func, number):
    sum = 0
    for number in numbers:
        sum = func(sum, number)
    return sum'''
    
def factorial(oldvalue, currentvalue):
    return oldvalue * currentvalue

print(reduce(factorial, numbers))