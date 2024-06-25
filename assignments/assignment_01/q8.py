P = float(input("Enter a principal amount: "))
R = float(input("Enter a rate of interest: "))
t = float(input("Enter a time in year: "))
n = float(input("Enter a number of times interest compounded per year: "))

# calculate the compound interest
A = P * ( 1 + R / ( 100 * n )) * (n * t)

print(f"The compound interest is {A:.2f}")