import random

print("1 - Rock \t 2 - Paper \t 3 - Scissors")
player = int(input("Make your choice:"))

computer = random.randint(1,3)
result = ""
print(f"Computer Choice: {computer}")
if (player == 1 and computer == 1) or (player == 2 and computer == 2) or (player == 3 and computer == 3):
    result = "You're Tied"
elif (player == 1 and computer == 2) or (player == 2 and computer == 1):
    if player == 1:
        result = "YOU WIN!"
    else:
        result = "COMPUTER WIN!"
elif (player == 1 and computer == 3) or (player == 3 and computer == 1):
    if player == 1:
        result = "YOU WIN!"
    else:
        result = "COMPUTER WIN!"
elif (player == 2 and computer == 3) or (player == 3 and computer == 2):
    if player == 1:
        result = "YOU WIN!"
    else:
        result = "COMPUTER WIN!"
print(result)