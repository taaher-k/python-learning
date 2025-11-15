
#5. Find all pair of number whose sum is equal to a number from the list.



def find_pairs(lst):
    if not lst or len(lst) < 2:
        raise ValueError("Need at least two numbers.")

    pairs = []
    for i in range(len(lst)):  #0 to length is 7 but loop will not excute the last num so its 0 to 6  
        for j in range(i+1, len(lst)): # i=0+-1 to length is 7 but loop will not excute the last num so its 1 to 6    # avoid duplicate pairs
          #  first loop after running one time the second loop run 1 to 6 
               
            s = lst[i] + lst[j]
            if s in lst:
                pairs.append((lst[i], lst[j], s))
    return pairs


numbers = [101, 10, 25, 7, 99, 42,3]
print(find_pairs(numbers))



