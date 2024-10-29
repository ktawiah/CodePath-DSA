"""
T-I-Double Guh-Er: That spells Tigger! Write a function tiggerfy() that accepts a string word and returns a new string that removes any substrings t, i, gg, and er from word. The function should be case insensitive.
"""


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

    # Create a set of conditional strings
    cond_set = {"t", "i", "gg", "er"}

    # Convert words into a list of chars
    word_list = list(words)

    # Iterate through word
    index = 0

    while index < len(word_list) - 1:
        # Pop out char(s) if in set
        if f"{word_list[index]}{word_list[index+1]}".lower() in cond_set:
            word_list.pop(index)
            word_list.pop(index)
        elif word_list[index].lower() in cond_set:
            word_list.pop(index)
        else:
            index += 1

    # Return string of chars
    return "".join(word_list)

    # cond_strings = {"t", "i", "gg", "er"}

    # word_list = list(words.lower())

    # new_list = []

    # index = 0

    # while index < len(words) - 1:
    #     if (word_list[index] == "e" and word_list[index + 1] == "r") or (
    #         word_list[index + 1] == "g" and word_list[index] == "g"
    #     ):
    #         index += 1
    #     elif word_list[index] not in cond_strings:
    #         # word_list.pop(index)
    #         new_list.append(word_list[index])

    #     index += 1

    # if word_list[-1] not in cond_strings:
    #     word_list.pop()
    #     new_list.append(word_list[-1])
    # return "".join(new_list)


word = "Trigger"
print(tiggerfy(word))

word = "eggplant"
print(tiggerfy(word))

word = "Choir"
print(tiggerfy(word))
