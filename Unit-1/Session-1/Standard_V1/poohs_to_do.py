"""
Write a function print_todo_list() that accepts a list of strings named tasks. The function should then number and print each task on a new line using the format:

Pooh's To Dos:
1. Task 1
2. Task 2
...
"""


def print_todo_list(tasks):
    """
    P: Print an order list on tasks

    S: 1. Loop through tasks
    2. Keep track of index, and value
    3. Format output string with index and value
    """
    print("Pooh's To Dos:\n")
    for index, task in enumerate(tasks):
        print(f"{index+1}. {task}\n")


if __name__ == "__main__":
    print_todo_list(
        [
            "Count all the bees in the hive",
            "Chase all the clouds from the sky",
            "Think",
            "Stoutness Exercises",
        ]
    )
