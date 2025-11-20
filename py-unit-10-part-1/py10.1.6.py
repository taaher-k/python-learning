#1

# Program to reverse each word of a string


s = input("Enter a string: ")

# Split into words
words = s.split()

#demo
wd =words[::-1]

#Reverse each word
reversed_words = [word[::-1] for word in words]

# Join back into a string
result = " ".join(reversed_words)

print("Original String:", s)
print(wd) #demo
print(reversed_words)#demo
print("Reversed Words String:", result)

