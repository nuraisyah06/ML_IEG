n = int(input("Enter a number to generate Collatz sequence: "))

while (n > 1):
    if n % 2 == 0:
        n = n/2
        print(n, end = " ")
    elif n % 2 != 0:
        n = 3*n + 1
        print(n, end = " ")
