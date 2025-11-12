def find_maximum(values):
    """
    Calculate the maximum from n values.
    :param values: A list of numbers
    :return: The maximum number in the list
    """
    if not values:
        raise ValueError("The list is empty. Cannot find maximum.")
    return max(values)
