n = int(input(" Enter a number: "))

sum = 0

for num in range(1,n):
    sum += 1/num
float(sum)
print(f"The sum of the first {n} of the harmonic series {sum:.4f}")