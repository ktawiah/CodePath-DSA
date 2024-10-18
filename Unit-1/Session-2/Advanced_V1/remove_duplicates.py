"""
Write a function remove_dupes() that accepts a sorted array items, and removes the duplicates in-place such that each element appears only once. Return the length of the modified array. You may not create another array; your implementation must modify the original input array items
"""


def remove_dupes(items):
    # items_set = set()

    # for index, item in enumerate(items):
    #     if item not in items_set:
    #         items_set.add(item)
    #     else:
    #         items.pop(index)
    if len(items) < 2:
        return items

    start = 0
    end = 1

    while end < len(items):
        if items[start] == items[end]:
            items.pop(start)
        else:
            start += 1
            end += 1

    print(len(items))


items = ["extract of malt", "haycorns", "honey", "thistle", "thistle"]
remove_dupes(items)

items = ["extract of malt", "haycorns", "honey", "thistle"]
remove_dupes(items)
