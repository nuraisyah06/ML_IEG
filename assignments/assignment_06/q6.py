def is_perfect(n):
    divisor_sum = sum([i for i in range(1, n) if n % i == 0])
    return divisor_sum == n

def generate_perfnum(count):
    perfect_numbers = []
    num = 1

    while len(perfect_numbers) < count:
        if is_perfect(num):
            perfect_numbers.append(num)
        num += 1

    return perfect_numbers

count = int(input("Enter a number to generate perfect number: "))
perfect_numbers = generate_perfnum(count)
print("The first 4 perfect numbers:", perfect_numbers)