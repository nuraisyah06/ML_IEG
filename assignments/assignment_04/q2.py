''' 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, etc.
Note that 2 is the only even prime number. 
All other even numbers greater than 2 can be divided by 2, 
so they are not prime.'''

prime_number = 2
count = 0
for i in range(2,30):
    while count == 10:
        if prime_number % 2 != 0:
            prime_number = i
            count += 1

    print(prime_number)

givenNumbers = range(2,51)
count = 9
print("The first 10 Prime Number is ", end=" ")
print(1, end=" ")

for numbers in givenNumbers:
    isPrime = True
    divisors = range(2, numbers)
    for divisor in divisors:
        if numbers % divisor == 0:
            isPrime = False
            break
    if isPrime == True:
        print(numbers, end=" ")
        count -= 1
    if count == 0:
        break
