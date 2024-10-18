"""
Write a function squash_spaces() that takes in a string s as a parameter and returns a new string with each substring with consecutive spaces reduced to a single space. Assume s can contain leading or trailing spaces, but in the result should be trimmed. Do not use any of the built-in trim methods.
"""


def squash_spaces(s: str):
    # Split words in s based on space encountered
    # Loop through new list and trim words
    # Create new string with properly formatted space
    # Trim new string and return

    s_list = s.split(" ")
    new_s = []

    for word_idx in range(len(s_list)):
        if s_list[word_idx]:
            new_s.append(s_list[word_idx])

    for word_idx, word in enumerate(new_s):
        s_list[word_idx] = word.strip()

    print(" ".join(new_s))


s = "   Up,     up,   and  away! "
squash_spaces(s)

s = "With great power comes great responsibility."
squash_spaces(s)
