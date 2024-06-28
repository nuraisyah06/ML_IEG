num = int(input("Enter a number to make multiplication table: "))

for i in range(12):
    no = i + 1
    multi = num * no
    print(f"{no} x {num} = {multi}")
    
