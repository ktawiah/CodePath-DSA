"""
The superhero team, The Fantastic Four, are training to increase their power levels. Their power level is represented as a power of 4. Write a recursive function that calculates the power of 4 raised to the nth power to determine their training level.

Evaluate the time complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.
"""


def power_of_four(n):
    neg = False if n > 0 else True

    n = abs(n)

    def helper(n, mult=1):
        if n == 0:
            return mult

        mult *= 4
        n -= 1
        return helper(n, mult)

    return 1 / helper(n) if neg else helper(n)


print(power_of_four(2))
print(power_of_four(-2))
