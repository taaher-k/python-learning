#2. Find maximum and second maximum number from a list.

 
#1 with bug in sec_max function secm = [x for x in list if lis != list ]


def maxnum(list):

    return max(list)


def sec_maxnum(list):

    lis = maxnum(list)
    
    secm = [x for x in list if lis != list ]

    secondmax = max(secm)

    return secondmax



numbers = [101,10, 25, 7, 99, 42]
print(maxnum(numbers))  
print(sec_maxnum(numbers))
 

#2 with bug in sec_max function secm = [x for x in list if lis != list ] bug fixed secm = [x for x in list if  x != lis ]


def maxnum(lst):
    return max(lst)

def sec_maxnum(lst):
    lis = maxnum(lst)
    secm = [x for x in lst if x != lis]   # exclude the max itself
    if not secm:
        raise ValueError("No second maximum found (all elements equal).")
    return max(secm)

numbers = [101, 10, 25, 7, 99, 42]
print(maxnum(numbers))      # 101
print(sec_maxnum(numbers))  # 99




#3 this is with out using pre defined max() function



def find_max_and_second(values):
    if not values or len(values) < 2:
        raise ValueError("Need at least two numbers.")

    max1 = max2 = float('-inf')  # start with very small values

    for num in values:
        if num > max1:
            max2 = max1   # old max becomes second max
            max1 = num
        elif num > max2 and num != max1:
            max2 = num

    return max1, max2


number = [101, 10, 25, 7, 99, 42]
print(find_max_and_second(number))  # Output: (101, 99)



