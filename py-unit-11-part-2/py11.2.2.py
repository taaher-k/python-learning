#2. Create a child class as Saving Account for Banking. Add method to
#calculate interest. For account balance greater than 25000, interest of
#6.5% should be added with account balance.




class Banking:
    def __init__(self, balance):
        # Constructor to assign account balance
        if balance < 500:
            print("Initial balance must be at least Rs.500. Setting balance to Rs.500.")
            self.balance = 500
        else:
            self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited Rs.{amount}. Current Balance: Rs.{self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif self.balance - amount < 500:
            print("Withdrawal denied. Minimum balance of Rs.500 must be maintained.")
        else:
            self.balance -= amount
            print(f"Withdrew Rs.{amount}. Current Balance: Rs.{self.balance}")

    def check_balance(self):
        print(f"Current Balance: Rs.{self.balance}")


# Child class SavingAccount
class SavingAccount(Banking):
    def calculate_interest(self):
        if self.balance > 25000:
            interest = self.balance * 0.065
            self.balance += interest
            print(f"Interest of Rs.{interest:.2f} added. New Balance: Rs.{self.balance:.2f}")
        else:
            print("Balance less than Rs.25000. No interest applied.")





# --- Program Execution ---
acc1 = SavingAccount(30000)   # Initial balance Rs.30000
acc1.check_balance()          # Show balance
acc1.calculate_interest()     # Apply interest
acc1.deposit(2000)            # Deposit Rs.2000
acc1.withdraw(5000)           # Withdraw Rs.5000
acc1.calculate_interest()     # Apply interest again
