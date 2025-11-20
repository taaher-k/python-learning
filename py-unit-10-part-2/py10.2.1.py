#1


#1. Store 5 account number and customer name in a dictionary and get account
#number from user and delete the specific account .


# Step 1: Create dictionary with 5 accounts
accounts = {
    "1001": "Alice",
    "1002": "Bob",
    "1003": "Charlie",
    "1004": "David",
    "1005": "Eva"
}

# Step 2: Get account number from user
acc_no = input("Enter account number to delete: ")

# Step 3: Delete if exists
if acc_no in accounts:
    del accounts[acc_no]
    print(f"Account {acc_no} deleted successfully.")
else:
    print("Account number not found.")

# Step 4: Display updated dictionary
print("Updated Accounts:", accounts)



 