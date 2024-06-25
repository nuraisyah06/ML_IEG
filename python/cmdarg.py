# when call python to executed the program, the value pass to the program
# in command line, also called line arguments, 
# arguments are separated by space
# arguments for function are separated by comma

# sys.argv output is a list, which contains all the command line arguments
# passed to python
# in the list, the item at index 0 is the program filename
import sys

cmdarguments = sys.argv # using . (dot) operator to access the vaiable inside
print(cmdarguments)

# to find total number of all arguments
# use loop since, the total number of arguments are unknown
total = 0
for number in cmdarguments[1:]:
    total = total + int(number)
print(total)



