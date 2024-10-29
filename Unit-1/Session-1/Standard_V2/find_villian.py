"""
Write a function find_villain() that accepts a list crowd and a value villain as parameters and returns a list of all indices where the villain is found hiding in the crowd.
"""


def find_villian(crowd, villian):
    """
    P: Return all the positions of the word 'villian' in crowd_list

    ['villian', 'me', 'villian'] -> [0, 2]

    S: 1. Create a placeholder for result list
    2. Loop through list and keep track of index
    3. Add index to result list if current element == 'villian' else do nothing
    4. Return result list
    """
    result_list = []
    for index, person in enumerate(crowd):
        if person == villian:
            result_list.append(index)

    return result_list


if __name__ == "__main__":
    print(
        find_villian(
            [
                "Batman",
                "The Joker",
                "Alfred Pennyworth",
                "Robin",
                "The Joker",
                "Catwoman",
                "The Joker",
            ],
            "The Joker",
        )
    )
