"""
Batman has a bomb to defuse, and his time is running out! His butler, Alfred, is on the phone providing him with a circular array code of length n and key k.

To decrypt the code, Batman must replace every number. All the numbers are replaced simultaneously.

If k > 0, replace the ith number with the sum of the next k numbers.
If k < 0, replace the ith number with the sum of the previous k numbers.
If k == 0, replace the ith number with 0.
As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0] is code[n-1].

Given the circular array code and an integer key k, write a function decrypt() that returns the decrypted code to defuse the bomb!
"""


def defuse(code, k):
    if k == 0:
        return [0] * len(code)
    index = 0
    result = []

    while index < len(code):

        if k < 0:
            sum_k = 0
            for i in range((index + k), index):
                sum_k += code[i % len(code)]
            result.append(sum_k)

        if k > 0:
            sum_k = 0
            for i in range(index + 1, index + k + 1, 1):
                sum_k += code[i % len(code)]
            result.append(sum_k)

        index += 1

    return result


code = [5, 7, 1, 4]
k = 3
print(defuse(code, k))

code = [1, 2, 3, 4]
k = 0
print(defuse(code, k))

code = [2, 4, 9, 3]
k = -2
print(defuse(code, k))
