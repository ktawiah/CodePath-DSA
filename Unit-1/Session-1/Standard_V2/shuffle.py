"""
Write a function shuffle() that accepts a list cards of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn]. Return the list in the form [x1,y1,x2,y2,...,xn,yn].


"""

from math import ceil


def shuffle(cards):
    """
    P: Return alternate combination of a list separated into two

    [1,2,3,4] -> [1,3,2,4]
    ['me',2,'you',1] -> ['me',1,2,'you']
    [1,2,3,4,5] -> [1,3,2,4,5]

    S: 1. Create placeholder for start
    2. Create place holder for mid_index and assign with upper of middle index
    3. While start < upper of mid:
      - Swap value at mid_index and start
    4. Return cards
    """
    left = 0
    new_list = []
    mid_index = int(ceil(len(cards) / 2))
    right = mid_index

    while left != mid_index and right < len(cards):
        # cards[left], cards[right] = cards[right], cards[left]
        new_list.append(cards[left])
        new_list.append(cards[right])
        left += 1
        right += 1

    if len(new_list) != len(cards):
        new_list.append(cards[-1])

    return new_list


if __name__ == "__main__":
    print(shuffle(["Joker", "Queen", 2, 3, "Ace", 7]))
    print(shuffle([9, 2, 3, "Joker", "Joker", 3, 2, 9]))
    print(shuffle([10, 10, 2, 2]))
