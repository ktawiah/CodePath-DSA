"""
Write a function nanana_batman() that accepts an integer x and prints the string "nanana batman!" where "na" is repeated x times. Do not use the * operator.
"""


def nanana_batman(x):
    """
    P: Return a string with recurrent 'na' x number of times

    3 -> nanana batman
    1 -> nanana batman
    0 -> batman -> strip

    S: 1. Create placeholder for new string
    2. Loop down x to 0
    3. At each x, join na to new string
    4. Append new_string with ' batman'
    5. Return result_string
    """
    # new_string = ""
    # while x != 0:
    #     new_string += "na"
    #     x -= 1

    # new_string += " batman"
    # return new_string.strip()

    # Rewritten
    return "na" * x + " batman"


if __name__ == "__main__":
    print(nanana_batman(6))
    print(nanana_batman(3))
    print(nanana_batman(0))
