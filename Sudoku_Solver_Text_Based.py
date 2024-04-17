# This text based Sudoku solver uses the Recursive Backtrack

board = [
    [0, 5, 0, 4, 0, 0, 3, 0, 1], 
    [0, 4, 0, 3, 0, 0, 6, 0, 5], 
    [0, 0, 1, 5, 6, 0, 4, 2, 9], 
    [2, 6, 3, 9, 5, 4, 8, 1, 7], 
    [9, 7, 5, 6, 0, 0, 2, 0, 3], 
    [1, 8, 4, 7, 3, 2, 5, 9, 6], 
    [4, 1, 0, 8, 0, 3, 7, 5, 2], 
    [3, 9, 0, 2, 7, 5, 1, 6, 4], 
    [5, 2, 7, 1, 4, 6, 9, 3, 8]
]

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

print_board(board)
solver(board)
print("-------------------------")
print_board(board)