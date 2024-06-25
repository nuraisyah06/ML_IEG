num = int(input("Enter a number: "))

binary_num = ""

while num > 0:
    remainder = num % 2
    binary_num = str(remainder) + binary_num
    num = num // 2

print(f"Decimal is {num} binary representation is {binary_num}")