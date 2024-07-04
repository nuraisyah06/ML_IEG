name = str(input("Enter name: "))
n = int(input("Enter integer: "))

if n < len(name):
    result = name[:n] + name[n+1:]
else:
    result = "Invalid Input"

print(result)