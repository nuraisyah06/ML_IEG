x = 0
y = 1

num = 0
print("Fibonacci series: ", x, y, end = " ",)
for count in range(1, 9):
    num = x + y
    x = y
    y = num
    print(num, end = ' ')