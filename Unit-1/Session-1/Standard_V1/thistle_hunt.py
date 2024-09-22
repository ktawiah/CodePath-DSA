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
