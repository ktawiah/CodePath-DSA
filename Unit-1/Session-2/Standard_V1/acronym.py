def is_acronym(words, s):
    """
    P: Determine if first characters in words list form the string, s

    ["can", "ate", "tard"], 'cat' -> True
    ["meat", "reave"], 'me' -> false

    S: 1. Create placeholder for concatenated string
    2. Loop through list
    3. add first character of each element to list
    4. Compare result list to s

    """
    acronym = ""

    for word in words:
        acronym += word[0]

    return acronym == s


if __name__ == "__main__":
    print(is_acronym(["christopher", "robin", "milne"], "crm"))
    print(is_acronym(["can", "ate", "tard"], "cat"))
    print(is_acronym(["meat", "reave"], "me"))
