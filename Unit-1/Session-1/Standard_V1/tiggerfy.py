def tiggerfy(s):
    """
    P: Return s excluding letters composing tiger

    'suspicious' -> suspcious
    'name' -> nm
    Q: What if characters repeat? Maintain or take out?

    S: 1. Create a list to store result -> Redundant
    2. Split s into a list
    3. Store tigger characters in set
    4. For each element in s_list, if character in tigger_set, remove from list, else do nothing
    5. Join chars in s_list
    6. Return new string.

    T.C: O(n)
    """
    s_list = s.split()
    t_set = set("tiger")

    for index, char in enumerate(s_list):
        if char in t_set:
            s_list.pop(index)

    return "".join(s_list)


if __name__ == "__main__":
    print(tiggerfy("suspcous"))
    print(tiggerfy(""))
    print(tiggerfy("Hunny"))
