#6. Print all the non – repeated data from the given list


#1


def non_repeated(lst):
    if not lst:
        raise ValueError("Empty list. Please provide data.")

    result = [x for x in lst if lst.count(x) == 1]
    return result


numbers = [10, 25, 7, 25, 42, 10, 99]
print(non_repeated(numbers))   # Output: [7, 42, 99]



#2
#from collections import Counter

from collections import Counter  

def non_repeate(lst):
    counts = Counter(lst)
    return [x for x in lst if counts[x] == 1]

numbers = [10, 25, 7, 25, 42, 10, 99]
print(non_repeate(numbers))   # Output: [7, 42, 99]


#3

number = [10, 25, 7, 25, 42, 10, 99]

non_repeated = [x for x in set(number) if number.count(x) == 1]
print(non_repeated)   # [42, 99, 7]



