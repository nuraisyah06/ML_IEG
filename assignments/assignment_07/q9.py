'''
Write a Python class BankAccount with attributes like accountNumber, openingBalance, 
currentBalance dateOfOpening and customerName. 
Add methods like deposit, withdraw, and checkBalance.
'''

class BankAccount:
    
    def __init__(self, accountNumber, openingBalance, dateOfOpening, customerName):
        self.accountNumber = accountNumber
        self.openingBalance = openingBalance
        self.currentBalance = openingBalance
        self.dateOfOpening = dateOfOpening
        self.customerName = customerName
        
    def keyboardInput(self, datatype, caption, errorMessage, defaultValue = None):
        value = None
        isInvalid = True
        while(isInvalid):
            try:
                if defaultValue == None:
                    value = datatype(input(caption))
                else:
                    value = input(caption)
                    if(value.strip() == ""):
                        value = defaultValue
                    else:
                        value = datatype(value)
            except:
                print(errorMessage)
            else:
                isInvalid = False
        return value

    def Deposit(self, amount):
        if amount > 0:
            self.currentBalance += amount
            print(f"You have deposited {amount}. Current balance is RM {self.currentBalance}")
        else:
            print("Invalid amount. Please enter a positive number")
    
    def Withdraw(self, amount):
        if amount > 0 and amount <= self.currentBalance:
            if amount % 20 == 0 or amount % 50 == 0:
                self.currentBalance -= amount
                print(f"Withdrew {amount}. New balance is {self.currentBalance}")
            else:
                print("Withdrawal amount must be a multiple of 20 or 50.")
        else:
            print("Insufficient balance.")
            
    def CheckBalance(self):
        print("Your current balance is RM", self.currentBalance)
                
    def authenticate(self, accountNumber, customerName):
        return self.accountNumber == accountNumber and self.customerName == customerName
    
    def Menu(self):
        choice = -1
        while (choice != 0):
            print("**************************")
            print(":    1. Deposit          :")
            print(":    2. Withdraw         :")
            print(":    3. Check Balance    :")
            print(":    0. Exit             :")
            print("**************************")
                
            choice = self.keyboardInput(int, "Choice [0, 1, 2, 3]: ", "Choice must be integer")
            if (choice == 0):
                print("Thank You for using our system")
            elif (choice == 1):
                amount = self.keyboardInput(float, "Enter amount to deposit: ", "Invalid amount. Please enter a number.")  
                self.Deposit(amount)
            elif (choice == 2):
                amount = self.keyboardInput(float, "Enter amount to deposit: ", "Invalid amount. Please enter a number.")                
                self.Withdraw(amount)
            elif (choice == 3):
                self.CheckBalance()
            else:
                print("Invalid choice. Please choose available menu only.")
         
account = BankAccount(123456, 1000.0, "2023-07-09", "Aisyah")
 
if account.authenticate(123456, "Aisyah"):
    account.Menu()
else:
    print("Invalid account number or customer name. Please try again.")