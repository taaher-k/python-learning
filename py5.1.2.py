#Write a Python program using a generator function to reverse a string
#character by character.



#1



def rev(n):
    for i in  n [::-1]:
        yield i
n = input("enter the string")
r= rev(n)


print ("reversed string")

for i in r:
    print(i,end=" ")



# 2

def reverse_string_gen(s):
    for i in range(len(s) - 1, -1, -1):
        yield s[i]

# Example usage
text = "Taaher"
print(f"Reversed string of '{text}':")
for char in reverse_string_gen(text):
    print(char, end="")


#3

name = "aftab"
namerev = []

for x in range(len(name)-1,-1,-1):
    namerev.append(name[x])

print( "".join(namerev))    
