principalAmount = float(input("Enter a principal amount: "))
rateOfInterest = float(input("Enter a rate of interest: "))
timeInYears = float(input("Enter a time in year: "))

simpleInterest = (principalAmount * rateOfInterest * timeInYears) / 100

print(f"The simple interest is {simpleInterest}")