#Write program to read user name, qualification, year of passed out and
#store in a text file. Text file should be created as username.txt


# Program to read user details and store in a text file


def store_user_details():
    # Step 1: Take inputs
    username = input("Enter your name: ")
    qualification = input("Enter your qualification: ")
    year = input("Enter your year of passed out: ")

    # Step 2: Create filename as username.txt
    filename = f"{username}.txt"

    try:
        # Step 3: Open file in write mode and store details
        with open(filename, 'w') as file:
            file.write(f"Name: {username}\n")
            file.write(f"Qualification: {qualification}\n")
            file.write(f"Year of Passed Out: {year}\n")

        print(f"Details saved successfully in '{filename}'")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
store_user_details()
