def tiggerfy(words):
    """
    P: Return the word after strings "er", t, i, gg have been removed

    eggplant -> eplan
    trigger -> r

    1. Create placeholder to store conditional strings
    2. Convert word to list of characters
    2. Loop through the word, keeping track of the index
    3. If the char is e, check if next char is g -> Do same for gg
    4. Else if char in set of strs, pop out char or pop out next two if gg or er
    5. Return result
    """
    cond_strings = {"T", "i", "r", "t"}

    word_list = list(words)

    new_list = []

    index = 0

    while index < len(words) - 1:
        if (word_list[index] == "e" and word_list[index + 1] == "r") or (
            word_list[index + 1] == "g" and word_list[index] == "g"
        ):
            index += 1
        elif word_list[index] not in cond_strings:
            # word_list.pop(index)
            new_list.append(word_list[index])

        index += 1

    if word_list[-1] not in cond_strings:
        # word_list.pop(index)
        new_list.append(word_list[-1])

    return "".join(new_list)


word = "Trigger"
print(tiggerfy(word))

word = "eggplant"
print(tiggerfy(word))

word = "Choir"
print(tiggerfy(word))
