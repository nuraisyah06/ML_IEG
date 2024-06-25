x = 0b10101100
y = 0b11011001

print(bin(0b1111))

if (y & 0b1 == 1):
    print("y is odd number")
else:
    print("y is even number")

print(bin(x & 0b00001111))

if(y >> 4) & 1 == 1:
    print("y is set")
else:
    print("y is not set")
