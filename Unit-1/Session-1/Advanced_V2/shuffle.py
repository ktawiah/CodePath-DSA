"""
The Riddler is planning to leave a coded message to lead Batman into a trap. Write a function shuffle() that takes in a string, the Riddler's message, and encodes it using an integer array indices. The message will be shuffled such that the character at the ith position in message moves to index indices[i] in the shuffled string. You may assume len(message) is equal to the len(indices).
"""


def shuffle(message, indices):
    # Create a list to store updated characters with the same length as message
    # Iterate through indices
    # Append message at index to list of updated chars
    # print updated chars

    char_list = [""] * len(message)

    for index in range(len(indices)):
        char_list[index] = message[index]

    encode_message = "".join(char_list)

    print(encode_message)


message = "evil"
indices = [3, 1, 2, 0]
shuffle(message, indices)

message = "findme"
indices = [0, 1, 2, 3, 4, 5]
shuffle(message, indices)
