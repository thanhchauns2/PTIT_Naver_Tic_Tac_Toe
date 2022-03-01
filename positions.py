from config import *

def not_valid(board, x):
    board_size = len(board)
    if x < 0 or x >= board_size:
        return True
    return False

def five_in_a_row(board, next_player, x, y):
    # dọc
    for i in range(x - 2, x + 3):
        if i < 0 or i >= len(board):
            break
        if board[i][y] == -next_player:
            break
        if i == x + 2:
            return True
    # ngang
    for i in range(y - 2, y + 3):
        if i < 0 or i >= len(board):
            break
        if board[x][i] == -next_player:
            break
        if i == y + 2:
            return True
    # chéo xuôi
    for i in range(-2, 3):
        if x + i < 0 or x + i >= len(board) or y + i < 0 or y + i >= len(board):
            break
        if board[i][y] == -next_player:
            break
        if i == 2:
            return True
    # chéo ngược
    for i in range(-2, 3):
        if x - i < 0 or x - i >= len(board) or y - i < 0 or y - i >= len(board):
            break
        if board[i][y] == -next_player:
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

def four_in_a_row(board, next_player, x, y):
    (up, down, left, right) = (0, 0, 0, 0)
    (up_left, down_left, up_right, down_right) = (0, 0, 0, 0)
    while x - up > 0 and board[x - up][y] == next_player:
        up += 1
    while x + down < len(board) and board[x + down][y] == next_player:
        down += 1
    while y - left > 0 and board[x][y - left] == next_player:
        left += 1
    while y + right < len(board) and board[x][y + right] == next_player:
        right += 1
    while x - up > 0 and y - left > 0 and board[x - up][y - left] == next_player:
        up_left += 1
    while x + down < len(board) and y - left > 0 and board[x + down][y - left] == next_player:
        down_left += 1
    while x - up > 0 and y + right < len(board) and board[x - up][y + right] == next_player:
        up_right += 1
    while x + down < len(board) and y + right < len(board) and board[x + down][y + right] == next_player:
        down_right += 1
    points = 0
    if up + down >= 3:
        if not_valid(board, x - up - 1) and not_valid(board, x + down + 1):
            pass
        elif not_valid(board, x - up - 1) or not_valid(board, x + down + 1):
            points += connect_four_has_obstacles
        else:
            points += connect_four
    if left + right >= 3:
        if not_valid(board, y - left - 1) and not_valid(board, y + right + 1):
            pass
        elif not_valid(board, y - left - 1) or not_valid(board, y + right + 1):
            points += connect_four_has_obstacles
        else:
            points += connect_four
    if up_left + down_right >= 3:
        if not_valid(board, x - up_left - 1) and not_valid(board, x + down_right + 1):
            pass
        elif not_valid(board, x - up_left - 1) or not_valid(board, x + down_right + 1):
            points += connect_four_has_obstacles
        else:
            points += connect_four
    if up_right + down_left >= 3:
        if not_valid(board, x - up_right - 1) and not_valid(board, x + down_left + 1):
            pass
        elif not_valid(board, x - up_right - 1) or not_valid(board, x + down_left + 1):
            points += connect_four_has_obstacles
        else:
            points += connect_four
    
    if points != 0 and points != connect_four_has_obstacles and points != connect_four:
        return connect_multiple_four
    elif points == connect_four:
        return connect_four
    elif points == connect_four_has_obstacles:
        return connect_four_has_obstacles
    return 0

def enemy_four_in_a_row(board, next_player):
    board_size = len(board)
    points = 0
    for i in range(board_size):
        for j in range(board_size):
            if board[i][j] != next_player:
                points = max(points, four_in_a_row(board, next_player, i, j))
    return -points

