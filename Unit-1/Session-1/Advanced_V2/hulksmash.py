"""
Write a function hulk_smash() that accepts an integer n and returns a 1-indexed string array answer where:

answer[i] == "HulkSmash" if i is divisible by 3 and 5.
answer[i] == "Hulk" if i is divisible by 3.
answer[i] == "Smash" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
"""


def hulk_smash(n):
    # Create answer list
    # Iterate from 1 -> n
    # Add value if value at index meets condition

    answer = []

    for index in range(1, n + 1):
        if index % 3 == 0 and index % 5 == 0:
            answer.append("HulkSmash")
        elif index % 3 == 0:
            answer.append("Hulk")
        elif index % 5 == 0:
            answer.append("Smash")
        else:
            answer.append(index)

    print(answer)


n = 3
hulk_smash(n)

n = 5
hulk_smash(n)

n = 15
hulk_smash(n)
