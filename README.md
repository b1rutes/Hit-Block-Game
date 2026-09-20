# Hit Block

A simple arcade-style brick breaker game built with Python's `turtle` module.

## Overview

Hit Block is a small game inspired by classic brick-breaker games. The player controls a paddle at the bottom of the screen and must bounce a ball to break blocks at the top. As the player clears rows of blocks, the level increases and the game becomes more challenging.

The game also includes:

- multiple lives
- score tracking
- level tracking
- a persistent high score saved in `highscore.json`
- bonus duplicate balls when a brown block is hit at the right moment

## How to Play

1. Run the game from the project folder.
2. Use the Left and Right arrow keys to move the paddle.
3. Bounce the ball upward to hit the blocks.
4. Clear all blocks to advance to the next level.
5. If you lose all lives, the game ends.

## Controls

- Left Arrow: move paddle left
- Right Arrow: move paddle right

## Project Structure

- `main.py` — game loop and setup
- `ball.py` — ball movement, collisions, duplicate-balls logic
- `block.py` — block generation and removal
- `paddle.py` — paddle behavior
- `scoreboard.py` — level, score, and high score logic
- `highscore.json` — saved high score data

## Run the Game

From the project directory, run:

```bash
python main.py
```

## Requirements

This project uses only the Python standard library, especially the built-in `turtle` module.

No external packages are required.

## Notes

The game uses a repeating `ontimer` loop to update the state about 60 times per second, creating smooth animation and gameplay.

## License

This project is provided for educational and learning purposes.
