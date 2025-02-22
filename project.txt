"""
Implementation of 2 player tic-tac-toe. One player should be
assigned “X” the other player “O”. Each player should take turns
choosing where they play, and their position should be shown on an
updated board. Win conditions should be implemented.
"""


def update_board(game_board, row, col, player):
    # Update the game_board with the player's move.
    if game_board[row][col] == " ":
        game_board[row][col] = player
        return True
    return False


def is_horizontal_full(game_board):
    # Check if any row is fully filled with the same symbol.
    for row in game_board:
        if row[0] == row[1] == row[2] != " ":
            return True
    return False


def is_vertical_full(game_board):
    # Check if any column is fully filled with the same symbol.
    for col in range(3):
        if game_board[0][col] == game_board[1][col] == game_board[2][col] != " ":
            return True
    return False


def is_diagonal_full(game_board):
    # Check if either diagonal is fully filled with the same symbol.
    if (game_board[0][0] == game_board[1][1] == game_board[2][2] != " ") or (
        game_board[0][2] == game_board[1][1] == game_board[2][0] != " "
    ):
        return True
    return False


def show_board(game_board):
    # Display the current board.
    print("-----------")
    for row in game_board:
        print(" | ".join(row))
        print("-----------")
    print()


def check_winner(game_board):
    # Check if there's a winner.
    if (
        is_horizontal_full(game_board)
        or is_vertical_full(game_board)
        or is_diagonal_full(game_board)
    ):
        return True
    return False


def main():
    # Create an empty 3x3 grid to represent the board.
    game_board = [[" "] * 3 for _ in range(3)]

    current_player = "X"
    turns, max_turns = 0, 9

    while turns < max_turns:
        print(f"\nPlayer {current_player}'s turn")

        # Display the board.
        show_board(game_board)

        while True:
            # Prompt the current player to make a move.
            move = int(input(f"Enter a number (1-9) for {current_player}: "))

            if 1 <= move <= 9:

                # Update corr. row and col indices
                row = (move - 1) // 3
                col = (move - 1) % 3

                # Update board
                if update_board(game_board, row, col, current_player):
                    break
                else:
                    print("Cell is already occupied, try again.")
            else:
                print("Invalid input. Please enter a number between 1 and 9.")

        # Update the turn count
        turns += 1

        # Check for winner
        if check_winner(game_board):
            show_board(game_board)
            print(f"Player {current_player} wins!")
            break

        # Switch player
        current_player = "X" if current_player == "O" else "O"

    # If all 9 turns are completed and no winner is found, declare the game as a draw.
    if turns == max_turns and not check_winner(game_board):
        show_board(game_board)
        print("It's a draw!!!")


main()
