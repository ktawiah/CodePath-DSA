def concatenate(strings):
    """
    P: Return concatenated strings in list

    ["a", "ba"] -> "aba"
    [] -> ""

    S: Use .join() to concatenate string
    """
    return "".join(strings)


if __name__ == "__main__":
    print(concatenate(["vengeance", "darkness", "batman"]))
    print(concatenate([]))
