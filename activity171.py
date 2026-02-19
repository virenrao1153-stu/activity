import random

# Possible moves
moves = ["rock", "paper", "scissors"]

# Score tracking
player_score = 0
ai_score = 0

# Store player's past moves
player_history = []

def get_ai_move():
    # If no history, choose random
    if not player_history:
        return random.choice(moves)

    # Count most frequent player move
    most_common = max(set(player_history), key=player_history.count)

    # AI chooses move that beats player's most common move
    if most_common == "rock":
        return "paper"
    elif most_common == "paper":
        return "scissors"
    else:
        return "rock"

def decide_winner(player, ai):
    global player_score, ai_score

    if player == ai:
        print("🤝 It's a tie!")

    elif (
        (player == "rock" and ai == "scissors") or
        (player == "paper" and ai == "rock") or
        (player == "scissors" and ai == "paper")
    ):
        print("🎉 You win this round!")
        player_score += 1
    else:
        print("💻 AI wins this round!")
        ai_score += 1

def play_game():
    print("🎮 Welcome to Rock Paper Scissors with AI!")
    print("Type rock, paper, scissors or quit to exit\n")

    while True:
        player_move = input("Your move: ").lower()

        if player_move == "quit":
            print("\nFinal Score:")
            print("You:", player_score)
            print("AI:", ai_score)
            print("👋 Thanks for playing!")
            break

        if player_move not in moves:
            print("❌ Invalid choice! Try again.")
            continue

        player_history.append(player_move)
        ai_move = get_ai_move()

        print("AI chose:", ai_move)
        decide_winner(player_move, ai_move)

        print("Score -> You:", player_score, "| AI:", ai_score)
        print("-" * 30)

# Run game
play_game()