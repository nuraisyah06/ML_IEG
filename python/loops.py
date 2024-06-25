fruits = ["apple", "orange", "mango", "grapes", "cempedak", "mangosteen", "durian", "rambutan", "lychee", "pear"]
# print items in a list
for fruit in fruits:
    print(fruit)
# print all the items in even position
for fruit in fruits[::2]:
    print(fruit)
print("-" * 30)
#print fruits ith 6 letters
for fruit in fruits:
    if(len(fruit) == 6):
        print(fruit)

#to print item together with the index(position)
position = 0
for fruit in fruits:
    print(position, fruit)
    position += 1
print("-" * 60)
# create multiplication of five
# until 12
multipliers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
multiplicant = 5
for multiplier in multipliers:
    print(multiplier, "x", multiplicant, "=", multiplier * multiplicant)
print("-" * 60)

''' this is not practical if the value is until hundreds
need to go for range option start_index:end_index
but the : (colon) operator only work on array
so, built in fucntion called range hich can generate list of numbers
range function takes start and end index and generates the number beteen the indexes ''' 
print(range(1, 12))
''' range is and iterabe object,
which means it can be use in for loop together ith "in" operator
'''
print("-" * 60)

multiplicant = 6
for multipler in (range(1, 13)):
    print(multipler, "x", multiplicant, "=", multipler * multiplicant)
print("-" * 60)

givennumber = 97409
while (givennumber > 0):
    print(givennumber % 10)
    # givennumber //= 10
    givennumber = givennumber // 10
print("-" * 60)

givennumber = 12345
numofdigit = len(str(givennumber)) - 1
while (givennumber > 0):
    print(givennumber // 10 ** numofdigit)
    givennumber %= 10 ** numofdigit
    numofdigit -= 1

print("-" * 60)

givennumber = 67891
strgivennumber = str(givennumber)
for digit in strgivennumber:
    print(digit)

# for loop and while loop can also have block
fruits = ["apple", "orange", "mango", "banana", "grapes"]
# code in else block ill get executed hen al the fruits are iterated
# iteration exhausted (no more product to iterate)
for fruit in fruits:
    print(fruit)
else: 
    print("All fruits printed")

for fruit in fruits:
    print(fruit)
    if (fruit == "mango"):
        break                   #to jump out of the loop/ stop the loop/ else block not executed
else: 
    print("All fruits printed")

print("=" * 60)

multiplicant = 9
multiplier = 1
while (multiplier <= 12):
    print(multiplier, "x", multiplicant, "=", multiplier * multiplicant)
    multiplier += 1

    if multiplier == 11:
        break
else:
    print("Multiplication table of 9 is completed")