def five_in_a_row(board, next_player, x, y):
    # dọc
    for i in range(x - 2, x + 3):
        if i < 0 or i >= len(board):
            break
        if board[i][y] == next_player:
            break
        if i == x + 2:
            return True
    # ngang
    for i in range(y - 2, y + 3):
        if i < 0 or i >= len(board):
            break
        if board[x][i] == next_player:
            break
        if i == y + 2:
            return True
    # chéo xuôi
    for i in range(-2, 3):
        if x + i < 0 or x + i >= len(board) or y + i < 0 or y + i >= len(board):
            break
        if board[i][y] == next_player:
            break
        if i == 2:
            return True
    # chéo ngược
    for i in range(-2, 3):
        if x - i < 0 or x - i >= len(board) or y - i < 0 or y - i >= len(board):
            break
        if board[i][y] == next_player:
            break
        if i == 2:
            return True
    return False

def enemy_five_in_a_row(board, next_player):
    board_size = len(board)
    for i in range(board_size):
        for j in range(board_size):
            if board[i][j] != next_player:
                if five_in_a_row(board, next_player, i, j):
                    return True