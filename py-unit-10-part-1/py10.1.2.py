#1
#Read a value and display how many times it is available in a Tuple.


def main():
    # Example tuple
    my_tuple = (10, 20, 30, 20, 40, 20, 50, 10)

    print("Tuple:", my_tuple)

    # Read value from user
    value = input("Enter a value to search: ")

    try:
        # Convert input to integer (since tuple has numbers)
        value = int(value)
    except ValueError:
        print("Error: Please enter a valid number.")
        return

    # Count occurrences
    count = my_tuple.count(value)

    # Display result
    print(f"Value {value} occurs {count} time(s) in the tuple.")

if __name__ == "__main__":
    main()
