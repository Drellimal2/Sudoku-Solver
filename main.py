"""
    Created By: Dane Miller
    Date: 29/05/2017
    Language: Python 3
"""

NULL = 0
SIZE = 9

def print_board(board):
    for row in board:
        res = []
        for col in row:
            if type(col) == type(3):
                res.append(str(col))
            else:
                res.append("-")
        print(" ".join(res))
def dirty_print(board):
    for row in board:
        print(" ".join(map(str, row)))


def get_board(size = 9):
    board = []
    unsolved = set([])
    for _ in range(size):
        row = ''
        while True:
            row = input().strip()
            if len(row) == size:
                break
        row = list(map(int,row))
        for c in enumerate(row):
            if c[1] == NULL:
                unsolved.add((_, c[0]))
                row[c[0]] = set(list(range(1, 10)))           
                
        board.append(row)
    return board, unsolved

def get_row_vals(row, board):
    return set([x for x in board[row] if type(x) == type(3)])

def get_col_vals(col, board):
    return set([x[col] for x in board if type(x[col]) == type(3)])

def get_square_vals(row, col, board):
    square_row_start = (row//3) * 3
    square_row_end = (row//3 + 1) * 3
    square_col_start = (col//3) * 3
    square_col_end = (col//3 + 1) * 3
    square_set = set([board[x][y] for x in range(square_row_start, square_row_end)  for y in range(square_col_start, square_col_end) if type(board[x][y]) == type(3)])
    return square_set 

def fill(row, col, board):
    if type(board[row][col]) == type(3):
        return True
    row_set = get_row_vals(row, board)
    col_set = get_col_vals(col, board)
    square_set = get_square_vals(row, col, board)

    board[row][col] -= row_set
    board[row][col] -= col_set
    board[row][col] -= square_set
    if len(board[row][col]) == 1:
        board[row][col] = board[row][col].pop()
        return True
    return False

def fill_row(row, board):
    vals = []
    for i in board[row]:
        if type(i) != type(3):
            vals += list(i)
    for (i, x) in enumerate(board[row]):
        if type(x) != type(3): 
            for y in x:
                if vals.count(y) == 1:
                    board[row][i] = y
                    fix_all(row, i, board, y)
    return board


def fill_col(col, board):
    vals = []
    for i in board:
        if type(i[col]) != type(3):
            vals += list(i[col])
    for (i, x) in enumerate(board):
        if type(x[col]) != type(3):
            for y in x[col]:
                if vals.count(y) == 1:
                    board[i][col] = y
    return board

def fill_square(num, board):
    row_start = num//3 * 3
    row_end = row_start + 3
    col_start = (num % 3) * 3
    col_end = col_start + 3
    vals = []
    for row in range(row_start, row_end):
        for col in range(col_start, col_end):
            if type(board[row][col]) != type(3):
                vals += list(board[row][col])
    for row in range(row_start, row_end):
        for col in range(col_start, col_end):
            if type(board[row][col]) != type(3):
                for x in board[row][col]:
                    if vals.count(x) == 1:
                        board[row][col] = x
                        fix_all(row, col, board, x)
    
    return board

def fix_row(row, board, val):
    for (i, x) in enumerate(board[row]):
        if type(x) != type(3):
            board[row][i] -= set([val])
    return board

def fix_col(col, board, val):
    for (i, row) in enumerate(board):
        if type(row[col]) != type(3):
            board[i][col] -= set([val])
    return board

def fix_all(row, col, board, val):
    fix_row(row, board, val)
    fix_col(col, board, val)
    sqr = get_square_num(row, col)
    fix_square_num(sqr, board, val)


def get_square_num(row, col):
    return (row//3) * 3 + col//3

"""
    Square Nums
    0 1 2
    3 4 5
    6 7 8
"""
def fix_square_num(num, board, val):
    row_start = num//3 * 3
    row_end = row_start + 3
    col_start = (num % 3) * 3
    col_end = col_start + 3

    for row in range(row_start, row_end):
        for col in range(col_start, col_end):
            if type(board[row][col]) != type(3):
                board[row][col] -= set([val])
    return board
            


if __name__  == "__main__":
    board, unsolved = get_board()
    print_board(board)
    for _ in range(5):
        solved = set([])
        for pos in unsolved:
            if fill(pos[0], pos[1], board):
                solved.add(pos)
                fix_all(pos[0], pos[1], board, board[pos[0]][pos[1]])
        unsolved -= solved
        for i in range(SIZE):
            
            fill_row(i, board)

            fill_col(i, board)

            fill_square(i, board)

    print("  +=========+  ")
    print_board(board)




