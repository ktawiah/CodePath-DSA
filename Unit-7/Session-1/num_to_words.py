"""
Convert a non-negative integer num to its English words representation.

 

Example 1:

Input: num = 123
Output: "One Hundred Twenty Three"
Example 2:

Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
"""


def number_to_words(num):
    if num == 0:
        return "Zero"

    # Mapping of numbers to their words
    words = {
        0: "",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten",
        11: "Eleven",
        12: "Twelve",
        13: "Thirteen",
        14: "Fourteen",
        15: "Fifteen",
        16: "Sixteen",
        17: "Seventeen",
        18: "Eighteen",
        19: "Nineteen",
        20: "Twenty",
        30: "Thirty",
        40: "Forty",
        50: "Fifty",
        60: "Sixty",
        70: "Seventy",
        80: "Eighty",
        90: "Ninety",
    }

    def helper(num):
        if num == 0:
            return ""
        elif num < 20:
            return words[num] + " "
        elif num < 100:
            return words[num // 10 * 10] + " " + helper(num % 10)
        elif num < 1000:
            return words[num // 100] + " Hundred " + helper(num % 100)
        elif num < 1_000_000:
            return helper(num // 1000) + "Thousand " + helper(num % 1000)
        elif num < 1_000_000_000:
            return helper(num // 1_000_000) + "Million " + helper(num % 1_000_000)
        else:
            return (
                helper(num // 1_000_000_000) + "Billion " + helper(num % 1_000_000_000)
            )

    return helper(num).strip()


# Example usage:
print(number_to_words(123))  # "One Hundred Twenty Three"
print(number_to_words(12345))  # "Twelve Thousand Three Hundred Forty Five"
print(
    number_to_words(1234567)
)  # "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
print(
    number_to_words(1234567891)
)  # "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
