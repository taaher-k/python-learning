#Read user name, emailed, mobile number, dob from user and store it in a
#CSV file. Create CSV file as userinfo.csv


#1

# Program to read user details and store them in a CSV file

import csv

def store_user_info():
    # Step 1: Collect user details
    username = input("Enter your name: ")
    email = input("Enter your email: ")
    mobile = input("Enter your mobile number: ")
    dob = input("Enter your date of birth (DD-MM-YYYY): ")

    # Step 2: Define the filename
    filename = "userinfo.csv"

    try:
        # Step 3: Open CSV file in append mode
        with open(filename, 'a', newline='') as file:
            writer = csv.writer(file)

            # Step 4: Write user details as a row
            writer.writerow([username, email, mobile, dob])

        print(f"Details saved successfully in '{filename}'")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
store_user_info()

