#5. Print all the odd index character from the given string.

#1

text = "python"

# Method 1: Using a loop
for i in range(len(text)):
    if i % 2 != 0:   # odd index
        print(text[i], end="")





#2
# Method 2: Using slicing
print(text[1::2])   # start at index 1, step by 2


#3

a= input(str("enter the string"))
for i in range(1,len(a),2):
    i = a[i]    
print(i, end=" ")    


