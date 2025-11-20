#1

#1. Write a menu driven program to add, remove, search values from a list.



def menu():
    my_list = []  # start with an empty list
    
    while True:
        print("\n--- List Operations Menu ---")
        print("1. Add Value")
        print("2. Remove Value")
        print("3. Search Value")
        print("4. Display List")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            value = input("Enter value to add: ")
            my_list.append(value)
            print(f"'{value}' added to the list.")
        
        elif choice == "2":
            value = input("Enter value to remove: ")
            if value in my_list:
                my_list.remove(value)
                print(f"'{value}' removed from the list.")
            else:
                print(f"'{value}' not found in the list.")
        
        elif choice == "3":
            value = input("Enter value to search: ")
            if value in my_list:
                print(f"'{value}' found at position {my_list.index(value)}.")
            else:
                print(f"'{value}' not found in the list.")
        
        elif choice == "4":
            print("Current List:", my_list)
        
        elif choice == "5":
            print("Exiting program...")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
