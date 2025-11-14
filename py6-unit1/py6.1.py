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


numbers = [101,10, 25, 7, 99, 42]
print(sort_list_manual(numbers))   # Output: [7, 10, 25, 42, 99]
 





def sort_list_manual(values):
    if not values:
        raise ValueError("The list is empty. Cannot sort.")

    n = len(values)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if values[j] > values[j+1]:
                values[j], values[j+1] = values[j+1], values[j]
                swapped = True
        if not swapped:  # No swaps → already sorted
            break
    return values


print(sort_list_manual([5]))          # Single element → [5]
print(sort_list_manual([3, 3, 3]))    # Duplicates → [3, 3, 3]
print(sort_list_manual([-1, 0, 2]))   # Negative numbers → [-1, 0, 2]


