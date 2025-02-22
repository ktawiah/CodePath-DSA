from random import choice


def guess_char():
    guessed_char = input("Guess: ")

    while not guess_char.isalpha:
        print("Your guess must be a lowercase character.\n")
        guessed_char = input("Guess: ")

    return guess_char


def play():
    # Pick random word to work with
    words = ["egg plant"]

    selected_word = choice(words)

    word_map = {}

    for i, char in enumerate(selected_word):
        word_map[char] = word_map.get(char, []) + [i]

    total_guesses = 10

    while total_guesses:
        guessed_char = guess_char()

        if guessed_char in word_map:
            if word_map.get(guessed_char):
                word_map.get(guessed_char).pop()


play()
