#Find and replace the specific value from the string without using pre-defined function


#1





def manual_replace(text, old, new):
    result = ""
    i = 0
    while i < len(text):
        # Check if substring starting at i matches 'old'

        if text[i:i+len(old)] == old:
            result += new        # add replacement
            i += len(old)        # skip over the old substring
        else:
            result += text[i]    # add current character
            i += 1
    return result


# Example
s = "I like Python. Python is powerful."
print(len(s))
print(manual_replace(s, "is", "Java"))





#2 


d = "python"
result = ""
for i in d:
    if i == "p":
        result += "c"
    else:
        result += i

print(result)


#3

e = "python"
for p in e:
    if(p=="p"):
        p = "c"
    print(p, end="")     

