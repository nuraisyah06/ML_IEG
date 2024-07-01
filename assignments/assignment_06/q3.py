num = int(input("Enter a number to find their prime factors: "))

factors = []
prime = 2

while num > 1:
    while num % prime == 0:
        factors.append(prime)
        num //= prime
    prime += 1
    
print(factors)
    
