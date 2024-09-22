def doubled(hunny_jars):
    """
    P: Return hunny_jars that has all its elements multiplied by 2

    [1,2,3] -> [2,4,6]
    [] -> []
    [0] -> [0]

    S: 1. Create a placeholder for doubled element
    2. Loop through list
    3. Multiply element by 2 and assign output to doubled_element
    4. Replace current value by doubled_element
    5. Set doubled_element to 0
    """
    doubled_element = 0
    for index, jar in enumerate(hunny_jars):
        doubled_element = jar * 2
        hunny_jars[index] = doubled_element
        doubled_element = 0
    return hunny_jars


if __name__ == "__main__":
    print(doubled([1, 2, 3]))
