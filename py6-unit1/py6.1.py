#Sort list items in ascending order.



def sort_list_manual(values):
    """
    Sort list items in ascending order manually (Bubble Sort).
    """
    if not values:
        raise ValueError("The list is empty. Cannot sort.")

    n = len(values)
    for i in range(n):  
        for j in range(0, n-i-1):
            if values[j] > values[j+1]:
                # swap
                values[j], values[j+1] = values[j+1], values[j]
    return values


numbers = [10, 25, 7, 99, 42]
print(sort_list_manual(numbers))   # Output: [7, 10, 25, 42, 99]
 