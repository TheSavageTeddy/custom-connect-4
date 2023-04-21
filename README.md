# Custom Connect 4

### A python implementation of connect 4, with customizable size and parameters, entirely played in the terminal.

## Installation

To install and play Custom Connect 4, follow the instructions below.
1. Clone this repository with
```
git clone https://github.com/TheSavageTeddy/custom-connect-4.git
```
2. `cd` into the repo that was just cloned
```
cd ./custom-connect-4
```
3. Run `main.py` with python version 3.10 or above to play the game
```
python3 main.py
```
And the game will now run. Use hotkey `CTRL + C` to send a SIGINT and exit the game at any time.

## Gameplay

When the game is ran, it will prompt you for the board dimensions and the amount of players. You should enter an integer between the ranges specified.

Example:
```
Enter board height (min 4): 6
Enter board width (min 4): 7
Enter amount of players (min 2, max 8): 2
```

Afterwards, the game will start. The columns will be labelled from 1 to the board width, and each player starting from player 1 will be prompted for their move.

```
                          . . . . . . .                           
                          . . . . . . .                           
                          . . . . . . .                           
                          . . . . . . .                           
                          . . . . . . .                           
                          . . . . . . .                           
                          1 2 3 4 5 6 7                           
Player 1's move: 
```

Also, note that the board will be centered depending on your terminal width.

A player's marker will fall to the most bottom row it can be on. If the column is full, a player cannot place a marker there. After a player enters their move, the updated board will be presented and the next player will be prompted for their move.

```
                          . . . . . . .                           
                          . . . . . . .                           
                          . . . . . . .                           
                          . . . . . . .                           
                          . . . . . . .                           
                          . . . . . . .                           
                          1 2 3 4 5 6 7                           
Player 1's move: 4
                          . . . . . . .                           
                          . . . . . . .                           
                          . . . . . . .                           
                          . . . . . . .                           
                          . . . . . . .                           
                          . . . 1 . . .                           
                          1 2 3 4 5 6 7                           
Player 2's move: 3
                          . . . . . . .                           
                          . . . . . . .                           
                          . . . . . . .                           
                          . . . . . . .                           
                          . . . . . . .                           
                          . . 2 1 . . .                           
                          1 2 3 4 5 6 7                           
Player 1's move: 
```

In the terminal, these markers should be coloured a different colour to the other markers, provided that the terminal supports ANSI codes. The marker will be the player number of the player that placed it.

This will repeat until a player wins or the game is declared a draw. A player wins by having any 4 of their own markers in a row, column or diagonal. A draw occurs when there are no moves that can be played, i.e. the board is completely filled up.

After a win or draw occurs, players will be awarded their respective points:
- 2 points for winner
- 1.5 points for all players when draw
- 1 point for loser(s)

```
Player 2's move: 5
                          . . . . . . .                           
                          . . . 1 2 . .                           
                          . 2 1 1 2 . .                           
                          . 1 2 2 2 . .                           
                          . 1 1 2 2 . .                           
                          1 2 2 1 1 1 .                           
                          1 2 3 4 5 6 7                           
Player 2 wins!
For WIN: Player 2 recieves 2 points (0 -> 2)
For LOSS: Player 1 recieves 1 point for (0 -> 1)
Press enter to continue to scoreboard...
```

Then, the scoreboard will be shown after you press enter. You will also be asked if you wish to play another round

```

    SCOREBOARD    

#1   Player 2: 2
#2   Player 1: 1

Do you want to play again? (Yes/No) 
```

Inputting "No" will exit the game. Note you can use CTRL+C to exit the game at any time.

If you input "Yes", you will be prompted again for the game settings. However, you may enter nothing to reuse the previous settings.

```
Do you want to play again? (Yes/No) yes
Please re-enter game settings, leave blank to use previous settings.
Enter board height (min 4): 
Enter board width (min 4): 
Enter amount of players (min 2): 
                          . . . . . . .                           
                          . . . . . . .                           
                          . . . . . . .                           
                          . . . . . . .                           
                          . . . . . . .                           
                          . . . . . . .                           
                          1 2 3 4 5 6 7                           
Player 1's move: 
```

That's it for playing the game! Enjoy!