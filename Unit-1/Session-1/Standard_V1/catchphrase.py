"""
Write a function print_catchphrase() that accepts a string character as a parameter and prints the catchphrase of the given character as outlined in the table below.

Character ->	Catchphrase
----------      -----------
"Pooh"	->    "Oh bother!"
"Tigger" ->	"TTFN: Ta-ta for now!"
"Eeyore" ->	"Thanks for noticing me."
"Christopher Robin" ->	"Silly old bear."

If the given character does not match one of the characters included above, print "Sorry! I don't know <character>'s catchphrase!"
"""


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
