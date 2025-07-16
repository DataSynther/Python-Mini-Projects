# Birthday Paradox Simulator

This Python script demonstrates the famous Birthday Paradox using a Monte Carlo simulation. It shows how likely it is for at least two people in a group to share the same birthday, even in surprisingly small groups.

## How It Works

- The user chooses a group size (up to 100).
- The script generates random birthdays for the group and checks for matches.
- It then runs 100,000 simulations to estimate the probability of a shared birthday in a group of that size.

## Features

- Explains the Birthday Paradox and shows a sample group of generated birthdays.
- Reports if there is a matching birthday in your sample group.
- Runs a large number of simulations to estimate the probability.
- Displays progress updates during the simulation.

## Requirements

- Python 3.x (no external libraries required)

## Usage

1. Save the script as `birthday_paradox.py`.
2. Run the script:
    ```
    python birthday_paradox.py
    ```
3. Enter the number of people in the group when prompted (1–100).
4. Review the generated birthdays and simulation results.

## Example Output

```
How many birthdays shall I generate? (Max 100)
> 23
Generating 23 birthdays...
Birthday #1: March 14th
Birthday #2: July 8th
...
Checking for matching birthdays...
Matching birthday found: April 21st
Done.

Generating 23 random birthdays 100,000 times...
0 simulations run...
10000 simulations run...
...
100,000 simulations run.
Out of 100,000 simulations of 23 birthdays, there were 50713 simulations with matching birthdays.
This means that the probability of two people having matching birthdays in a group of 23 is about 50.71 %.
This is surprisingly high, even for a group as small as 23.
Thanks for playing!
```

## References

- [Birthday Problem - Wikipedia](https://en.wikipedia.org/wiki/Birthday_problem)

---

Enjoy exploring probability with the Birthday Paradox!