from string import ascii_lowercase

"""
Ground control has sent a transmission containing important information. A complete transmission is one where every letter of the English alphabet appears at least once.

Given a string transmission containing only lowercase English letters, return true if the transmission is complete, or false otherwise.
"""


def check_if_complete_transmission(transmission):
    """
    :type transmission: str
    :rtype: bool

    P: Determine if every alphabet appears at least once
    """
    # Check if transmission length less than 26
    if len(transmission) < 26:
        return False

    # Create a set of alphabets from alphabets
    alph_set = set(transmission)

    # Iterate through transmission
    for char in ascii_lowercase:

        # Return false if char not an alphabet
        if char.lower() not in alph_set:
            return False

    # Return True
    return True


transmission1 = "thequickbrownfoxjumpsoverthelazydog"
transmission2 = "spacetravel"

print(check_if_complete_transmission(transmission1))
print(check_if_complete_transmission(transmission2))
