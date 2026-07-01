def print_catchphrase(character):
    if character == "Pooh":
        return "Oh, bother!"
    elif character == "Trigger":
        return "TTFN: Ta-ta for now!"
    elif character == "Eeyore":
        return "Thanks for noticing me."
    elif character == "Christopher Robin":
        return "Silly old bear."
    else:
        return f"Sorry! I don't know {character}'s catchphrase!"

print(print_catchphrase("Pooh"))
print(print_catchphrase("Trigger"))
print(print_catchphrase("Eeyore"))
print(print_catchphrase("Christopher Robin"))
print(print_catchphrase("Christopher Robi"))