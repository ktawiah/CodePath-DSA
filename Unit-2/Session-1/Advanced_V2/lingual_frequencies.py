"""
As a time traveling linguist, you are analyzing texts written in an ancient script. However, some words in the text are illegible and can't be deciphered. Write a function find_most_frequent_word() that accepts a string text and a list of illegible words illegibles and returns the most frequent word in text that is not an illegible word.
"""

import re


def find_most_frequent_word(text, illegibles):
    """
    P: Return most frequent word that is not illegible
    """

    # Create a set of illegibles
    illegibles_set = set(illegibles)

    # Convert text to list
    word_list = word_list = re.split(r"[ ,]+", text)

    # Get list of legibles
    legibles = []
    for word in word_list:
        if word not in illegibles_set:
            legibles.append(word.lower())

    # Create a frequency map of list elements
    freq_map = {}
    for word in legibles:
        freq_map[word] = freq_map.get(word, 0) + 1

    # Return word with most occurrences
    max_count = 0

    for word, count in freq_map.items():
        if count > max_count:
            key = word
            max_count = max(count, max_count)
    print(freq_map)
    return key


paragraph1 = "a."
illegibles1 = []
print(find_most_frequent_word(paragraph1, illegibles1))

paragraph2 = "Bob hit a ball, the hit BALL flew far after it was hit."
illegibles2 = ["hit"]
print(find_most_frequent_word(paragraph2, illegibles2))
