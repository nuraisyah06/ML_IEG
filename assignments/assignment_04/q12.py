num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

result = 0

for i in range(num2):
    result += num1

print(f"Multiply of {num1} and {num2} is {result}")