count = int(input("Enter the number of Armstrong Number to generate: "))

armstrong = []
num = 1

while len(armstrong) < count:
    num_str = str(num)
    num_digits = len(num_str)

    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)

    if num == sum_of_powers:
        armstrong.append(num)

    num += 1

print(f"The first {count} Armstong numbers are: {armstrong}")