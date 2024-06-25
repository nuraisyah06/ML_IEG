a = 0b10101000
b = 0b01010100

#1
lowerbit = a | 0b1111
print(bin(lowerbit))

#2
print(bin(a | b))

#3
mask = 0b100010
print("Mask: ", bin(mask))
print("Result: ", bin(a | mask))