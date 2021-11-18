# Sudoku Solver

Welcome to the sudoku solver.:smiley: This is a project that contains a program allowing players to solve any standard 9 by 9 valid sudoku board that they wish. A proper sudoku board contains at least 17 clues and thus has one and only unique solution. In this case, only proper sudoku boards will be considered valid setup board inputs. Finally, upon running and setting up the program, player will be given two choices repeatedly in the next step, solve the puzzle or check the solution, until the player correctly answers the puzzle or gives up and checks the solution.

---
## Execution instructions
### Requirements:

**Python 3** installation is required in your system for the execution of this program. If you don't have it installed, check this installation [guidline](https://realpython.com/installing-python/).

### How to run the program:
Open your terminal or command line interface at the folder where the script of the program is, and run the following:
```bash
python3 sudoku.py
```
There are two `.txt` files called `example1.txt` and `example2.txt` included. In there, example sudoku board setups are provided, with their solutions included as well. You can input these parameters to setup the program when prompted, and check with the answers prospectively. You are welcome to setup and test any valid 9 by 9 sudoku board of your own.

---
## Execution example
Here is an example of successfully running the program with the setups in `example2.txt`
>$ python3 sudoku.py
>Hello player!
Please enter your initial board to begin the game(Enter row by row for exactly 9 rows, for each row enter a list with exactly 9 numbers separated by only commas and no space in between each number):
>
>Enter your 1th row: 0,0,0,8,0,0,4,0,3
[0, 0, 0, 8, 0, 0, 4, 0, 3]
Enter your 2th row: 2,0,0,0,0,4,8,9,0
[2, 0, 0, 0, 0, 4, 8, 9, 0]
Enter your 3th row: 0,9,0,0,0,0,0,0,2
[0, 9, 0, 0, 0, 0, 0, 0, 2]
Enter your 4th row: 0,0,0,0,2,9,0,1,0
[0, 0, 0, 0, 2, 9, 0, 1, 0]
Enter your 5th row: 0,0,0,0,0,0,0,0,0
[0, 0, 0, 0, 0, 0, 0, 0, 0]
Enter your 6th row: 0,7,0,6,5,0,0,0,0
[0, 7, 0, 6, 5, 0, 0, 0, 0]
Enter your 7th row: 9,0,0,0,0,0,0,8,0
[9, 0, 0, 0, 0, 0, 0, 8, 0]
Enter your 8th row: 0,6,2,7,0,0,0,0,1
[0, 6, 2, 7, 0, 0, 0, 0, 1]
Enter your 9th row: 4,0,3,0,0,6,0,0,0
[4, 0, 3, 0, 0, 6, 0, 0, 0]
The board you entered is:
0 0 0 8 0 0 4 0 3
2 0 0 0 0 4 8 9 0
0 9 0 0 0 0 0 0 2
0 0 0 0 2 9 0 1 0
0 0 0 0 0 0 0 0 0
0 7 0 6 5 0 0 0 0
9 0 0 0 0 0 0 8 0
0 6 2 7 0 0 0 0 1
4 0 3 0 0 6 0 0 0
>
>Your board is valid!
Hello player, please give your instruction:
If you want to solve the puzzle with the current board, please input the number 1. If you want to know the answer, input 2.
>
>Enter your instruction(1 or 2)：1
Please enter your solution（Enter row by row for exactly 9 rows, for each row enter a list with exactly 9 numbers separated by only commas and no space in between each number):
Enter 1th row: 7,5,1,8,9,2,4,6,2
Enter 2th row: 2,3,6,1,7,4,8,9,5
Enter 3th row: 8,9,4,5,6,3,1,7,2
Enter 4th row: 6,4,5,3,2,9,7,1,8
Enter 5th row: 1,2,9,4,8,7,3,5,6
Enter 6th row: 3,7,8,6,5,1,2,4,9
Enter 7th row: 9,1,7,2,3,5,6,8,4
Enter 8th row: 5,6,2,7,4,8,9,3,1
Enter 9th row: 4,8,3,9,1,6,5,2,7
Your answer is wrong, try again please!
>
>Enter your instruction(1 or 2)：1
Please enter your solution（Enter row by row for exactly 9 rows, for each row enter a list with exactly 9 numbers separated by only commas and no space in between each number):
Enter 1th row: 7,5,1,8,9,2,4,6,3
Enter 2th row: 2,3,6,1,7,4,8,9,5
Enter 3th row: 8,9,4,5,6,3,1,7,2
Enter 4th row: 6,4,5,3,2,9,7,1,8
Enter 5th row: 1,2,9,4,8,7,3,5,6
Enter 6th row: 3,7,8,6,5,1,2,4,9
Enter 7th row: 9,1,7,2,3,5,6,8,4
Enter 8th row: 5,6,2,7,4,8,9,3,1
Enter 9th row: 4,8,3,9,1,6,5,2,7
Congratulations, you've solved the puzzle! Bye now.
