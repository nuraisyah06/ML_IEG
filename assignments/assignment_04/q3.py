count = int(input("Enter the number of ADAM Numbers to generate: "))

adam_numbers = []
num = 1

while len(adam_numbers) < count:
    reversed_num = int(str(num)[::-1])      #Reversed the number
   
    orig_square = num * num
    rev_sq = reversed_num * reversed_num    #Calculate squares

    rev_orig_sq = int(str(orig_square)[::-1])

    if rev_orig_sq == rev_sq:
        adam_numbers.append(num)

    num += 1

print(f"The ADAM numbers generated are: {adam_numbers}")

