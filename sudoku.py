# Global variable that keeps track of the correct solution to the sudoku board in a 9x9 grid
solution = [[9] for x in range(9)]
# Global variable that keeps track of the number of empty cells in a board, gets updated regularly
num_empty = 0
# Global variable that keeps track of where the empty cells are, gets updated regularly
empty_location = [0, 0]

# Check whether a solution is valid 
def check_board_valid(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] < 1 or grid[i][j] > 9 \
               or not check_cell_valid(i, j, grid):
                return False
    return True # The fixed cells are valid

# Check whether grid[i][j] is valid at the i's row
def check_row_safe(i, j , grid):
    for column in range(9):
        if column != j and grid[i][column] == grid[i][j]:
            return False
    return True
    
# Check whether grid[i][j] is valid at the j's column
def check_col_safe(i, j, grid):
    for row in range(9):
        if row != i and grid[row][j] == grid[i][j]:
            return False
    return True
    
# Check whether grid[i][j] is valid in the 3 by 3 box
def check_box_safe(i, j, grid):
    for row in range((i // 3) * 3, (i // 3) * 3 + 3):
        for col in range((j // 3) * 3, (j // 3) * 3 + 3):
            if row != i and col != j and grid[row][col] == grid[i][j]:
                return False
    return True
       
# Check whether grid[i][j] is valid in the grid 
def check_cell_valid(i, j, grid):
    # The current value at grid[i][j] is valid, returns true if only all of the conditions below are True
    return check_row_safe(i, j, grid) and \
        check_col_safe(i, j, grid) and \
        check_box_safe(i, j, grid) 

# Helper function that prints the board, each number is separated by space
def print_board(grid):
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end=" ")
        print()
    print()

# Helper function that finds the empty cells in the grid, and updates the number, return 0 if all filled
def find_empty_num(grid):
    total_empty = 0
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                total_empty = total_empty + 1
    return total_empty

#Helper function that finds the location of the empty cell in the grid and updates the local variable                
def find_empty_spot(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                empty_location[0] = i
                empty_location[1] = j
                return True
    return False

# Backtracking recursion to solve the board
def solve_board(grid):
    # Base case: If there are no empty spots left, then the board is solved
    if find_empty_spot(grid) == False:
        solution = grid
        return True
    
    row_empty = empty_location[0]
    col_empty = empty_location[1]

    # Try number from 1 to 9, check if valid at prosepective cell, if it's valid then continues, if not then reset/backtrack to 0 and try again 
    for num in range(1, 10):
        grid[row_empty][col_empty] = num

        if check_cell_valid(row_empty, col_empty, grid):
            if(solve_board(grid)):
                return True

        grid[row_empty][col_empty] = 0
    return False

def main():
    # This variable initiated here is a place holder for the initial setup of the sudoku board
    input_grid = [[9] for x in range(9)] 
    run = True

    while True:
        print("Hello player! \nPlease enter your initial board to begin the game(Enter row by row for exactly 9 rows, for each row enter a list with exactly 9 numbers separated by only commas and no space in between each number): \n")
        # Populate the player input grid
        for i in range(9):
            row_str = input("Enter your %dth row: " % (i+1))
            row = list(row_str.split(','))

            # User prompt read string, convert it to integer
            for j in range(9):
                row[j] = int(row[j])
            print(row)
            input_grid[i] = row

        print("The board you entered is: ")
        print_board(input_grid)

        num_empty = find_empty_num(input_grid)
        
        # The minimum number of clues for a sudoku to have a unique solution is 17, else the board is invalid
        if (81 - num_empty) < 17:
            print("Invalid board, too many empty cells! Number of clues in the board has to be at least 17.")
        else:
            print("Your board is valid!")
            # Update the global variable with the initial board, and solve the board in the background
            solution = input_grid
            solve_board(input_grid)

            print("Hello player, please give your instruction: ")
            print("If you want to solve the puzzle with the current board, please input the number 1. If you want to know the answer, input 2. \n")
    
            # Run the main functionality of the program
            while run:
                val = input("Enter your instruction(1 or 2)：")

                if val == '1':
                    # This variable is a grid that keeps track of the player's inputs
                    player_grid = [[9] for x in range(9)]
                    print("Please enter your solution（Enter row by row for exactly 9 rows, for each row enter a list with exactly 9 numbers separated by only commas and no space in between each number): ")
            
                    #populate the player input grid
                    for i in range(9):
                        row_str = input("Enter %dth row: " % (i+1))
                        row = list(row_str.split(','))
                        player_grid[i] = row

                        #user prompt read str, convert it to integer
                        for j in range(9):
                            row[j] = int(row[j])
                        player_grid[i] = row
            
                    # Check if the player's solution is correct
                    validate = check_board_valid(player_grid)
                    if validate == False:
                        print("Your answer is wrong, try again please! \n")
                    else:
                        print("Congratulations, you've solved the puzzle! Bye now.")
                        run = False
                        break
                elif val == '2':
                    print("The answer is: ")
                    print_board(solution)
                    print("Bye!")

                    run = False
                    break
                else:
                    print("Invalid instruction. Try again! \n")
                    break
            
            break

if __name__ == "__main__":
    main()