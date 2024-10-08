def final_value_after_operations(operations):
    tiger = 1

    for operation in operations:
        if operation in {"bouncy", "flouncy"}:
            tiger += 1
        else:
            tiger -= 1

    print(tiger)


operations = ["trouncy", "flouncy", "flouncy"]
final_value_after_operations(operations)

operations = ["bouncy", "bouncy", "flouncy"]
final_value_after_operations(operations)
