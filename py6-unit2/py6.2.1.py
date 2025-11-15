#1. Read 2 strings and check if anagram or not.



def is_anagram(str1, str2):
    # Normalize: remove spaces and lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Compare sorted characters
    return sorted(str1) == sorted(str2)


# Example
s1 = "listen"
s2 = "silent"
print(is_anagram(s1, s2))   # Output: True
