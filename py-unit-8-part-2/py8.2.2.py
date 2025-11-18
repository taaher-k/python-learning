#Write program to open userinfo.csv in read mode. Display all content in output.


#1


# Program to open userinfo.csv in read mode and display all content

import csv

def display_user_info():
    filename = "userinfo.csv"
    try:
        # Step 1: Open CSV file in read mode
        with open(filename, 'r') as file:
            reader = csv.reader(file)

            # Step 2: Display all rows
            print("Contents of userinfo.csv:\n")
            for row in reader:
                print(row)

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.") 
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
display_user_info()

