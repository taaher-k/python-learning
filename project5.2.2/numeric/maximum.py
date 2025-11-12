def find_maximum(values):
    """
    Calculate the maximum from n values.
    :param values: A list of numbers
    :return: The maximum number in the list
    """
    if not values:
        raise ValueError("The list is empty. Cannot find maximum.")
    return max(values)



def maxcal(x):
    if not x:
            raise ValueError("The list is empty. Cannot find maximum.")
    else:
        maxval = 0
        for i in x: 
            if i > maxval:
               maxval = i

    return maxval       


def maxca(x):
    if not x:  # check if list is empty
        raise ValueError("The list is empty. Cannot find maximum.")

    maxval = x[0]  # start with the first element
    for i in x[1:]:  # loop through the rest
        if i > maxval:
            maxval = i
    return maxval
