"""The Avengers need to determine who is the strongest. Given a list of their strengths, find the maximum strength using a recursive approach without using the max() function.

Evaluate the time complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.
"""
def strongest_avenger(strengths, max_avg=float("-inf")):
    if len(strengths)==0:
        if max_avg != float("-inf"):
            return max_avg
        else:
            return -1

    current = strengths.pop()
    max_avg = current if current > max_avg else max_avg
    return strongest_avenger(strengths, max_avg)


print(strongest_avenger([88, 92, 95, 99, 97, 100, 94]))
print(strongest_avenger([50, 75, 85, 60, 90]))