def letterCombinations(digits):
    phone = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def backtrack(path, index):
        if index == len(digits):
            result.append(path)
            return

        for char in phone.get(digits[index]):
            backtrack(path + char, index + 1)

    result = []
    if digits:
        backtrack("", 0)

    return result


print(letterCombinations("23"))
