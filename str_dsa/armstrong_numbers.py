"""
An Amrstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.
"""

def is_armstrong_number(N):
    org_N = N
    cube_sum = 0
    while N:
        cube_sum += (N%10) ** 3
        N //= 10

    return  cube_sum == org_N

print(is_armstrong_number(153))
print(is_armstrong_number(145))
