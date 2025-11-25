#Create a program to read transaction type and amount as input. Initialize

#account balance as 50000. Transaction type can be withdraw or deposit.

#Withdraw amount should be in hundreds only. Withdraw amount should

#not exceed 25000. Create and raise custom exceptions.



# Step 1: Define custom exceptions
class InvalidTransactionType(Exception):
    """Raised when transaction type is not withdraw or deposit"""
    pass

class InvalidWithdrawAmount(Exception):
    """Raised when withdraw amount is not in hundreds or exceeds limit"""
    pass


try:
    # Step 2: Initialize balance
    balance = 50000

    # Step 3: Read transaction type and amount
    transaction_type = input("Enter transaction type (withdraw/deposit): ").lower()
    amount = int(input("Enter amount: "))

    # Step 4: Validate transaction type
    if transaction_type not in ["withdraw", "deposit"]:
        raise InvalidTransactionType("Transaction type must be 'withdraw' or 'deposit'.")

    # Step 5: Handle withdraw
    if transaction_type == "withdraw":
        if amount % 100 != 0:
            raise InvalidWithdrawAmount("Withdraw amount must be in multiples of 100.")
        if amount > 25000:
            raise InvalidWithdrawAmount("Withdraw amount must not exceed 25000.")
        if amount > balance:
            raise InvalidWithdrawAmount("Insufficient balance.")
        balance -= amount
        print(f"Withdraw successful! New balance: Rs.{balance}")

    # Step 6: Handle deposit
    elif transaction_type == "deposit":
        balance += amount
        print(f"Deposit successful! New balance: Rs.{balance}")

# Step 7: Handle exceptions
except InvalidTransactionType as e:
    print("Error:", e)

except InvalidWithdrawAmount as e:
    print("Error:", e)

except ValueError:
    print("Error: Please enter a valid integer amount.")

finally:
    print("Transaction process completed.")


