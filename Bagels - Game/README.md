# Bagels - Deductive Logic Game

Bagels is a classic deductive logic game where you must guess a secret number based on clues provided after each guess. This Python implementation is inspired by Al Sweigart's original version.

## How to Play

- The computer thinks of a secret number with **no repeated digits** (default: 3 digits).
- You have **10 tries** to guess the secret number.
- After each guess, you receive clues:
  - **Fermi**: One digit is correct and in the right position.
  - **Pico**: One digit is correct but in the wrong position.
  - **Bagels**: No digit is correct.

**Example:**  
If the secret number is `248` and your guess is `843`, the clues would be:  
`Fermi Pico`  
(`4` is correct and in the right place, `8` is correct but in the wrong place.)

## Game Features

- Adjustable number of digits and guesses by changing `NUM_DIGITS` and `MAX_GUESSES` in the code.
- Ensures the secret number has unique digits.
- Provides clear feedback after each guess.
- Option to play multiple rounds.

## Getting Started

### Requirements

- Python 3.x

### Running the Game

1. Save the script as `bagels.py`.
2. Open a terminal and navigate to the script's directory.
3. Run the game:
    ```
    python bagels.py
    ```

4. Follow the on-screen instructions to make your guesses.

## Customization

- **Change Difficulty:**  
  Edit the following lines at the top of the script to adjust the game:
  ```python
  NUM_DIGITS = 3      # Number of digits in the secret number
  MAX_GUESSES = 10    # Number of allowed guesses
  ```

## Example Session

```
Bagels, a deductive logic game.
Originally, invented by Al Sweigart al@inventwithpython.com

I am thinking of a 3-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
When I say:    That means:
Pico         One digit is correct but in the wrong position.
Fermi        One digit is correct and in the right position.
Bagels       No digit is correct.

Guess #1:
> 123
Bagels
Guess #2:
> 456
Pico
Guess #3:
> 426
Fermi Pico
...
Hey!! You guessed it right!!
Do you want to play again? (yes or no)
```

## Credits

- Original concept by [Al Sweigart](https://inventwithpython.com/)
- Python implementation and enhancements

---

Enjoy playing and improving your deductive reasoning skills!