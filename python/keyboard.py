# input function takes a single parameter (caption / question)
# input is always type string
# always stored the input in a variable
firstNumber = input("Please enter the first number: ")
print(firstNumber)
print(type(firstNumber))

secondNumber = input("Please enter the second number: ")
print(firstNumber + secondNumber) #string concatenation
print(int(firstNumber) + int(secondNumber)) #addition

numbers = input("Enter numbers to do Total:")
numberlist = numbers.split(",")
print(numberlist)

total = 0
for number in numberlist:
    #int function trim the string value that have space to integer
    total = total + int(number)
print(total)