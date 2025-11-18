#Open a file, read content and append it with another file content.



#5

#1

# Program to read content from one file and append it to another file

def append_file_content(source_file, target_file):
    try:
        # Step 1: Read content from source file
        with open(source_file, 'r') as src:
            content = src.read()

        # Step 2: Append content to target file
        with open(target_file, 'a') as tgt:
            tgt.write("\n")  # optional: add newline before appending
            tgt.write(content)

        print(f"Content from '{source_file}' appended successfully to '{target_file}'")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
append_file_content("sample.txt", "output.txt")
