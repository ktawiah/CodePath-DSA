from string import ascii_letters

"""
Taken captive, Captain Anne Bonny has been smuggled a secret message from her crew. She will know she can trust the message if it contains all of the letters in the alphabet. Given a string message containing only lowercase English letters and whitespace, write a function can_trust_message() that returns True if the message contains every letter of the English alphabet at least once, and False otherwise.
"""


def can_trust_message(message):
    # Convert message to list of characters
    char_set = set()

    # Create a set of lowercase characters
    alphabets = set(ascii_letters.lower())

    # Iterate through message chars
    for char in message:
        # Check availability in set
        if char != " ":
            char_set.add(char)

    # Return True
    return char_set == alphabets


message1 = "sphinx of black quartz judge my vow"
message2 = "trust me"

print(can_trust_message(message1))
print(can_trust_message(message2))
