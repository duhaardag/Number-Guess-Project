# Number Guessing Game

## Description

Welcome to the Number Guessing Game! This is a simple Python program that allows players to guess a randomly generated number within a specified range. The player is given a limited number of chances to guess the correct number.

## How to Play

1. Run the Python script `number_guessing_game.py`.
2. The game will prompt you to guess a number within a specified range.
3. Enter your guess.
4. You will receive hints whether your guess is too small or too big.
5. Continue guessing until you either guess the correct number or run out of chances.

## Configuration

You can customize the game by adjusting the following parameters in the script:

- `min_number`: The minimum value of the number to be guessed (default is 1).
- `max_number`: The maximum value of the number to be guessed (default is 100).
- `chance`: The number of chances given to the player (default is 5).

Example:

```python
number_guessing_game(1, 50, 5)
