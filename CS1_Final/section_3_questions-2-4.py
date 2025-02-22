"""
SECTION 3, QUESTION 2

Function that prints out a number grid as specified in assignment
"""


def draw_number_grid():

    # Iterate through range of row values
    for row_val in range(1, 13, 1):

        # Iterate through range of column values
        for col_val in range(1, 13, 1):

            # Display display of row and column values
            print(row_val * col_val, end="\t")

        print()


draw_number_grid()


"""
SECTION 3, QUESTION 3

Function that prints out a diagonal number grid as specified in assignment
"""


def draw_diagonal_number_grid():

    # Iterate through range of row values
    for row_val in range(1, 13, 1):

        # Iterate through range of column values
        for col_val in range(1, row_val + 1, 1):

            # Display display of row and column values
            print(row_val * col_val, end="\t")

        print()


draw_diagonal_number_grid()


"""
SECTION 3, QUESTION 4

Using the following algorithm, create a function in python called multiplicationByAddition that 
accomplishes the task outlined with two parameters, a and b.
"""

# Start

# Step 1 Accept first value (a)
a = int(input("Enter first value: "))

# Step 2 Accept second value (b)
b = int(input("Enter second value: "))

# Step 3 If either a or b is negative, display message saying ‘This program does not support negative numbers’, then end program
if a < 0 or b < 0:
    print("This program does not support negative numbers")
else:
    # Step 4 if both values are positive continue

    # Step 5 Create placeholder c with initial value equal to 0
    c = 0

    while b > 0:
        # Step 6 Add a to c, reduce b by 1
        c += a

        b -= 1

    # Step 7 Repeat until b = 0

    # Step 8 Display result (c)
    print("The result of c is", c)

# Stop
