def common_elements(lst1, lst2):
    """
    P: Return a list of all common elements between both lists

    [1,2,3], [1,3,5] -> [1,3]

    S: 1. Create a placeholder to store the common values
    2. Convert one list to a set
    3. Loop through first list
    4. Look up value in set
    5. Add to common values list if found else do nothing
    6. Return new list
    """
    common_values = []

    set_2 = set(lst2)

    for val in lst1:
        if val in set_2:
            common_values.append(val)

    return common_values


lst1 = ["super strength", "super speed", "x-ray vision"]
lst2 = ["super speed", "time travel", "dimensional travel"]
print(common_elements(lst1, lst2))

lst1 = ["super strength", "super speed", "x-ray vision"]
lst2 = ["martial arts", "stealth", "master detective"]
print(common_elements(lst1, lst2))
print(common_elements([1, 2, 3], [1, 3, 5]))
