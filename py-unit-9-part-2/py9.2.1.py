#1

#Write a program that presents a menu with numbered options. The user can choose an
#operation to perform, such as creating a directory, renaming a file, copying a file, etc.
#● Create Directory:
#● List Directory Contents
#● Rename File
#● Delete File:
#● Delete Directory
#● Copy File
#● Move File


import os
import shutil

def create_directory():
    dirname = input("Enter directory name: ")
    try:
        os.mkdir(dirname)
        print(f"Directory '{dirname}' created successfully.")
    except FileExistsError:
        print("Error: Directory already exists.")
    except Exception as e:
        print(f"Error: {e}")



def list_directory_contents():
    path = input("Enter directory path (leave blank for current): ")
    if not path:
        path = "."
    try:
        contents = os.listdir(path)
        print("Contents of directory:", contents)
    except Exception as e:
        print(f"Error: {e}")

def rename_file():
    old_name = input("Enter current file name: ")
    new_name = input("Enter new file name: ")
    try:
        os.rename(old_name, new_name)
        print(f"File renamed from '{old_name}' to '{new_name}'.")
    except Exception as e:
        print(f"Error: {e}")

def delete_file():
    filename = input("Enter file name to delete: ")
    try:
        os.remove(filename)
        print(f"File '{filename}' deleted successfully.")
    except Exception as e:
        print(f"Error: {e}")

def delete_directory():
    dirname = input("Enter directory name to delete: ")
    try:
        os.rmdir(dirname)
        print(f"Directory '{dirname}' deleted successfully.")
    except Exception as e:
        print(f"Error: {e}")

def copy_file():
    src = input("Enter source file: ")
    dest = input("Enter destination file: ")
    try:
        shutil.copy(src, dest)
        print(f"File copied from '{src}' to '{dest}'.")
    except Exception as e:
        print(f"Error: {e}")

def move_file():
    src = input("Enter source file: ")
    dest = input("Enter destination file: ")
    try:
        shutil.move(src, dest)
        print(f"File moved from '{src}' to '{dest}'.")
    except Exception as e:
        print(f"Error: {e}")

def menu():
    while True:
        print("\n--- File Operations Menu ---")
        print("1. Create Directory")
        print("2. List Directory Contents")
        print("3. Rename File")
        print("4. Delete File")
        print("5. Delete Directory")
        print("6. Copy File")
        print("7. Move File")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            create_directory()
        elif choice == "2":
            list_directory_contents()
        elif choice == "3":
            rename_file()
        elif choice == "4":
            delete_file()
        elif choice == "5":
            delete_directory()
        elif choice == "6":
            copy_file()
        elif choice == "7":
            move_file()
        elif choice == "8":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
