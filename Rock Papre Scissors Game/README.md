# Rock Paper Scissors Game

This is a Python implementation of the classic Rock Paper Scissors game. The user plays against the computer, and the game continues in a loop until the user decides to stop.

## Features

- Uses Python's `Enum` for clear action definitions.
- Handles user input and validates choices.
- Determines the winner based on standard Rock Paper Scissors rules.
- Allows playing multiple rounds in a row.

## How to Play

1. **Run the script:**
    ```
    python rock_paper_sciossors.py
    ```

2. **Follow the prompt:**
    - Enter a number corresponding to your choice:
        - Rock [0]
        - Paper [1]
        - Scissors [2]

3. **See the result:**
    - The computer will also make a choice.
    - The winner is displayed.

4. **Play again:**
    - After each round, you can choose to play again or exit.

## Example

```
Welcome to Rock Paper Scissors!
Enter a choice (Rock[0], Paper[1], Scissors[2]): 0
Both players selected Rock. It's a tie!
Play again? (y/n): y
Enter a choice (Rock[0], Paper[1], Scissors[2]): 2
Rock beats Scissors! You win!
Play again? (y/n): n
```

## Notes

- If you enter an invalid number, the program will prompt you to try again.
- The game uses random selection for the computer's choice.

---