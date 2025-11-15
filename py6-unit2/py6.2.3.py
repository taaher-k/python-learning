#1

# Check if given string is palindrome.



def is_palindrome(s):
    # Normalize: remove spaces and lowercase
    s = s.replace(" ", "").lower()

    # Compare string with its reverse
    if s == s[::-1]:
        return "Palindrome"
    else:
        return "Not a Palindrome"


# Example
x = input("Enter a string: ")
print(is_palindrome(x))


