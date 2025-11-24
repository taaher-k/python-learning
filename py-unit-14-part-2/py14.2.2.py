#Read a number and display its cube. If input is not a number, raise an
#exception. If no exception has occurred, then display result using else
#block.


try:
    # Step 1: Read input from user
    num = int(input("Enter a number: "))

    # Step 2: Calculate cube
    cube = num ** 3

# Step 3: Handle invalid input (non-integer)
except ValueError:
    print("Error: Please enter a valid integer.")

# Step 4: If no exception occurs, run else block
else:
    print(f"The cube of {num} is {cube}")

finally:
    print("Program execution completed.")
