# Given number is 97531
# Reverse the number
# Expected result is 13579

reversed = 1 * 10000 + 3 * 1000 + 5 * 100 + 7 * 10 + 9
print(reversed)

a0 = 97531
result = a0 % 10
a1 = a0 // 10
print(result, a1)

result = (result * 10) + (a1 % 10)
a2 = a1 // 10
print(result, a2)

result = (result * 10) + (a2 % 10)
a3 = a2 // 10
print(result, a3)

result = (result * 10) + (a3 % 10)
a4 = a3 // 10
print(result, a4)

result = (result * 10) + (a4 % 10)
a5 = a4 // 10
print(result, a5)
print(result)

# Akmal Solution
print("--------")
result = (a0 % 10) * 10000
result = result + ((a0 // 10 ) % 10) * 1000
result = result + ((a0 // 100 ) % 10) * 100
result = result + ((a0 // 1000 ) % 10) * 10
result = result + ((a0 // 10000 ) % 10) * 1
print(result)

givenNumber = 97531
result = 0
result = result * 0 + (givenNumber % 10)      # 1
#givenNumber = givenNumber // 10  #9753
givenNumber //= 10 # 9753
result = result * 10 + (givenNumber % 10)
givenNumber //= 10 # 975
result = result * 10 + (givenNumber % 10)
givenNumber //= 10 # 97
result = result * 10 + (givenNumber % 10)
givenNumber //= 10 # 9
result = result * 10 + (givenNumber % 10)
givenNumber //= 10 # 0
result = result * 10 + (givenNumber % 10)

str_numbers = input()
str_numbers = str_numbers.split(",")
print(str_numbers)

numbers = [int(str_number) for str_number in str_numbers]
print(numbers)
numbers = map(int, str_numbers)
#print(list(numbers))
print(set(list(numbers)))