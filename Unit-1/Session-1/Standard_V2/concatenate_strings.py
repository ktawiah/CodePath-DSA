"""
Write a function concatenate() that takes in a list of strings words and returns a string concatenated that concatenates all elements in words.
"""


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
