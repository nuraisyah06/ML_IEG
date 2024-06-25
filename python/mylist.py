'''there are 4 different types of builtin structure in python
list, tuple, set and dictionary

list uses []
- modifiedable (append, edit and delete)
- ordered (the items retain at its position)
- list index star with 0 (0, 1, 2, 3, ...)
- allows duplicate
'''

fruits = ["apple", "orange", "mango", "banana", "durian", "grapes", "rambutan", "mangosteen"]

print(fruits)

#update
fruits[5] = "coconut"
print(fruits)

#remove from list
fruits.remove("mangosteen")
print(fruits)

#remove last item from list using pop function
fruits.pop()
print(fruits)

#delete item by index
#using keyord del
del fruits[3]
print(fruits)

#to remove all item( clear the list)
fruits.clear()
print(fruits)       # the list/ array still there, just the items inside is deleted

# to delete entire thing
del fruits
#print(fruits)

fruits = ["apple", "orange", "apple", "mango", "banana", "durian", "grapes", "mango", "apple"]
print(fruits.index("mango"))

newfruit = fruits[2:]
print(fruits.index("mango") + 1)

print(list(enumerate(fruits)))

for item in enumerate(fruits):
    if item[1] == "mango":
        print("Mango is in position:", item[0])

print("Total number of apples: ", fruits.count("apple"))

#to sort items in the list
fruits.sort()
print(fruits)

#to reverse items in the list
fruits.reverse()
print(fruits)

print("\n","*-" * 50)
count = 0
for fruit in fruits:
    if (fruit == "apple"):
        count += 1
        if count > 2:
            print("HEYO")
        else:
            print("MEH")

print("\n","*-" * 50)

#shallow copy
x = [10,20,30,40,50]
y = x
print(x)
print(y)
x[2] = 35
print(x)
print(y)

print("-" * 40)

#we want deep copy
x = [10,20,30,40,50]
y = []
for i in x:
    y.append(i)
print(x)
print(y)
x[2] = 35
print(x)
print(y)    

print("-" * 50)

x = [10,20,30,40,50]
y = x.copy()
print(x)
print(y)
x[2] = 35
print(x)
print(y)


def total(numbers):
    print(type(numbers))
    result = 0
    for number in numbers:
        result = result + number
    return result

x = [10,20,30,40,50]
print(x)
print(total(x))
print(x)

#list can auto explode
# explode is to create different variable for every item in the list
fruits = ["apple", "orange", "mango"]
fruit01 = fruits[0]
fruit02 = fruits[1]
fruit03 = fruits[2]
# in pyhton u can simplified the explode into this
fruit01, fruit02, fruit03 = fruits
