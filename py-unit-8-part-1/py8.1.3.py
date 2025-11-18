## Program to read content from a file and count spaces, words, and sentences




def analyze_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()

            # Count spaces
            spaces = content.count(" ")

            # Count words (split by whitespace)
            words = len(content.split())

            # Count sentences (basic: split by '.', '!', '?')
            sentences = 0
            for end in [".", "!", "?"]:
                sentences += content.count(end)

            print(f"File: {filename}")
            print(f"Number of spaces: {spaces}")
            print(f"Number of words: {words}")
            print(f"Number of sentences: {sentences}")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
analyze_file("sample.txt")
