# Global variables to track game results
total_games = 0
player1_wins = 0
player2_wins = 0
ties = 0


def read_required_string(prompt):
    """
    Prompt the user for input and ensure a non-empty string is returned.

    Parameters:
    - prompt (str): The prompt to display to the user.

    Returns:
    - str: The non-empty string entered by the user.
    """
    return input(prompt).strip()


def get_player_choice(player_name):
    """
    Get and validate the player's choice for Rock, Paper, or Scissors.

    Parameters:
    - player_name (str): The name of the player.

    Returns:
    - int: The validated choice (1 for Rock, 2 for Paper, 3 for Scissors).
    """
    while True:
        choice = read_required_string(
            f"{player_name}, choose.\n1. Rock\n2. Paper\n3. Scissors\nSelect [1-3]: ")
        if choice in ['1', '2', '3']:
            return int(choice)
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")


def apply_rules(p1_choice, p2_choice):
    """
    Apply the game rules and determine the winner.

    Parameters:
    - p1_choice (int): Player 1's choice (1 for Rock, 2 for Paper, 3 for Scissors).
    - p2_choice (int): Player 2's choice (1 for Rock, 2 for Paper, 3 for Scissors).

    Returns:
    - str: The result of the game (win, lose, or tie).
    """
    global player1_wins, player2_wins, ties  # pylint: disable=global-statement

    if p1_choice == p2_choice:
        ties += 1
        return "It's a tie."
    elif (p1_choice == 1 and p2_choice == 3) or (p1_choice == 2 and p2_choice == 1) or (p1_choice == 3 and p2_choice == 2):
        player1_wins += 1
        return "Player 1 wins."
    else:
        player2_wins += 1
        return "Player 2 wins."


def get_choice_string(choice):
    """
    Get the corresponding choice string for Rock, Paper, or Scissors.

    Parameters:
    - choice (int): The numeric choice (1 for Rock, 2 for Paper, 3 for Scissors).

    Returns:
    - str: The corresponding choice string.
    """
    if choice == 1:
        return 'Rock'
    elif choice == 2:
        return 'Paper'
    elif choice == 3:
        return 'Scissors'
    else:
        return 'Unknown Choice'


def play_game(player1_name, player2_name):
    """
    Play a single game of Rock, Paper, Scissors.

    Parameters:
    - player1_name (str): The name of Player 1.
    - player2_name (str): The name of Player 2.
    """
    global total_games  # pylint: disable=global-statement

    total_games += 1

    player1_choice = get_player_choice(player1_name)
    player2_choice = get_player_choice(player2_name)

    # Use the extracted function to get choice strings
    player1_choice_str = get_choice_string(player1_choice)
    player2_choice_str = get_choice_string(player2_choice)

    print(f"{player1_name} chose {player1_choice_str}.")
    print(f"{player2_name} chose {player2_choice_str}.")

    result = apply_rules(player1_choice, player2_choice)
    print(result)


def run():
    """
    Run the Rock, Paper, Scissors game.

    Handles player names input and game execution.
    """
    global total_games, player1_wins, player2_wins, ties  # pylint: disable=global-statement

    player1_name = read_required_string("Player #1, Enter your name: ")
    player2_name = read_required_string("Player #2, Enter your name: ")

    while True:
        play_game(player1_name, player2_name)

        play_again = read_required_string("Play again? [y/n]: ").lower()
        if play_again != 'y':
            break

    print(f"\nTotal games: {total_games}")
    print(f"{player1_wins=}, {player2_wins=}, Ties: {ties}")
    print("Goodbye.")


if __name__ == "__main__":
    print("Welcome to RPS.\n")
    run()
