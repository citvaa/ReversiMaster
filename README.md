# ReversiMaster

This project involves developing a program for playing the game Reversi (Othello) in a human vs. computer mode. The game is played by two players (White and Black) on an 8x8 board, and it starts with 4 central discs. The black player always begins the game.

## Project Description

In Reversi, players take turns placing a new disc on the board to form a line (horizontal, vertical, or diagonal) with an existing disc that must include at least one opposing disc. When a line is formed, all opposing discs on that line are flipped to the current player's color. The game continues until the board is full or a player has no more legal moves. The player with the most discs at the end wins.

## Features

- **Game Mechanics:**
  - Display the board in the console with clearly marked fields after each move.
  - Offer available moves to the user for the next turn.
  - Allow players to make their moves according to the game rules.
  - Flip the opponent's discs when a valid move is made.

- **Advanced Features:**
  - Implementation of trees and hash maps for efficient game state management.
  - Minimax algorithm with enhancements using alpha-beta pruning for optimal computer moves.
  - Heuristic evaluation to determine the best move.
  - Variable depth for more dynamic gameplay.
  - Ensuring the computer makes its move within 3 seconds for a smooth gaming experience.

By implementing these features, the game provides an engaging and challenging experience for the user while demonstrating advanced programming techniques and data structures.
