
#2. Read list of strings and find the longest string.
#1


def longest_string(lst):
    if not lst:
        raise ValueError("Empty list. Please provide some strings.")

    longest = lst[0]   # assume first string is longest
    for s in lst:
        if len(s) > len(longest):
            longest = s
    return longest


# Example
strings = ["apple", "banana", "cherry", "watermelon", "kiwi"]
print("Longest string is:", longest_string(strings))


#2


strings = ["apple", "banana", "cherry", "watermelon", "kiwi"]
print("Longest string is:", max(strings, key=len))
