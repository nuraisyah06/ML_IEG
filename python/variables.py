#to differentiate variable from vale can use "" or ''
#after = is call, parameter/arguments
product = 'Television'  #string can use "" or ''
quantity = 2  #integer
price = 1455.25 #float
available = True #boolean value/literal
print("Product:", product)
print("Quantity:", quantity)
print("Price: RM", price)
print("Availability:", available)

#type funtion tells the data type of the variable (dynamicall assigned by python)
#inner function jalan dulu
#function(call function(variable))
print(type(product))
print(type(quantity))
print(type(price))
print(type(available))

total = quantity * price
print("Total: RM", total)

quantity = "10"
print(type(quantity))

#type casting
#to convert data type
#to conver string to integer, use function int
#to convert string to float, use function float
total = int(quantity) * float(price)
print(total)

x = 100
print(x)
# to know location of the value x
# create a function called id
print(id(x))

y = 100
# if the content value already exist python will use the same address/id 
print(id(y))

a = "hello everyone!"
b = "hello everyone!"
print(id(a))
print(id(b))

# assign 2 different value to 2 different variable
x, y = 101, 102

#also can do this
x, y = 101 + 1, 102 + 1
x, y = x + 1, y + 1
print(x, y)

#multiple variable to a single value also can but NOT ALLOWED!
#x, y = 105

#other language has variable initialization / declare
#but python, need to be assign to a value
y = 0 #numeric initialization
y = "" #string initialization / empty string
y = None 
print(type(y))