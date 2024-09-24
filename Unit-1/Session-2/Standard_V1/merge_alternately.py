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

    result = ""

    while p1 < len(word1) and p2 < len(word2):
        result += word1[p1]
        result += word2[p2]
        p1 += 1
        p2 += 1

    if p1 < len(word1):
        result += word1[p1:]

    if p2 < len(word2):
        result += word2[p2:]

    return result


if __name__ == "__main__":
    print(merged_alternatively("war", "maysa"))
    print(merged_alternatively("wol", "oze"))
