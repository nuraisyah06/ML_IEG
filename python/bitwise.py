# how to present binary numbers in python
# use 0b followed by the binary number
# but it's still an integer
# by adding 0b, pyhton will read is as binary number
# not as decimal number
ownerpermission = 0b111
print(ownerpermission)

filepermission = 0b111101001 
# now owner can read, write and execute
# group can read and execute
# others can execute only

# in data science/machine learning when you were given
# categorical data you must convert them to numbers
# which machine can understand
# this itself called "feature engineering"
# gender representation 01 for female or 10 for male
# race representation 1000 for malay and 0100 for chinese

# this bit extraction can be use using bitwise and operator
mask = 0b000111000
print((filepermission & mask) >> 3) # we manage to get group permission over the file
#print("{0:b}".format((filepermission & mask) >> 3))

# in order to perform bit extraction we use bitwise & operator
# we are interested in 4, 5, 6 bits only
# Original Data             111101001   &      #to extract certain bits
# Our Mask                  000111000
# 4,5,6 bits extracted      000101000
# shift it to right 3 times 000000101   >> 3
print(bin(filepermission & mask))

# Original Data             111101001   |      #to modify the bits
# Our Mask                  000111000
# 4,5,6 bits extracted      000101000
print(bin(filepermission | mask))
# The OR operator is used to set a specific bit to 1
# REMEMBER there is no way to set a specific bit to 0 using OR operator
# OR operator is used in extracting region of interest in images

# Original Data             111101001   ^
# Our Mask                  000111000
# 4,5,6 bits extracted      111010001
print(bin(filepermission ^ mask))
# XOR is used for encryption
message = 0b00101100    # my content "J"
key = 0b00101100        # encryption key ","
encrypted_message = message ^ key
print(bin(encrypted_message))

#1s complement
givennumber = 5
# 5                 0101
# 1s Complement     1010
print(~givennumber) #1s complement
# 2s Complement = 1s Complement + 1
print(~givennumber + 1) #2s complement
print(-givennumber)     # - unary negative
print(+givennumber)     # + unary negative


# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A,   B,  C,  D,  E,  F
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15  
hexadecimalnumber = 0xf
print(hexadecimalnumber)
print(hex(hexadecimalnumber))

# 0, 1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 13, 14, 15, 17, 20
# 0, 1, 2, 3, 4, 5, 6, 7, 8,   9, 10, 11, 12, 13, 14, 15, 16
