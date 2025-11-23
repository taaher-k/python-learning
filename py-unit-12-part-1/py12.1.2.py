#A bank maintains two kinds of accounts – Savings account and Current account


#. The savings account provides simple interest, deposit and withdrawal facilities.


# The current account only provides deposit and withdrawal facilities.


# Using inheritance write program for the same.



class BankAccount:
    def __init__(self, balance=0):
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


# Child class: Savings Account
class SavingsAccount(BankAccount):
    def calculate_interest(self, rate, time):
        # Simple Interest = (P * R * T) / 100
        interest = (self.balance * rate * time) / 100
        self.balance += interest
        print(f"Interest of Rs.{interest:.2f} added. New Balance: Rs.{self.balance:.2f}")




# Child class: Current Account
class CurrentAccount(BankAccount):
    # Only deposit and withdraw (already inherited)
    pass





# --- Program Execution ---
print("=== Savings Account ===")
s1 = SavingsAccount(10000)
s1.deposit(2000)
s1.withdraw(3000)
s1.calculate_interest(rate=5, time=2)   # 5% for 2 years
s1.check_balance()

print("\n=== Current Account ===")
c1 = CurrentAccount(15000)
c1.deposit(5000)
c1.withdraw(7000)
c1.check_balance()
