# This text based Sudoku solver uses the Recursive Backtracking algorithm
from sudoku_api import fetch_sudoku_board

# get the board from the api file
board = fetch_sudoku_board()

def convert_board(str_board):
    for i in range(9):
        for j in range(9):
            if str_board[i][j] == '.':
                str_board[i][j] = 0
            else:
                str_board[i][j] = int(str_board[i][j])
                
            

def print_board(board):
    # this method is used to print the Sudoku board to the terminal in a presentable manner
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")
                
def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j) # gives us row, column of the empty spot
    return None

def is_Valid(board, num, pos):
    # First we check the respective row of the Sudoku
    for i in range(9):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
        
    # Next we check the respective column of the Sudoku
    for i in range(9):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
        
    # Finally we check the respective 3x3 box of the Sudoku
    box_row = pos[0] // 3
    box_col = pos[1] // 3
    for j in range(box_col * 3, box_col * 3 + 3):
        for i in range(box_row * 3, box_row * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False
            
    return True

def solver(board):
    empty_spot = find_empty(board)
    
    # First we check if there is an empty spot on the Sudoku board
    if not empty_spot:
        return True
    else:
        row, col = empty_spot
        
    for i in range(1, 10):
        if is_Valid(board, i, empty_spot):
            board[row][col] = i
            
            if solver(board):
                return True
            
            board[row][col] = 0
            
    return False

convert_board(board)
print_board(board)
solver(board)
print("-------------------------")
print_board(board)
