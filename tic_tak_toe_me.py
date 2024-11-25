def update_board(board, row, col, player):
    """Update the board with the player's move."""
    if board[row][col] == " ":
        board[row][col] = player
        return True
    return False


def is_horizontal_full(board):
    """Check if any row is fully filled with the same symbol."""
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return True
    return False


def is_vertical_full(board):
    """Check if any column is fully filled with the same symbol."""
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True
    return False


def is_diagonal_full(board):
    """Check if either diagonal is fully filled with the same symbol."""
    if (
        board[0][0] == board[1][1] == board[2][2] != " "
        or board[0][2] == board[1][1] == board[2][0] != " "
    ):
        return True
    return False


def show_board(board):
    """Display the current game board."""
    for row in board:
        print(" | ".join(row))
        print("-----------")


def check_winner(board):
    """Check if there's a winner."""
    if is_horizontal_full(board) or is_vertical_full(board) or is_diagonal_full(board):
        return True
    return False


def main():
    board = [[" "] * 3 for _ in range(3)]
    current_player = "X"
    turns = 0
    max_turns = 9

    while turns < max_turns:
        print(f"\nPlayer {current_player}'s turn")
        show_board(board)

        while True:
            try:
                move = int(input(f"Enter a number (1-9) for {current_player}: "))
                if 1 <= move <= 9:

                    row = (move - 1) // 3
                    col = (move - 1) % 3
                    if update_board(board, row, col, current_player):
                        break
                    else:
                        print("Cell is already occupied, try again.")
                else:
                    print("Invalid input. Please enter a number between 1 and 9.")
            except ValueError:
                print("Invalid input. Please enter an integer.")

        turns += 1

        if check_winner(board):
            show_board(board)
            print(f"\nPlayer {current_player} wins!")
            break

        current_player = "O" if current_player == "X" else "X"

    if turns == max_turns and not check_winner(board):
        show_board(board)
        print("\nIt's a draw!")


main()
