def my_function():
    a, b = 0, 100
    while a < b:
        a -= 5
        print("value of a is ", a, " and value of b is", b)


my_function()


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def calculate(expression):
    compute_map = {"+": add, "-": subtract}

    # Parse numbers and operators
    num = 0
    total = 0
    operator = "+"
    index = 0

    while index < len(expression):
        if expression[index].isdigit():
            # Parse full number
            num_start = index
            while index < len(expression) and expression[index].isdigit():
                index += 1
            num = int(expression[num_start:index])
            # Perform the operation
            total = compute_map[operator](total, num)
        else:
            # Update the current operator
            operator = expression[index]
            index += 1

    return total


# expression1 = "1-2-3+5"
# expression2 = "255"
# expression3 = "0-1+3-5"
# print(calculate(expression1))
# print(calculate(expression2))
# print(calculate(expression3))
