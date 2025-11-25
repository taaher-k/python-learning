#1.Create 2 threads, one to display multiplication table of given number. Another

#thread is to display all divisors of given number.

 

import threading

# Function to display multiplication table
def multiplication_table(num):
    print(f"\nMultiplication Table of {num}:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

# Function to display divisors
def divisors(num):
    print(f"\nDivisors of {num}:")
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=" ")
    print()  # newline


# --- Main Program ---
try:
    number = int(input("Enter a number: "))

    # Create threads
    t1 = threading.Thread(target=multiplication_table, args=(number,))
    t2 = threading.Thread(target=divisors, args=(number,))

    # Start threads
    t1.start()
    t2.start()

    # Wait for both threads to finish
    t1.join()
    t2.join()

    print("\nBoth threads finished execution.")

except ValueError:
    print("Error: Please enter a valid integer.")




