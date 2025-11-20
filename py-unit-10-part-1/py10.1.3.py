#1
"""


# 3. Get input from user and reverse the list

# Program to get input from user and reverse the list

# Step 1: Ask the user for input (comma-separated values)
user_input = input("Enter elements separated by commas: ")

# Step 2: Convert the string into a list
my_list = user_input.split(",")

# Step 3: Reverse the list
reversed_list = my_list[::-1]   # slicing method

# Step 4: Display the reversed list
print("Original List:", my_list)
print("Reversed List:", reversed_list)


# Program to get input from user and reverse the list using predefined function

# Step 1: Get input from user
user_input = input("Enter elements separated by commas: ")

# Step 2: Convert to list
my_list = user_input.split(",")

# Step 3: Reverse the list using predefined function
my_list.reverse()   # reverses in place

# Step 4: Display result
print("Reversed List:", my_list)








# Program to get input from user and reverse the list using predefined function

user_input = input("Enter elements separated by commas: ")
my_list = user_input.split(",")

# reversed() returns an iterator, so we convert it back to a list
reversed_list = list(reversed(my_list))

print("Reversed List:", reversed_list)




ind = input("enter the string")


b = reversed(ind)

print(b)

"""

inj= input("Enter the string: ")

c= list(reversed(inj))  # convert iterator to list

print(c)                  # prints ['o', 'l', 'l', 'e', 'h']





ind = input("Enter the string: ")          

b = "".join(reversed(ind))   # join characters into a string

print(b)                     # prints "olleh"








ind = input("Enter the string: ")          

b = "".join(ind[::-1])   # join characters into a string

print(b)                     # prints "olleh"








num = 256476
rev = 0

while num > 0:
    digit = num % 10          # get last digit
    rev = rev * 10 + digit    # build reversed number
    num = num // 10           # remove last digit

print(rev)   # Output: 674652




s = "hello"
rev_iter = reversed(s)        # gives an iterator
print(rev_iter)               # <reversed object at ...>

rev_list = list(rev_iter)     # convert to list
print(rev_list)               # ['o', 'l', 'l', 'e', 'h']

rev_str = "".join(reversed(s))  # join back into string
print(rev_str)                # "olleh"
