#!/usr/bin/python3
# Exersize sheet 1, exersize 1


def insertionsort(lst):
    """ Sort list using the Insertion Sort algorithm.

    >>> insertionsort([24, 6, 12, 32, 18])
    [6, 12, 18, 24, 32]

    >>> insertionsort([])
    []

    >>> insertionsort("hallo")
    Traceback (most recent call last):
        ...
    TypeError: lst must be a list

    """
    # Check given parameter data type.
    if not type(lst) == list:
        raise TypeError('lst must be a list')
    # Get length of the list.
    n = len(lst)
    # For each list element.
    for i in range(n):
        min_value = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > min_value:
            lst[j+1] = lst[j]
            j = j - 1
        lst[j+1] = min_value
    return lst

"""if __name__ == "__main__":
    # Create an unsorted list of integers.
    numbers = [10, 4, 1, 5, 2, 3, 11, 3, 9]
    # Sort the list.
    print(insertionsort(numbers))
    """
# Create an unsorted list of integers.
numbers = [10, 4, 1, 5, 2, 3, 11, 3, 9]
# Sort the list.
print(insertionsort(numbers))
# end
