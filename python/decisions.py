#Find whether the number is +ve, -ve or zero
#Find whether business making profit, loss or breakeven

expenses = 1000
sales = 1100

# Objective 1: State whether we are making profit
if (sales > expenses):
    #block of code
    print("You are making Profit")

#Obective 2: State whether we are making profit or loss
if (sales > expenses):
    #block of code
    print("You are making Profit")
else:
    print("You are making losses!")

#Obective 3: State whether we are making profit or loss or breakeven
if (sales > expenses):
    #block of code
    print("You are making Profit")
else:
    if (sales == expenses):
        print("You are making breakeven")
    else:
        print("You are making losses!")

if (sales > expenses):
    #block of code
    print("You are making Profit")
elif (sales == expenses):
    print("You are making breakeven")
else:
    print("You are making losses!")

print("Thank You!")
    

# find whether the given number is even 
givenumber = 5 
# the block statement can be in the same line and not, as long as there is colon 
if (givenumber % 2 == 0): print("Even number")

# find whether the given number is even or odd 
print("Even number") if (givenumber % 2 == 0) else print("Odd number")

givenumber = 1
# find hether the number is +ve, -ve or 0
print("+ve") if (givenumber > 0) else print("-ve") if (givenumber < 0) else print("zero")

