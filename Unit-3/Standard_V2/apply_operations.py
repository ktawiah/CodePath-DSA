"""You are given a 0-indexed array ratings of size n consisting of non-negative integers. Each integer represents the rating of a show in a streaming service.

You need to apply n - 1 operations to this array where, in the ith operation (0-indexed), you will apply the following on the ith element of ratings:

If ratings[i] == ratings[i + 1], then multiply ratings[i] by 2 and set ratings[i + 1] to 0. Otherwise, you skip this operation.
After performing all the operations, shift all the 0's to the end of the array.

For example, the array [1,0,2,0,0,1] after shifting all its 0's to the end, is [1,2,1,0,0,0].

Return the resulting array of ratings."""


def apply_rating_operations(ratings):
    stack = []

    for rating in ratings:
        if stack and stack[-1] == rating:
            stack[-1] *= 2
        elif rating != 0:
            stack.append(rating)

    stack.extend([0] * (len(ratings) - len(stack)))

    return stack


print(apply_rating_operations([1, 2, 2, 1, 1, 0]))
print(apply_rating_operations([0, 1]))
