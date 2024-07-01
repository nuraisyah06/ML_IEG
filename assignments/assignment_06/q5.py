
def divisor(n):
    listDiv = []
    for i in range(1, n):
        if n % i == 0:
            listDiv.append(i)
    return listDiv

num = int(input("Enter a number to find their divisors: "))
print(divisor(num))
print(f"The sum of the proper divisors: {sum(divisor(num))}")