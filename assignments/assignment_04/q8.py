'''Write a python program that takes few 
numbers as command line argument. Use a loop 
to display all elements. Use another loop to 
display all elements in the even position. 
Use another loop to display all elements in 
the odd position.'''

import sys

cmdarg = sys.argv
print(cmdarg)

print("All elements: ")
for arg in cmdarg[1:]:
    print(arg, end=' ')
print()

print("Elements in even position: ")
for item in range(1, len(cmdarg)):
    if item % 2 == 0:
        print(cmdarg[item], end=' ')
print()

print("Elements in odd position: ")
for item in range(1, len(cmdarg)):
    if item % 2 != 0:
        print(cmdarg[item], end=' ')