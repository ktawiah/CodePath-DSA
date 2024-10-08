def linear_search(lst, target):
    for index, item in enumerate(lst):
        if item == target:
            return index

    # for index in range(len(lst)):
    #     if lst[index] == target:
    #         return index

    return -1


items = ["haycorn", "haycorn", "haycorn", "hunny", "haycorn"]
target = "hunny"
print(linear_search(items, target))

items = ["bed", "blue jacket", "red shirt", "hunny"]
target = "red balloon"
print(linear_search(items, target))
