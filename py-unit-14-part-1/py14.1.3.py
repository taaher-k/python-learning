#Get two integers from the user and convert it into integer and perform
#division operation. Handle necessary Exceptions.


try:
    # Step 1: Get two integers from the user
    num1 = int(input("Enter first integer: "))
    num2 = int(input("Enter second integer: "))

    # Step 2: Perform division
    result = num1 / num2

    print(f"Result of {num1} / {num2} = {result}")

# Handle invalid input (non-integer values)
except :
    print("Error: Please enter valid integers only.")

# Handle division by zero
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# Handle any other unexpected errors
except Exception as e:
    print("Unexpected error:", e)

finally:
    print("Program execution completed.")
