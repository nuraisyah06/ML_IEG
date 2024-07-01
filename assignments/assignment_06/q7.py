def totalDivisor(i):
    sumDiv = 0
    for j in range(1, i):
        if i % j ==  0:
            sumDiv += j
    return sumDiv

def amicable(lower, upper):
    listAmicable = []
    
    for i in range(lower, upper + 1):
        sumDiv = totalDivisor(i)
        if sumDiv > i:
            sumDiv2 = totalDivisor(sumDiv)
            if sumDiv2 == i and sumDiv2 != sumDiv:
                listAmicable.append(i)
                listAmicable.append(sumDiv)
    return listAmicable

print(amicable(1, 1000))