# Program to read content from a file, reverse it, and display the output

def reverse_file_content(filename):
    try:
        # Step 1: Read content from file
        with open(filename, 'r') as file:
            content = file.read()

        # Step 2: Reverse the content
        reversed_content = content[::-1]

        # Step 3: Display the reversed content
        print("Reversed Content:\n")
        print(reversed_content)

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
reverse_file_content("sample.txt")


