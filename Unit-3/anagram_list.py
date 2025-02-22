question = ["cat", "tab", "ate", "eat", "bat", "tac"]


anagrams = []


def is_anagram(str1, str2):
    map_1, map_2 = {}, {}

    for char in str1:
        map_1[char] = map_1.get(char, 0) + 1

    for char in str2:
        map_2[char] = map_2.get(char, 0) + 1

    return map_1 == map_2


def list_anagrams(str_list):

    if len(str_list) == 0:
        return

    curr = []

    el = str_list[0]

    curr.append(el)

    str_list = str_list[1::]

    new_list = str_list

    for item in str_list:

        if is_anagram(el, new_list[new_list.index(item)]):

            curr.append(item)

            new_list.pop(new_list.index(item))

    anagrams.append(curr)

    list_anagrams(new_list)


list_anagrams(question)

print(anagrams)
