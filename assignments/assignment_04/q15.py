input_binary = input("Enter a binary number: ")

decimal_num = 0
base = 1

for digit in input_binary[::-1]:
    if digit == '1':
        decimal_num += base
    base *= 2

print(f"Binary is {input_binary}, Decimal representation is {decimal_num}")