import random

def get_valid_input(prompt, valid_choices):
    while True:
        choice = input(prompt).lower()
        if choice in valid_choices:
            return choice
        else:
            print("Invalid input. Try again.")

def play_single_player():
    wins = 0
    losses = 0

    while True:
        guess = get_valid_input("Guess Heads or Tails (h/t): ", ["h", "t"])

        toss = random.choice(["h", "t"])
        print("Coin toss result:", "Heads" if toss == "h" else "Tails")

        if guess == toss:
            print("You win!")
            wins += 1
        else:
            print("You lose!")
            losses += 1

        print(f"Score → Wins: {wins}, Losses: {losses}")

        again = get_valid_input("Play again? (y/n): ", ["y", "n"])
        if again == "n":
            break

    print("Final Score:")
    print(f"Wins: {wins}, Losses: {losses}")


def play_two_players():
    p1_score = 0
    p2_score = 0

    while True:
        p1 = get_valid_input("Player 1 (Heads/Tails) (h/t): ", ["h", "t"])
        p2 = get_valid_input("Player 2 (Heads/Tails) (h/t): ", ["h", "t"])

        toss = random.choice(["h", "t"])
        print("Coin toss result:", "Heads" if toss == "h" else "Tails")

        if p1 == toss:
            print("Player 1 wins this round!")
            p1_score += 1
        if p2 == toss:
            print("Player 2 wins this round!")
            p2_score += 1
        if p1 != toss and p2 != toss:
            print("No one wins this round!")

        print(f"Score → Player 1: {p1_score}, Player 2: {p2_score}")

        again = get_valid_input("Play again? (y/n): ", ["y", "n"])
        if again == "n":
            break

    print("Final Score:")
    print(f"Player 1: {p1_score}, Player 2: {p2_score}")


def main():
    print("=== Coin Toss Game ===")

    mode = get_valid_input(
        "Choose mode: 1 = Single Player, 2 = Two Players: ",
        ["1", "2"]
    )

    if mode == "1":
        play_single_player()
    else:
        play_two_players()

    print("Thanks for playing!")


# Run the game
main()