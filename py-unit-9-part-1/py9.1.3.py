#1


import sys

def main():
    # Check if numbers are provided
    if len(sys.argv) < 2:
        print("Usage: python multiply.py <num1> <num2> ... <numN>")
        return
    
    try:
        # Convert arguments (excluding script name) to floats
        numbers = [float(arg) for arg in sys.argv[1:]]
        
        # Multiply all numbers
        result = 1
        for num in numbers:
            result *= num
        
        print("Result:", result)
    
    except ValueError:
        print("Error: Please provide valid numbers.")

if __name__ == "__main__":
    main()
