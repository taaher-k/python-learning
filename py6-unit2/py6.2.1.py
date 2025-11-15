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



#2

from collections import Counter

def is_anagrame(str1, str2):
    return Counter(str1.replace(" ", "").lower()) == Counter(str2.replace(" ", "").lower())

# Example
s1 = "listen"
s2 = "silent"
print(is_anagrame(s1, s2))   # Output: True



#3


a =input(str("enter the first word to check an anagram "))
b =input(str("enter the second word to check an anagram "))

if len(a) == len(b):
    count = 0
    for i in a :
        if i in b:
            print("Anagram")
        else:
             print("Not a Anagram") 
else:
      print("Not a Anagram")             

      
      

 #4  



def annanas(srr1, srr2):
    # Normalize: remove spaces and lowercase
    srr1 = srr1.replace(" ", "").lower()
    srr2 = srr2.replace(" ", "").lower()

    # If lengths differ, cannot be an anagram
    if len(srr1) != len(srr2):
        return "Not an Anagram"

    # Build frequency dictionary for srr1
    freq1 = {}
    for ch in srr1:
        freq1[ch] = freq1.get(ch, 0) + 1

    # Build frequency dictionary for srr2
    freq2 = {}
    for ch in srr2:
        freq2[ch] = freq2.get(ch, 0) + 1

    # Compare dictionaries
    if freq1 == freq2:
        return "Anagram"
    else:
        return "Not an Anagram"


# Example
x = input("Enter first string: ")
y = input("Enter second string: ")


print(annanas(x, y))
     


