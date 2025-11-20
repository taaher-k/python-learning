#1


#4. How to count a number of consonants in a given String?



# Program to count consonants in a string

s = input("Enter a string: ")

# Step 1: Define vowels
vowels = "aeiouAEIOU"

# Step 2: Initialize counter
count = 0

# Step 3: Loop through characters
for ch in s:
    if ch.isalpha() and ch not in vowels:   # check consonant
        count += 1

# Step 4: Display result
print("Number of consonants:", count)



#2
# 
s = input("Enter a string: ")
vowels = "aeiouAEIOU"
consonants = [ch for ch in s if ch.isalpha() and ch not in vowels]
print("Number of consonants:", len(consonants))
print("Consonants are:", consonants)
    