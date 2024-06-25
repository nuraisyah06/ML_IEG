binary = 1011

a1 = binary // 1000 * 2**3
print(a1)
a2 = binary // 100 % 10  * 2**2
print(a2)
a3 = binary // 10 % 100 * 2**1
print(a3)
a4 = binary % 10 * 2**0
print(a4)
print("Decimal represntation of binary 1011 is ",a1+a2+a3+a4)