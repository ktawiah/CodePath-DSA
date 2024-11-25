# Function to initialize the board
def initialize_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

# Function to print the game board
def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Function to check if a player has won
def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or \
                all([board[j][i] == player for j in range(3)]):
            return True
    if board[0][0] == board[1][1] == board[2][2] == player or \
            board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

# Function to check if the board is full (tie game)
def is_full(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

# Function to get valid input from the player
def get_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            row, col = divmod(move, 3)
            if move < 0 or move > 8:
                print("Invalid input. Please choose a number between 1 and 9.")
            return row, col
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

# Main function for the game
def play_game():
    board = initialize_board()
    current_player = 'X'
    while True:
        print_board(board)
        print(f"Player {current_player}'s turn.")
        row, col = get_move()

        if board[row][col] != ' ':
            print("The cell is already occupied. Try again.")
            continue

        # Place the player's mark on the board
        board[row][col] = current_player

        # Check if the current player has won
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        # Check if the board is full (tie game)
        if is_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'

# Run the game
if __name__ == "__main__":
    play_game()
