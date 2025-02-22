import random

# ASCII art for Rock, Paper, Scissors
ascii_art = {
    0: r''' 
               | |   
 _ _ __   _| | __
| '_/ _ \ / _| |/ /
| | | () | (_|   < 
||  \_/ \_||\_\
''',
    1: r'''
| '_ \ / ` | ' \ / _ \ '__|
| |) | (| | |) |  _/ |   
| ._/ \,| ._/ \_||   
| |         | |              
||         ||
''',
    2: r'''
__
/ __ \
( (_) |_ __
 \___,'   """""----...._
  __<  () dd       ___----'
 / _   _`._-----""""
( (__) |
 \__/
''',
}

# Prompt user to play the game
print("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.")
user_choice = int(input("Your choice: "))

# Validate user input
while user_choice not in [0, 1, 2]:
    print("Invalid choice! Please select 0, 1, or 2.")
    user_choice = int(input("Your choice: "))

# Display user's choice
print("\nYou chose:")
print(ascii_art[user_choice])

# Generate computer's choice
computer_choice = random.randint(0, 2)
print("Computer chose:")
print(ascii_art[computer_choice])

# Determine the result
if user_choice == computer_choice:
    print("The game is tied!")
elif (
    (user_choice == 0 and computer_choice == 2)
    or (user_choice == 1 and computer_choice == 0)
    or (user_choice == 2 and computer_choice == 1)
):
    print("You win!")
else:
    print("You lose!")


