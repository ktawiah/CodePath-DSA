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
