#Read a string and count number of vowels.

#1




def check_vowels(number):

  vowels =  ["a","e","i","o","u"]


  result = [x for x in name.lower() if x in vowels]

  print(f"the number of vowels in the string are : {len(result)} {result} " )


name = input("enter your name ")
check_vowels(name)



#2


def count_vowels(text):
    if not text:
        raise ValueError("Empty string. Please enter some text.")

    vowels = "aeiouAEIOU"   # include uppercase too
    count = 0

    for ch in text:
        if ch in vowels:
            count += 1

    return count


# Example
s = "Hello Python World"
print(count_vowels(s))   # Output: 4
