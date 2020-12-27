# Nim-CPU
# The Game
A terminal based python script that will play a user in the game of Nim. Nim is played with three rows of 7 5 and 3 sticks each. On a players turn they may take as little as one or all sticks from any one row. The object of the game is to make your opponent take the very last stick.
# How it Works
This program utilizes the mathematical proof of Nim to create a winning move. Working towards a nim sum, which can be explained here https://www.archimedes-lab.org/How_to_Solve/Win_at_Nim.html, the program finds the optimal move. If no good moves are available it will chose one at random. The program should win every single time if it is allowed to play first. There are a very limited number of moves that will result in a win for the player, all dependant on them knowing the winning formula. The program will also reject improper moves or inputs. This was created in the span of a few days working between classes as a small personal challenge. Perhaps someone besides myself will enjoy this as well :)
