def final_value_after_operations(operations):
    tigger = 1
    for word in operations:
        if word == "bouncy" or word == "flouncy":
            tigger += 1
        elif word == "trouncy" or word == "pouncy":
            tigger -= 1
    print(tigger)
    return tigger

operations = ["trouncy", "flouncy", "flouncy"]
final_value_after_operations(operations)

operations = ["bouncy", "bouncy", "flouncy"]
final_value_after_operations(operations)
