def print_catchphrase(character):
    """
    Problem: Print a specific string based on the character input
    Ex: Pooh -> Oh brother!

    1. Store conditions and output in dictionary
    2. Print out output if condition exists else return error string
    """
    catchphrase_map = {
        "Pooh": "Oh bother!",
        "Tiger": "TTFN: Ta-ta for now!",
        "Eeyore": "Thanks for noticing me.",
        "Christopher Robin": "Silly old bear.",
    }

    if character in catchphrase_map:
        print_catchphrase(catchphrase_map.get(character))
    else:
        print(f"Sorry! I don't know {character}'s catchphrase!")


if __name__ == "__main__":
    print_catchphrase("Pooh")
    print_catchphrase("Piglet")
