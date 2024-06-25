strNum = str(input("Enter list of string contains number seperated by comma"))

listStrNum = strNum.split(",")
listNum = []

for strNum in listStrNum:
    listNum.append(int(strNum))

