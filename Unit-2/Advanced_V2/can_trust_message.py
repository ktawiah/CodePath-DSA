"""
Taken captive, Captain Anne Bonny has been smuggled a secret message from her
crew. She will know she can trust the message if it contains all of the letters
in the alphabet. Given a string message containing only lowercase English letters
and whitespace, write a function can_trust_message() that returns True if the me
ssage contains every letter of the English alphabet at least once, and False
otherwise.

"""
from string import ascii_lowercase

def can_trust_message(message):
    # Convert message into a set
    message_set = set(message)

    # Iterate through alphabets
    for char in ascii_lowercase:
        
        # Return false if alphabet not found in message set
        if char not in message_set:
            return False

    # Return True
    return True

message1 = "sphinx of black quartz judge my vow"
message2 = "trust me"

print(can_trust_message(message1))
print(can_trust_message(message2))