def three_in_a_row(board, next_player, x, y):
    (up, down, left, right) = (0, 0, 0, 0)
    (up_left, down_left, up_right, down_right) = (0, 0, 0, 0)
    while x - up > 0 and board[x - up][y] == next_player:
        up += 1
    while x + down < len(board) and board[x + down][y] == next_player:
        down += 1
    while y - left > 0 and board[x][y - left] == next_player:
        left += 1
    while y + right < len(board) and board[x][y + right] == next_player:
        right += 1
    while x - up > 0 and y - left > 0 and board[x - up][y - left] == next_player:
        up_left += 1
    while x + down < len(board) and y - left > 0 and board[x + down][y - left] == next_player:
        down_left += 1
    while x - up > 0 and y + right < len(board) and board[x - up][y + right] == next_player:
        up_right += 1
    while x + down < len(board) and y + right < len(board) and board[x + down][y + right] == next_player:
        down_right += 1

    points = 0

    if up + down >= 2:
        if not_valid(board, x - up - 1) and not_valid(board, x + down + 1):
            pass
        elif not_valid(board, x - up - 1) or not_valid(board, x + down + 1):
            points += connect_three_has_obstacles
        else:
            points += connect_three

    if left + right >= 2:
        if not_valid(board, y - left - 1) and not_valid(board, y + right + 1):
            pass
        elif not_valid(board, y - left - 1) or not_valid(board, y + right + 1):
            points += connect_three_has_obstacles
        else:
            points += connect_three

    if up_left + down_right >= 2:
        if not_valid(board, x - up_left - 1) and not_valid(board, x + down_right + 1):
            pass
        elif not_valid(board, x - up_left - 1) or not_valid(board, x + down_right + 1):
            points += connect_three_has_obstacles
        else:
            points += connect_three

    if up_right + down_left >= 2:
        if not_valid(board, x - up_right - 1) and not_valid(board, x + down_left + 1):
            pass
        elif not_valid(board, x - up_right - 1) or not_valid(board, x + down_left + 1):
            points += connect_three_has_obstacles
        else:
            points += connect_three

    if points != 0 and points != connect_three_has_obstacles and points != connect_three:
        return connect_multiple_three
    elif points == connect_three:
        return connect_three
    elif points == connect_three_has_obstacles:
        return connect_three_has_obstacles
    return 0

def enemy_three_in_a_row(board, next_player):
    board_size = len(board)
    points = 0
    for i in range(board_size):
        for j in range(board_size):
            if board[i][j] != next_player:
                points = max(points, three_in_a_row(board, next_player, i, j))
    return -points

def two_in_a_row(board, next_player, x, y):
    (up, down, left, right) = (0, 0, 0, 0)
    (up_left, down_left, up_right, down_right) = (0, 0, 0, 0)
    while x - up > 0 and board[x - up][y] == next_player:
        up += 1
    while x + down < len(board) and board[x + down][y] == next_player:
        down += 1
    while y - left > 0 and board[x][y - left] == next_player:
        left += 1
    while y + right < len(board) and board[x][y + right] == next_player:
        right += 1
    while x - up > 0 and y - left > 0 and board[x - up][y - left] == next_player:
        up_left += 1
    while x + down < len(board) and y - left > 0 and board[x + down][y - left] == next_player:
        down_left += 1
    while x - up > 0 and y + right < len(board) and board[x - up][y + right] == next_player:
        up_right += 1
    while x + down < len(board) and y + right < len(board) and board[x + down][y + right] == next_player:
        down_right += 1

    points = 0
    if up + down >= 1:
        if not_valid(board, x - up - 1) and not_valid(board, x + down + 1):
            pass
        elif not_valid(board, x - up - 1) or not_valid(board, x + down + 1):
            points += connect_two_has_obstacles
        else:
            points += connect_two

    if left + right >= 1:
        if not_valid(board, y - left - 1) and not_valid(board, y + right + 1):
            pass
        elif not_valid(board, y - left - 1) or not_valid(board, y + right + 1):
            points += connect_two_has_obstacles
        else:
            points += connect_two
    
    if up_left + down_right >= 1:
        if not_valid(board, x - up_left - 1) and not_valid(board, x + down_right + 1):
            pass
        elif not_valid(board, x - up_left - 1) or not_valid(board, x + down_right + 1):
            points += connect_two_has_obstacles
        else:
            points += connect_two

    if up_right + down_left >= 1:
        if not_valid(board, x - up_right - 1) and not_valid(board, x + down_left + 1):
            pass
        elif not_valid(board, x - up_right - 1) or not_valid(board, x + down_left + 1):
            points += connect_two_has_obstacles
        else:
            points += connect_two
    
    if points != 0 and points != connect_two_has_obstacles and points != connect_two:
        return connect_multiple_two
    elif points == connect_two:
        return connect_two
    elif points == connect_two_has_obstacles:
        return connect_two_has_obstacles
    return 0

def enemy_two_in_a_row(board, next_player):
    board_size = len(board)
    points = 0
    for i in range(board_size):
        for j in range(board_size):
            if board[i][j] != next_player:
                points = max(points, two_in_a_row(board, next_player, i, j))
    return -points