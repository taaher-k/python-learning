#Read 5 integers and store in a list. Read 2 positions between 0 and 4 and

#fetch those numbers in those positions. Find product of those 2 numbers.

#Raise necessary exceptions.





try:
    # Step 1: Read 5 integers and store in a list
    numbers = []
    print("Enter 5 integers:")
    for i in range(5):
        num = int(input(f"Enter integer {i+1}: "))
        numbers.append(num)

    # Step 2: Read 2 positions between 0 and 4
    pos1 = int(input("Enter first position (0-4): "))
    pos2 = int(input("Enter second position (0-4): "))

    # Step 3: Raise exceptions for invalid positions
    if pos1 < 0 or pos1 > 4 or pos2 < 0 or pos2 > 4:    
        raise IndexError("Position must be between 0 and 4")

    # Step 4: Fetch numbers and calculate product
    num1 = numbers[pos1]
    num2 = numbers[pos2]
    product = num1 * num2

    print(f"Number at position {pos1}: {num1}")
    print(f"Number at position {pos2}: {num2}")
    print(f"Product: {product}")

except ValueError:
    print("Error: Please enter only integers.")

except IndexError as e:
    print("Error:", e)

finally:
    print("Program execution completed.")
