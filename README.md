# Rock-Paper-Scissors-with-Functions-and-List-in-Python

### Goal

Implement a Rock, Paper, Scissors program in Python using functions and a list.

### High Level Requirements

1. Ask each player for their name. Print their name during game prompts.
2. Ask each player to choose rock, paper, or scissors. Confirm it's a valid choice.
3. Apply game rules: rock beats scissors, scissors beats paper, paper beats rock, ties.
4. Ask if players would like to play again.
5. Track game results.
6. Display the result to the players.
### Plan before you write code.

Answer these questions:

- **What are the steps?**
- **What is the step sequence?**
- **Which decisions need to be made?**
- **What repeats (loops)?**
- **What data is needed?**
- **Which data types are appropriate?**
- **Can we extract repeated code into a function definition?**
- **Can we extract code that does one thing well into a function definition?**

### What are the steps?

1. **Initialize**: Set up the game variables, such as total games, player wins, and ties.
2. **Welcome Message**: Display a welcome message to the players.
3. **Player Input**: Ask each player for their name.
4. **Game Loop**: Continuously play the game until players decide not to continue.
   - **Sub-steps**:
     - Get player choices.
     - Determine the winner based on the game rules.
     - Display the result.
     - Ask if players want to play again.

### What is the step sequence?

1. Initialize global variables.
2. Display welcome message.
3. Enter a loop to play the game.
   - Get player names.
   - Enter a nested loop to play a single game.
     - Get player choices.
     - Determine the winner.
     - Display the result.
     - Ask if players want to play again.
   - Exit the loop if players choose not to play again.
4. Display total game results.
5. Say goodbye.

### Which decisions need to be made?

1. Whether to play another game after the current one.
2. The choices made by each player in a single game.
3. Determining the winner based on the game rules.
4. Whether to display the results and play again.

### What repeats (loops)?

1. The overall game loop continues until players decide not to play.
2. Within the game loop, there is a nested loop for playing a single game.
3. The game asks if players want to play again after each round.

### What data is needed?

1. Player names.
2. Player choices.
3. Game results (total games, player wins, ties).

### Which data types are appropriate?

1. Strings for player names.
2. Integers for player choices and game results.
3. Booleans for deciding whether to play again.

### Can we extract repeated code into a function definition?

1. Yes, the logic for determining the winner based on choices can be extracted into a function.

### Can we extract code that does one thing well into a function definition?

1. Yes, the code for playing a single game (getting choices, determining the winner, displaying results) can be extracted into a function.

### Complete and Continue

1. Ensure that the code is modular and follows good practices.
2. Continue by testing the code and making adjustments as needed.
3. Consider adding error handling for unexpected input from users.
4. Enhance user experience with additional features if desired.

Planning before writing code helps create a clear roadmap and leads to more organized and maintainable code.

## Acknowledgments

Special thanks and a shout out to the following individuals and organizations:

- [Dev10](https://www.dev-10.com/)

## Contact

If you have any questions or feedback, feel free to reach out to [Amir](https://www.linkedin.com/in/amirhossein-olyaei/).

## License

This project is licensed under the MIT License.
