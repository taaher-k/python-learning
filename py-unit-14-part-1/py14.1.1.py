#Read name, gender and hobby from user. Create a file named userinfo.txt
#and store all input data in this file. Raise an exception if file already
#exists. Close the file using finally block.



import os

try:
    # Step 1: Check if file already exists
    if os.path.exists("userinfo.txt"):
        raise FileExistsError("File 'userinfo.txt' already exists!")

    # Step 2: Get user input
    name = input("Enter your name: ")
    gender = input("Enter your gender: ")
    hobby = input("Enter your hobby: ")

    # Step 3: Create and write to file
    f = open("userinfo.txt", "w")
    f.write(f"Name   : {name}\n")
    f.write(f"Gender : {gender}\n")
    f.write(f"Hobby  : {hobby}\n")

    print("Data successfully written to userinfo.txt")

except FileExistsError as e:
    print("Error:", e)

finally:
    # Step 4: Close file safely
    try:
        f.close()
        print("File closed successfully.")
    except NameError:
        # If file was never opened (due to exception), skip closing
        print("No file to close.")
