"""You make friends with a local at your latest destination, and they give you a coded message with the name of a secret beach most tourists don't know about! You are given the strings key and message which represent a cipher key and a secret message, respectively. The steps to decode the message are as follows:

Use the first appearance of all 26 lowercase English letters in key as the order of the substitution table.
Align the substitution table with the regular English alphabet.
Each letter in message is then substituted using the table.
Spaces ' ' are transformed to themselves.
For example, given key = "travel the world" (an actual key would have at least one instance of each letter in the alphabet), we have the partial substitution table of ('t' -> 'a', 'r' -> 'b', 'a' -> 'c', 'v' -> 'd', 'e' -> 'e', 'l' -> 'f', 'h' -> 'g', 'w' -> 'h', 'o' -> 'i', 'd' -> 'j').

Write a function decode_message() that accepts the strings key and message and returns a string representing the decoded message.
"""

from string import ascii_lowercase


def decode_message(key, message):
    """
    P: Decode message given the key and message

    Time Complexity: 0(m+n) if m-len(message), n-len(key)

    """
    # Handle key length less 26
    if len(key) < 26:
        return -1

    # Create a list of non-duplicates
    non_dup = []

    # Create a set to keep track of visited chars
    visited = set()

    # Iterate through key and update set and list
    for char in key:  # 0(n)
        if char not in visited and not char.isspace():  # 0(1)
            visited.add(char)
            non_dup.append(char)

    # Create a map of corresponding chars and alphabet
    char_map = {}
    for i in range(26):  # 0(1)
        char_map[non_dup[i]] = ascii_lowercase[i]

    # Convert message to a list
    message_list = list(message)  # 0(m)

    # Iterate through message string chars and replace with corr. alphabet
    for index, char in enumerate(message):  # 0(m)
        if not char.isspace():
            message_list[index] = char_map.get(char)

    return "".join(message_list)  # 0(m)


key1 = "the quick brown fox jumps over the lazy dog"
message1 = "vkbs bs t suepuv"

print(decode_message(key1, message1))
