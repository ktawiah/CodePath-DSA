"""
Write a function greeting() that accepts a single parameter, a string name, and prints the string "Welcome to The Hundred Acre Wood <name>! My name is Christopher Robin."

"""


def greetings(name):
    """
    Problem: Print out a dynamic string with changing input name
    Match: F-string
    """
    print(f"Welcome to The Hundred Acre Wood {name}! My name is Christopher Robin.")


if __name__ == "__main__":
    greetings("Michael")
    greetings("Winnie the Pooh")
