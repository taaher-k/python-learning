#!

#Create a class Banking. Constructor to assign account balance. Create
#methods to deposit and withdraw. Minimum account balance should be
#Rs.500.


"""
class banking(self):
     def__if__()
    

     def assignevalue(self,acc)
 
"""



class Banking:
    def __init__(self, balance):
        # Constructor to assign account balance
        if balance < 500:
            print("Initial balance must be at least Rs.500. Setting balance to Rs.500.")
            self.balance = 500
        else:
            self.balance = balance

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited Rs.{amount}. Current Balance: Rs.{self.balance}")
        else:
            print("Deposit amount must be positive.")

    # Method to withdraw money
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif self.balance - amount < 500:
            print("Withdrawal denied. Minimum balance of Rs.500 must be maintained.")
        else:
            self.balance -= amount
            print(f"Withdrew Rs.{amount}. Current Balance: Rs.{self.balance}")

    # Method to check balance
    def check_balance(self):
        print(f"Current Balance: Rs.{self.balance}")



# --- Program Execution ---
account1 = Banking(1000)   # Initial balance Rs.1000
account1.deposit(500)      # Deposit Rs.500
account1.withdraw(700)     # Withdraw Rs.700
account1.withdraw(400)     # Attempt withdraw Rs.400 (should fail due to min balance)
account1.check_balance()   # Show balance
