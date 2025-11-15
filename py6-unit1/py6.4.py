#Read a string and reverse every word.



def reverse_a_string(x):
    
  name = x[::-1]
  print(name)
  


x = input("enter your name")

reverse_a_string(x)





#2

def reverse_words(text):
    if not text:
        raise ValueError("Empty string. Please enter some text.")

    words = text.split()              # split into words
    reversed_words = [w[::-1] for w in words]  # reverse each word
    return " ".join(reversed_words)   # join back into a string


# Example
s = "Hello Python World"
print(reverse_words(s))   # Output: "olleH nohtyP dlroW"



  


#3

a = input("hello")
print(a[::-1])   # "dlroW nohtyP olleH"
