#1st method
import mymodule
print("Interest:", mymodule.simpleInterest(1000, 1, 6))

#second method
from mymodule import simpleInterest
print("Interest:", simpleInterest(1000, 1, 6))      # better

#3rd method
from mymodule import *

print("Interest: ", simpleInterest(1000, 1, 6))
print("Result: ", add(10, 20))
