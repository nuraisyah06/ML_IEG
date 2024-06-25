import sys

cmdarg = sys.argv
print(cmdarg)

total = 0
print("All elements: ")
for arg in cmdarg[1:]:
    ele = int(arg)
    total += ele

print(f"Average of all elements: {total/(len(cmdarg) - 1):.2f}")