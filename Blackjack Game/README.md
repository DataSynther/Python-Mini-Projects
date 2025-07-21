
# Blackjack Game (Python)

This is a simple implementation of the classic Blackjack game (also known as 21), adapted for Python 3.

Inspired by Al Sweigart's original version, this text-based Blackjack game includes:
- Card handling using standard symbols (♥, ♦, ♣, ♠)
- Simple betting mechanism
- Dealer logic that stops at 17
- Double Down support
- ASCII display for cards

Note: This version does **not** include splitting or insurance.

## Game Rules

- Try to get as close to 21 without going over.
- Kings, Queens, and Jacks are worth 10 points.
- Aces can be worth 1 or 11 points.
- Cards 2 through 10 are worth their face value.
- (H)it to take another card.
- (S)tand to stop taking cards.
- On your first play, you can (D)ouble down to increase your bet but must hit exactly one more time before standing.
- In case of a tie, the bet is returned to the player.
- The dealer stops hitting at 17.

## How to Play

1. Run the script.
2. You start with a balance of $5000.
3. Place a bet each round.
4. Make your moves based on the prompts.
5. Win or lose money based on the game outcome.

## Technical Details

- Python 3 required
- No external dependencies
- Uses `random` and `sys` libraries only

## To Run

```bash
python blackjack.py
```

## More Info

For more on Blackjack: [Wikipedia - Blackjack](https://en.wikipedia.org/wiki/Blackjack)

---

Happy Playing! 🎲🃏
