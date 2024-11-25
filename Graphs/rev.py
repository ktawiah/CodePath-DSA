from typing import List


def superiorElements(a: List[int]) -> List[int]:
    # Write your code here.
    result = []

    for idx1 in range(len(a)):
        for idx2 in range(idx1, len(a)):
            if a[idx2] > a[idx1]:
                break
        else:
            result.append(a[idx1])

    return result


print(superiorElements([1, 2, 3, 2]))
print(superiorElements([1, 2, 2, 1]))
