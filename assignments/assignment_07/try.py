import re

string = "What is 5 plus 13?"

# Split the string into a list of words
string_split = string.split()
# Initialize an empty list to store integers
string_int = []
# Initialize the symbol variable
symbol = ""

# Iterate over the split strings
for word in string_split:
    # Check if the word is "plus" before cleaning
    if word == "plus":
        symbol = "+"
    
    # Remove non-numeric characters using regex
    word_cleaned = re.sub(r'\D', '', word)
    if word_cleaned:
        try:
            # Try to convert each cleaned word to an integer
            num = int(word_cleaned)
            if num >= 0:
                string_int.append(num)
        except ValueError:
            continue

# Perform the addition if the symbol is found and there are exactly two integers
if symbol == "+" and len(string_int) == 2:
    result = string_int[0] + string_int[1]
    print(f"{string_int[0]} + {string_int[1]} = {result}")

print("Split words:", string_split)
print("Integers found:", string_int)
