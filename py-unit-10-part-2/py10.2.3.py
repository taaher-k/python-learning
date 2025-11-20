#3. Convert the key-value pairs of the dictionary, as tuples in a list.




# Step 1: Create a dictionary
accounts = {
    "1001": "Alice",
    "1002": "Bob",
    "1003": "Charlie",
    "1004": "David",
    "1005": "Eva"
}

# Step 2: Convert key-value pairs into list of tuples
tuple_list = list(accounts.items())

# Step 3: Display result
print("Dictionary:", accounts)
print("List of Tuples:", tuple_list)



#2


tuple_list = [(k, v) for k, v in accounts.items()]
print(tuple_list)

