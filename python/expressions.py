# Arithmetic Operators
x = 7
y = 2
# print function takes expression as the arguments
print("Addition: ", x + y)
print("Sbtraction: ", x - y)
print("Multiplication: ", x * y)
print("Division: ", x / y)

print("Quotien:", x // y)
print("Remainder: ", x % y)

print("Exponent: ", 10 ** 3)
print("The maximum number in a 64 bit env: ", (2 ** 64) - 1)

# Assignment Operators
x = 100
x += 1  # x = x + 1
x += 2
x += 5
x += x + 1 # x = x + x + 1

print(x)

x -= 1  # x = x - 1
x *= 1  # x = x * 1
x /= 1  # x = x / 1
x //= 1 # x = x // 1
x %= 1  # x = x % 1

# Comparison Operators
myHeight = 5.2
yourHeight = 5.3
mySisterHeight = 5.2

# Let us create TRUE statements
print(yourHeight > myHeight) #greater than
print(myHeight == mySisterHeight) #equals to
print(mySisterHeight < yourHeight) #less than
print(myHeight != yourHeight) #not equals to

print(yourHeight >= myHeight) #greater than or equals to
print(myHeight >= mySisterHeight)

print(myHeight <= yourHeight) #less than or equals to
print(mySisterHeight <= myHeight)

a = 21
b = 14
c = 7

print(a > b and a > c) # a is the greatest number
print(c < a and c < b) # a is the smallest number

print(b > c and b < a) #b is the middle number

print((b > c and b < a) or (b < c and b > a)) #b is the middle number

#Negation Operator
print(not (a > c)) #False
print(not (a < c)) #True

#Truth Table
#XOR ^
print((a > c) ^ (a > b))


