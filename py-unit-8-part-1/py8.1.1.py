# Program to read content from file and count number of characters

def count_chars(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            char_count = len(content)
            print(f"Total number of characters in '{filename}': {char_count}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
 
# Example usage
count_chars("sample.txt")
