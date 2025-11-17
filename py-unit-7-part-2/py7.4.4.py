#4. Pattern to display letter of the word.

# 1


word = "Python"

for i in range(1, len(word)+1):       # Outer loop → controls rows
    for j in range(i):                 # Inner loop → controls letters
        print(word[j], end=" ")        # Print letters up to index j
    print()                            # Move to next line



