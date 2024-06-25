a = int(input("Enter 1st integer: "))
b = int(input("Enter 2nd integer: "))

gcd = 0

#remain = a % b

while (a > 0 and b > 0):
    if  a != 0:
        remain = a % b 
        print(f"GCD({a},{b}) =", end = " ")
        a = b
        b = remain
        gcd = b
    else:
        gcd = a
print(f"GCD({a},{b}) = {gcd}", end = " ")
    
