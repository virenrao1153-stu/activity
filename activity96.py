# ------------------------------

# Create the board (9 empty spaces)
board = [" " for _ in range(9)]

# Function to print the board
def print_board():
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()

# Check if a player has won
def check_winner(player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]
    for combo in win_conditions:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

# Check for draw
def is_draw():
    return " " not in board

# Main game function
def play_game():
    current_player = "X"
    print("===== TIC TAC TOE =====")
    print_board()

    while True:
        try:
            move = int(input(f"Player {current_player} choose (1-9): ")) - 1

            if move < 0 or move > 8:
                print("❌ Invalid choice! Enter a number between 1–9.")
                continue

            if board[move] != " ":
                print("❌ Position already taken. Choose another.")
                continue

        except ValueError:
            print("❌ Please enter a valid number.")
            continue

        # Place the player's symbol
        board[move] = current_player
        print_board()

        # Check for winner
        if check_winner(current_player):
            print(f"🎉 Player {current_player} WINS!")
            break

        # Check for draw
        if is_draw():
            print("🤝 It's a DRAW!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"

# Run the game
play_game()