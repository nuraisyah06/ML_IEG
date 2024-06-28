'''def numToWord(num):
    if num == 0:
        return "zero"
    
    words = ""
    firstDigit = ["One", "Two","Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]
    teendigit = ["Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eightteen", "Nineteen"]
    tensdigit = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety" ]
    
    if num >= 1000:
        words += firstDigit[num // 1000-1] + "thousands"
        num = num % 1000
        
    if num >= 100:
        words += firstDigit[num // 100-1] + "hundreds"
        num = num % 100
    
    if num >= 10 and num <= 19:
        words += " and " + teendigit[num - 11] + " "
        num = 0
    elif num >= 20:
        words += " and " + tensdigit[num // 10]
        num %= 10
    
    if num >= 1 and num <= 9:
        words += firstDigit[num - 1] + " "
    return words
        
num = int(input("Enter a number to convert: "))

print(numToWord(num))
'''

def numToWord(num):
    if num == 0:
        return "zero"
    
    words = ""
    firstDigit = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    teenDigit = ["Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tensDigit = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    
    if num >= 1000:
        words += firstDigit[num // 1000 - 1] + " Thousand "
        num = num % 1000
        
    if num >= 100:
        words += firstDigit[num // 100 - 1] + " Hundred "
        num = num % 100
        if num > 0:
            words += "and "
    
    if num >= 11 and num <= 19:
        words += teenDigit[num - 11] + " "
        num = 0
    elif num == 10:
        words += "Ten "
        num = 0
    elif num >= 20:
        words += tensDigit[num // 10] + " "
        num %= 10
    
    if num >= 1 and num <= 9:
        words += firstDigit[num - 1] + " "
    
    return words.strip()

num = int(input("Enter a number to convert: "))
print(numToWord(num))
 
