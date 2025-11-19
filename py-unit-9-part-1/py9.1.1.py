#1
import sys

def main():
    # Check if filename argument is provided
    if len(sys.argv) < 2:
        print("Usage: python script.py <filename>")
        return
    
    filename = sys.argv[1]
    
    try:
        # Open and read the file
        with open(filename, 'r') as file:
            content = file.read()
        
        # Display content in reverse order
        print(content[::-1])
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    
    main()
    # file: example.py
print(__name__)



def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__": #if you import this file  below code will not work because of the if name main condition
    # This runs only if you execute the file directly
    print(greet("Taaher"))
