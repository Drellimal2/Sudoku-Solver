"""
    Created By: Dane Miller
    Date: 29/05/2017
    Language: Python 3
"""

NULL = 0


def print_board(board):
    for row in board:
        res = []
        for col in row:
            if type(col) == type(3):
                res.append(str(col))
            else:
                res.append("-")
        print(" ".join(res))

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
        return board
    row_set = get_row_vals(row, board)
    col_set = get_col_vals(col, board)
    square_set = get_square_vals(row, col, board)

    board[row][col] -= row_set
    board[row][col] -= col_set
    board[row][col] -= square_set
    if len(board[row][col]) == 1:
        board[row][col] = board[row][col].pop()
    return board

if __name__  == "__main__":
    board, unsolved = get_board()
    print_board(board)
    for _ in range(20):
        for pos in unsolved:
            fill(pos[0], pos[1], board)
    print("  +=========+  ")
    print_board(board)




