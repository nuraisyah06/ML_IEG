






principle = int(input("Principle: "))
period = int(input("Period: "))


# Runtime Error
try:
    principle = int(input("Principle: "))
except ValueError:
    print("Error: Principle amount must be an Integer!")
    #principle = 1000
except Exception as e:
    print("Something went wrong", e)
else:
    print("All is well")
finally:
    print("Thank You")
    
    
period = int(input("Period: "))
rate = int(input("Rate: "))
interest = (principle * rate * period)
print("Interest Amount: ", interest)

