def merged_alternatively(word1, word2):
    """
    P: Return a merges string with alternate characters of two word inputs

    "war", "maysa" -> "wmaarysa"
    "wol", "oze" -> "woozle"

    S: 1. Create two pointers and initialize both to zero
    2. Create result string
    3. Add character at first word to result string
    4. Add character at second word to result string
    5. Increment pointers
    6. Break when either pointers exceed the length of either words
    7. Add words after pointer to the result string

    """
    p1, p2 = 0, 0
    word_list = []

    while p1 < len(word1) and p2 < len(word2):
        word_list.append(word1[p1])
        word_list.append(word2[p2])

        p1 += 1
        p2 += 1

    while p1 < len(word1):
        word_list.append(word1[p1])
        p1 += 1

    while p2 < len(word2):
        word_list.append(word2[p2])
        p2 += 1

    return "".join(word_list)


if __name__ == "__main__":
    print(merged_alternatively("war", "maysa"))
    print(merged_alternatively("wol", "oze"))
