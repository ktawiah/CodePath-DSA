"""
Time -> Upper bound

0(1), constant time, space
0(n), linear time

f(x) = x^3 + 2x

If nested -> Multiply
If on the same line add
"""

nums = [1, 2, 3, 4, 8, 9, 7]
n = len(nums)
# 2 -> 2
# 3 -> 3
# 6 -> 6


# 0, 4
# f(n) = n * 1 -> n
# for i in range(n):  # n
#     print(i)  # 1


# f(n) = n * n * 1 -> n^2 -> 0(n^2)
# f(n) = n * 1 * 1 -> n -> 0(n)
# for i in range(n):  # n
#     for j in range(2):  # 1
#         print(i, j)  # 1

# i = 0
#   j = 0, 1, 2
# i = 1
#   j = 0, 1, 2
# i = 2
#   j = 0, 1, 2
# for i in range(len(nums)): # 0(n)
#     print(nums[i]) # 0

# log10(n) -> n = 100

# n = 100
# iteration = 0
# while n > 0:
#     print(f"At iteration {iteration} = {n}")
#     iteration += 1
#     n = n // 10

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = 1

while n < len(nums) + 1:
    print(nums[0 : n + 1])
    print(n)
    n = n * 2

"""

i -> 0, 6

0 -> 1
1 -> 2
2 -> 3
4 -> 4

"""
