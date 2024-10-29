"""
Rabbit is very particular about his belongings and wants to own an even number of each thing he owns. Write a function can_pair() that accepts a list of integers item_quantities. Return True if each number in item_quantities is even. Return False otherwise.
"""


def can_pair(item_quantities):
    """
    P: Check if all quantities in item_quanties are even

    [1,2,3] -> False
    [2,4] -> True
    [1] -> False
    [] -> False

    S: 1. Loop through the list
    2. Return False if any element is not even
    3. Return True otherwise
    """
    if len(item_quantities) == 0:
        return False

    for quantity in item_quantities:
        if quantity % 2 != 0:
            return False

    return True


if __name__ == "__main__":
    print(can_pair([2, 4, 6, 8]))
    print(can_pair([]))
    print(can_pair([1, 2, 3, 4]))
