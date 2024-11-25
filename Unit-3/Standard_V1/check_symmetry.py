"""As part of a new feature on your social media platform, you want to highlight post titles that are symmetrical, meaning they read the same forwards and backwards when ignoring spaces, punctuation, and case. Given a post title as a string, use a new algorithmic technique the two-pointer method to determine if the title is symmetrical."""


def is_symmetrical_title(title):
    if not title:
        return False

    title_list = []
    # Convert title into a list
    for char in title:
        if char not in {" ", ",", ".", ";", ":"}:
            title_list.append(char.lower())

    # Create pointer and check if not palindrome
    start, end = 0, len(title_list) - 1

    while start < end:
        if title_list[start] != title_list[end]:
            return False
        start += 1
        end -= 1

    # Return True
    return True


print(is_symmetrical_title("A Santa at NASA"))
print(is_symmetrical_title("Social Media"))
