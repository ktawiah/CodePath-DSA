def reverse_vowel(s):
    """
    P: Reverse all the vowel characters in string, s

    "Kelvin" -> Kilven

    S: 1. Create start and end pointer
    2. Create placeholder for all vowel characters
    3. While start < end
        - if both start and end values are vowels, swap, move both
        - if either values is vowel, move other pointer
        - if both are constants, move both

    """

    vowels = {"a", "e", "i", "o", "u"}

    s_list = list(s)

    start, end = 0, len(s) - 1

    while start < end:
        if s_list[start].lower() in vowels and s_list[end].lower() in vowels:
            s_list[start], s_list[end] = s_list[end], s_list[start]
            start += 1
            end -= 1
        elif s_list[start].lower() not in vowels and s_list[end].lower() not in vowels:
            start += 1
            end -= 1
        elif s_list[start].lower() in vowels and s_list[end].lower() not in vowels:
            end -= 1
        else:
            start += 1

    return "".join(s_list)


if __name__ == "__main__":
    print(reverse_vowel("robin"))
    print(reverse_vowel("BATgirl"))
    print(reverse_vowel("batman"))
