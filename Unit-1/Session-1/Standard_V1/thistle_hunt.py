"""
Pooh, Piglet, and Roo are looking for thistles to gift their friend Eeyore. Write a function locate_thistles() that takes in a list of strings items and returns a list of the indices of any elements with value "thistle". The indices in the resulting list should be ordered from least to greatest.
"""


def locate_thistle(items):
    """
    P: Return a list of indices of 'thistle' in items

    S: 1. Create list for result
    2. Loop through items
    3. if item is equal to 'thistle' add index to result_list,else do nothing
    4. Return result_list
    """
    result_list = []

    for index, item in enumerate(items):
        if item == "thistle":
            result_list.append(index)

    return result_list


if __name__ == "__main__":
    print(locate_thistle(["thistle", "stick", "carrot", "thistle", "eeyore's tail"]))
    print(locate_thistle(["book", "bouncy ball", "leaf", "red balloon"]))
