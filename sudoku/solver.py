# Big thanks to Kylie Ying's video: https://www.youtube.com/watch?v=tvP_FZ-D9Ng&ab_channel=KylieYing
# Backtracking: https://jeffe.cs.illinois.edu/teaching/algorithms/book/02-backtracking.pdf


from typing import Tuple
from pprint import pprint

def find_next_empty(puzzle) -> Tuple:
    # Find the next empty grid (row, col) on the puzzle that is not filled yet ---> representing with -1
    # Return row, col tuple or (None, None)   if there is none (meaning we have filled all the grid yay)

    # NOTE: indexing 0-8
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == -1:
                return row, col 

    # If all grids are filled
    return None, None

def is_valid(puzzle, guess, row, col) -> bool:
    "Important helper function that will check if the guess at that position in the puzzle is a valid guess"
    # returns True or False

    # for a guess to be valid, then we will need to follow the sudoku rules
    # ------
    # Number must not be repeated in the row, column, or the 3x3 square that it appears in

    # 1. CHECK WITH VALUES OF THAT CORRESPONDING ROW
    row_vals = puzzle[row]
    if guess in row_vals:
        return False # if repeated, then guess is invalid
    
    # 2. CHECK WITH VALUES OF THAT CORRESPONDING COLUMN
    col_vals = [puzzle[i][col] for i in range(9)] # list comprehension if you need a reminder

    if guess in col_vals:
        return False # same situation
    
    # 3. CHECK WITH THE 3X3 SQUARE, WHICH IS A CHARACTERISTIC OF THIS GAME
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start+3):
        for c in range(col_start, col_start+3):
            if puzzle[r][c] == guess:
                return False
            
    # if we have gone through three tests for validity and all passed
    return True

def solve_sudoku(puzzle) -> bool:
    # solve sudoku using backtracking

    # step 1: choose somewhere on the puzzle to make a guess
    row, col = find_next_empty(puzzle)

    # step 1a: if there is nowhere left, then we're done becasue we only allowed valid inputs
    if row is None:
        return True 
    
    # step 2: if there is a place to put a number, then make a guess between 1 and 9 as the input trial
    for guess in range(1, 10): # 1, 2, ... , 9
        # if this is a valid guess
        if is_valid(puzzle, guess, row, col):
            
            # step 3a: if this is a valid guess, then place it at that spot on the puzzle
            puzzle[row][col] = guess
            
            # step 4: recursively call `solve_sudoku()`
            if solve_sudoku(puzzle):
                return True
            
        # step 5: if not valid or if nothing gets returned True, we would need to **backtrack** to try a new number
        puzzle[row][col] = -1

    # step 6: if none of the numbers that have been tested works :< , then this puzzle is unsolvable!!
    return False # that's where the backtrack comes in handy so we can reset the initial choice


if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solve_sudoku(example_board))
    pprint(example_board)