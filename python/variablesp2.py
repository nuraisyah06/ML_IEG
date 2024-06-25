# multiple values assign to multiple variables
# x = 10
# x, y = 10, 11

#assign multiple values to a single variable
#array

fruits = ["apple", "orange", "mango", "banana", "grapes"]

# indexing and selection
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])
print(fruits[4])

# to know ho many item in the array, use len()
print("Number of items we have: ", len(fruits))

# to know maximum index of the array, - 1 from the len()
print("Max index is: ", len(fruits) - 1)

#index number can be negative,
# -1 index = last index, len() - 1 ## in python only
print(fruits[-1])
print(fruits[-2])
print(fruits[-3])
print(fruits[-4])
print(fruits[-5])
# also to retrieve index in reverse

# range, start_index:end_index
# the end_index is not included
print(fruits[1:3])
# to take index from the star unitl a limit
print(fruits[:4])
# to take index from a limit to the end
print(fruits[2:])

# 
fruits = ["apple", "orange", "mango", "grapes", "cempedak", "mangosteen"]


print(fruits[0:9:3]) # totake samples
# if there is plenty of data in the array, but doesnt need all data
# the selection must be evenly distributed

# in the range can have -ve numbers
print(fruits[-5:-1]) # position -1 is not included
print(fruits[-1:-5]) # -1 > -5, start index is bigger tan end index, so there's no list / empty list
# by default step up is 1 -1 + 1
print(fruits[-1:-5:-1]) # item in index -5 is not included
# to reverse entire list
print(fruits[::-1])



