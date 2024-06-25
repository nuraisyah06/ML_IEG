brand = int(input("Enter branding expenses \n"))
travel =  int(input("Enter travel expenses \n"))
food =  int(input("Enter food expenses \n"))
logistic =  int(input("Enter logistic expenses \n"))

total = brand + travel + food + logistic

brandper =(brand / total) * 100
travelper = (travel / total) * 100
foodper = (food / total) * 100
logper = (logistic / total) * 100

print(f"Total expenses : Rs. {total:.2f}")
print(f"Brand expenses percentage : {brandper:.2f}%")
print(f"Travel expenses percentage : {travelper:.2f}%")
print(f"Food expenses percentage : {foodper:.2f}%")
print(f"Logistic expenses percentage : {logper:.2f}%")