# 1. Create a module as numbers.py. Define
# a. function to read list of numbers and return even numbers.
# b. Function to read list of numbers and return prime numbers
# Create a main program and call functions from module.
"""
import numbers

list =[x for x in range(1,100)]

print(list)

even_numbers = numbers.even(list)
prime_numbers = numbers.prime(list)

"""
# main.py

import numbers

# Read list of numbers from user
user_input = input("Enter numbers separated by spaces: ")
#num_list = [int(x) for x in user_input.split()]
num_list = list(map(int, user_input.split()))

# Get even and prime numbers
even_list = numbers.even(num_list)
prime_list = numbers.prime(num_list)

# Display results
print("Even numbers:", even_list)
print("Prime numbers:", prime_list)
