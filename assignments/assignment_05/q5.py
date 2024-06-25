import random

computer = random.randint(1,100)

while True:
    user = int(input("Enter a number beteen 1 - 100 to guess:"))

    if user > computer:
        print("Too high")
    elif user < computer:
        print("Too low")
    else: 
        print("Your guess is correct!")
        break