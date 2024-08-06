class BankAccount:
    
    def __init__(self, account_number, opening_balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.opening_balance = opening_balance
        self.current_balance = opening_balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name
        
    def keyboard_input(self, datatype, caption, error_message, default_value=None):
        value = None
        is_invalid = True
        while is_invalid:
            try:
                if default_value is None:
                    value = datatype(input(caption))
                else:
                    value = input(caption)
                    if value.strip() == "":
                        value = default_value
                    else:
                        value = datatype(value)
            except:
                print(error_message)
            else:
                is_invalid = False
        return value

    def deposit(self, amount):
        if amount > 0:
            self.current_balance += amount
            print(f"You have deposited {amount}. Current balance is RM {self.current_balance}")
        else:
            print("Invalid amount. Please enter a positive number")
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.current_balance:
            if amount % 20 == 0 or amount % 50 == 0:
                self.current_balance -= amount
                print(f"Withdrew {amount}. New balance is RM {self.current_balance}")
            else:
                print("Withdrawal amount must be a multiple of 20 or 50.")
        else:
            print("Insufficient balance.")
            
    def check_balance(self):
        print("Your current balance is RM", self.current_balance)
                
    def authenticate(self, account_number, customer_name):
        return self.account_number == account_number and self.customer_name == customer_name
    
    def menu(self):
        choice = -1
        while choice != 0:
            print("**************************")
            print(":    1. Deposit          :")
            print(":    2. Withdraw         :")
            print(":    3. Check Balance    :")
            print(":    0. Exit             :")
            print("**************************")
                
            choice = self.keyboard_input(int, "Choice [0, 1, 2, 3]: ", "Choice must be an integer")
            if choice == 0:
                print("Thank You for using our system")
            elif choice == 1:
                amount = self.keyboard_input(float, "Enter amount to deposit: ", "Invalid amount. Please enter a number.")
                self.deposit(amount)
            elif choice == 2:
                amount = self.keyboard_input(float, "Enter amount to withdraw: ", "Invalid amount. Please enter a number.")
                self.withdraw(amount)
            elif choice == 3:
                self.check_balance()
            else:
                print("Invalid choice. Please choose an available menu option.")

# Create an instance of BankAccount
account = BankAccount(123456, 1000.0, "2023-07-09", "Aisyah")
 
if account.authenticate(123456, "Aisyah"):
    account.menu()
else:
    print("Invalid account number or customer name. Please try again.")
