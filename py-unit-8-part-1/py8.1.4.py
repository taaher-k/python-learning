#3


# Program to read content from a file, remove vowels, and write to another file

def remove_vowels(input_file, output_file):
    vowels = "aeiouAEIOU"
    try:
        # Step 1: Read content from input file
        with open(input_file, 'r') as file:
            content = file.read()

        # Step 2: Remove vowels
        result = ''.join([ch for ch in content if ch not in vowels])

        # Step 3: Write remaining content to output file
        with open(output_file, 'w') as file:
            file.write(result)

        print(f"Vowels removed successfully. Output saved in '{output_file}'")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
remove_vowels("sample.txt", "output.txt")
