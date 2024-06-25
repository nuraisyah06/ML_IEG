firstName = "Khairi"
lastName = "Abu Bakar"
#to add to string se "string concatenation"
fullName = firstName + " " + lastName
print(fullName)

carPlate = "NAR"
number = 1106
#cannot add string and number
#convert int to string using str function
carPlateNumber = carPlate + str(number)
print(carPlateNumber)

#when string multiply with integer
#it ill have "times" effect
product = "cookies"
print(product * 5)
print("#" * 50)

# strings/ str are enclosed with double quote " " or single quote ' '
# to print output in seperate line, use \n, called escape character
# \t is to tab ke
# \r to carriage return

message = "You are invited to \n engagement of \n Aisyah \t & \t Izzat \non Sept 14th"
print(message)

#to ignore the escape space use extra \\
myfile = "c:\\nefolder\\table\\read.txt"
print(myfile)
# or, use  special string, raw string
myfile = r"c:\newfolder\table\read.txt"
print(myfile)

# relationship between string and list
# strings are list of characters
myGreeting = "Hello World"
print(myGreeting[0])
print(myGreeting[0:6])
print(myGreeting[::2])
print(myGreeting[::-1]) # to reverse
# how many characters in myGreeting
print(len(myGreeting))

#reverse the given number
givenNumber = 98654
#conver to string and reverse
# strGivennumber = str(givennumber)
# print(int(strGivennumber[::-1]))

# also can write in one line
print(int(str(givenNumber[::-1])))

# literals are objects
# "Television" is a string literal / string value
# "Television" is also called string object
# Objects have functions inside
product = "Television Cloths Vegetables Fruits"
print(product.split())
# split fx take literal assigned to the variable
# product split them tokenize them into multiple words
# using space as seperator
# it will return more than 1 word and going to be lists of words
# fx inside the object called "Method"
# print is a function
# where as "split is a method"



