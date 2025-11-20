#1


#5. How to print the first non repeated character from String?



from collections import Counter

# Step 1: Get input
s = input("Enter a string: ")

# Step 2: Count frequency of each character
freq = Counter(s)

# Step 3: Find first non-repeated character
for ch in s:
    if freq[ch] == 1:
        print("First non-repeated character:", ch)
        break
else:
    print("No non-repeated character found")



#2


s = input("Enter a string: ")

for ch in s:
    if s.count(ch) == 1:   # check frequency directly
        print("First non-repeated character:", ch)
        break
else:
    print("No non-repeated character found")









#🔍 Explanation
#Counter(s) and s.count() → counts each character: { 'p':1, 'r':2, 'o':1, 'g':2, 'a':1, 'm':2, 'i':1, 'n':1 }

#Traverse "programming" left to right:

#'p' → count = 1 → ✅ first non-repeated.