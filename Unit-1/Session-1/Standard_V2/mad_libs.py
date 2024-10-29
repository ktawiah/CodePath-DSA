"""
Write a function madlib() that accepts one parameter, a string verb. The function should print the sentence: "I have one power. I never <verb>. - Batman".
"""


def mad_libs(verb):
    """
    P: Output a dynamic string with verb input inside
    """
    print(f"I have one power. I never {verb}. - Batman")


if __name__ == "__main__":
    mad_libs("give up")
    mad_libs("nap")
