def are_equivalent(word1, word2):
    """
    P: Determine all concatenated string elements in both lists are equal

    ["k", "el", "vin"], ["kel", "v", "in"] -> "kelvin"

    S: 1. Create placeholder for string of word1
    2. Create placeholder for string of word2
    3. Use .join() method to create concatenated strings for both words
    4. Compare strings
    """
    str_1 = "".join(word1)
    str_2 = "".join(word2)

    return str_1 == str_2


if __name__ == "__main__":
    print(are_equivalent(["bat", "man"], ["b", "atman"]))
    print(are_equivalent(["alfred", "pennyworth"], ["alfredpenny", "word"]))
    print(are_equivalent(["cat", "wom", "an"], ["catwoman"]))
