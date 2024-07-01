
def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
        
        
oddNum = [x for x in range(1, 1001) if x % 2 != 0]
oddNum.remove(oddNum[0])
oddPrime = [x for x in oddNum if isPrime(x)]
twinPrime = []

for i in oddPrime:
    if i + 2 in oddPrime:
        twinPrime.append((i, i + 2))
        
print(twinPrime)