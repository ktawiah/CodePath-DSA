"""
Write a function words_with_char() that accepts a list of strings words and a character x. Return a list of indices representing the words that contain the character x. The returned list may be in any order.
"""


def words_with_char(words, x):
    # Create placeholder for indices
    word_indices = []

    # Iterate through words
    for index, word in enumerate(words):

        # Check if char in words. Add to indices if it is else do nothing
        if x in word:
            word_indices.append(index)

    # return list of indices
    print(word_indices)


words = ["batman", "superman"]
x = "a"
words_with_char(words, x)

words = ["black panther", "hulk", "black widow", "thor"]
x = "a"
words_with_char(words, x)

words = ["star-lord", "gamora", "groot", "rocket"]
x = "z"
words_with_char(words, x)
