'''Parse and evaluate simple math word problems returning the answer as an integer.
What is 5?    -> 5
What is 5 plus 13?    -> 18
What is 7 minus 5?    -> 2
What is 6 multiplied by 4?     -> 24
What is 25 divided by 5?       -> 5
What is 5 plus 13 plus 6?      -> 24
What is 3 plus 2 multiplied by 3?       -> 15'''

import re

string = "What is 3 plus 2 divided by 3???"

string_split = string.split()
string_int = []
operations = []

for word in string_split:
    
    if word == "plus":
        operations.append("+")
    elif word == "minus":
        operations.append("-")
    elif word == "multiplied":
        operations.append("*")
    elif word == "divided":
        operations.append("/")
        
    word_cleaned = re.sub(r'\D', '', word)
    if word_cleaned:
        try:
            num = int(word_cleaned)     #to convert string to integer
            if num >= 0:
                string_int.append(num)
        except ValueError:              # if the word is not integer
            continue

print(f"Integers: {string_int} \nSymbol: {operations}")

if len(string_int) > 1 and len(operations) > 0:
    result = string_int[0]
    for i in range(1, len(string_int)):
        if i - 1 < len(operations):
            if operations[i - 1] == "+":
                result += string_int[i]
            elif operations[i - 1] == "-":
                result -= string_int[i]
            elif operations[i - 1] == "*":
                result *= string_int[i]
            elif operations[i - 1] == "/":
                result //= string_int[i]
                
    print(f"Result of calculation: {result}")


