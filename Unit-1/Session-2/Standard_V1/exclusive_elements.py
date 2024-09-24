def exclusive_elements(lst1, lst2):
    """
    P: Return distinct values between two lists

    [1,2,3], [1,3,5] -> [2,5]

    Q. What if there are duplicates in either lists?

    S: 1. Convert list 2 to set
    2. Create result list
    2. Loop through list 1
    4. Check if element is in set, add to result list if it is
    5. Repeat 1, 3, 4 for list 2
    6. Return result list
    """
    set_1 = set(lst1)
    set_2 = set(lst2)
    result_list = []

    for element in lst1:
        if element not in set_2:
            result_list.append(element)

    for element in lst2:
        if element not in set_1:
            result_list.append(element)

    return result_list


if __name__ == "__main__":
    print(exclusive_elements(["pooh", "roo", "piglet"], ["piglet", "eeyore", "owl"]))
    print(exclusive_elements(["pooh", "roo"], ["piglet", "eeyore", "owl", "kanga"]))
    print(exclusive_elements(["pooh", "roo", "piglet"], ["pooh", "roo", "piglet"]))
