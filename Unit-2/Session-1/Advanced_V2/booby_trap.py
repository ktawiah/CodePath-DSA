"""
Captain Feathersword has found another pirate's buried treasure, but they suspect it's
booby-trapped. The treasure chest has a secret code written in pirate language, and
Captain Feathersword believes the trap can be disarmed if the code can be balanced.
A balanced code is one where the frequency of every letter present in the code is equal.
To disable the trap, Captain Feathersword must remove exactly one letter from the message. Help Captain Feathersword determine if it's possible to remove one letter to balance the pirate code.

Given a 0-indexed string code consisting of only lowercase English letters, write a
function is_balanced() that returns True if it's possible to remove one letter so that
the frequency of all remaining letters is equal, and False otherwise.
"""

def is_balanced(code):
    """
    P: Determine if count of chars in code can be the same by removing one char
    """

    # Create a freq_map
    freq_map = {}

    for char in code:
        freq_map[char] = freq_map.get(char, 0) + 1

    # Create count for number of deviations
    count = 0
    
    # Iterate through map
    values = list(freq_map.values())
    for index in range(len(values)-1):

        # Update count
        if values[index] != values[index+1]:
            count +=1

    # Return count
    return count == 1

code1 = "arghh"
code2 = "haha"

print(is_balanced(code1)) 
print(is_balanced(code2)) 
