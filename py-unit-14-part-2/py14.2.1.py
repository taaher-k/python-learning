
#Read age from user and check if eligible to vote or not. Create and raise

#custom exception, if age is given as negative.






# Step 1: Define a custom exception
class NegativeAgeError(Exception):
    """Raised when age entered is negative"""
    pass


try:
    # Step 2: Read age from user
    age = int(input("Enter your age: "))

    # Step 3: Raise custom exception if age is negative
    if age < 0:
        raise NegativeAgeError("Age cannot be negative!")

    # Step 4: Check voting eligibility
    if age >= 18:
        print("You are eligible to vote ✅")
    else:
        print("You are NOT eligible to vote ❌")

# Step 5: Handle custom exception
except NegativeAgeError as e:
    print("Error:", e)

# Handle invalid input (non-integer)
except ValueError:
    print("Error: Please enter a valid integer for age.")

finally:
    print("Program execution completed.")
