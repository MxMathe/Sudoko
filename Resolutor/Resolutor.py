def is_valid(board, row, col, num):
    # Verifica linha e coluna
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Verifica bloco 3x3
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def print_board(board):
    for i in range(9):
        print(" ".join(str(num) if num != 0 else '.' for num in board[i]))

# Colocar os numeros na grade
board = [
    [0, 0, 9, 0, 8, 6, 2, 0, 0],
    [0, 3, 0, 0, 7, 0, 0, 9, 6],
    [0, 6, 0, 0, 1, 0, 0, 0, 5],
    [5, 0, 3, 0, 0, 0, 0, 8, 0],
    [0, 9, 0, 1, 2, 5, 0, 6, 0],
    [0, 4, 0, 0, 0, 0, 1, 0, 7],
    [7, 0, 0, 0, 3, 0, 0, 1, 0],
    [9, 8, 0, 0, 4, 0, 0, 2, 0],
    [0, 0, 6, 8, 5, 0, 4, 0, 0],
]

print("Original:")
print_board(board)

if solve(board):
    print("\nResolvido:")
    print_board(board)
else:
    print("Essa grade não tem solução válida.")
