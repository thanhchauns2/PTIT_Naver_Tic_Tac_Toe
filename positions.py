from config import *
dict = {
    'connect_multiple_four1' : connect_multiple_four1,
    'connect_four_has_obstacles1' : connect_four_has_obstacles1,
    'connect_four1' : connect_four1,
    'connect_multiple_three1' :  connect_multiple_three1,
    'connect_three_has_obstacles1' : connect_three_has_obstacles1,
    'connect_three1' : connect_three1,
    'connect_multiple_two1' : connect_multiple_two1,
    'connect_two_has_obstacles1' : connect_two_has_obstacles1,
    'connect_two1' : connect_two1,

    'connect_multiple_four2' : connect_multiple_four2,
    'connect_four_has_obstacles2' : connect_four_has_obstacles2,
    'connect_four2' : connect_four2,
    'connect_multiple_three2' :  connect_multiple_three2,
    'connect_three_has_obstacles2' : connect_three_has_obstacles2,
    'connect_three2' : connect_three2,
    'connect_multiple_two2' : connect_multiple_two2,
    'connect_two_has_obstacles2' : connect_two_has_obstacles2,
    'connect_two2' : connect_two2
}


def not_valid(board, x):
    nboard = len(board)
    if x < 0 or x >= nboard:
        return True
    return False
def five_in_a_row(board, next_player, x, y):
    # dọc
    for i in range(x - 2, x + 3):
        if i < 0 or i >= len(board):
            break
        if board[i][y] != next_player:
            break
        if i == x + 2:
            return True
    # ngang
    for i in range(y - 2, y + 3):
        if i < 0 or i >= len(board):
            break
        if board[x][i] != next_player:
            break
        if i == y + 2:
            return True
    # chéo xuôi
    for i in range(-2, 3):
        if x + i < 0 or x + i >= len(board) or y + i < 0 or y + i >= len(board):
            break
        if board[x + i][y + i] != next_player:
            break
        if i == 2:
            return True
    # chéo ngược
    for i in range(-2, 3):
        if x + i < 0 or x + i >= len(board) or y - i < 0 or y - i >= len(board):
            break
        if board[x + i][y - i] != next_player:
            break
        if i == 2:
            return True
    return False

def have_five(board, next_player, x, y):
    (up, down, left, right) = (0, 0, 0, 0)
    (up_left, down_left, up_right, down_right) = (0, 0, 0, 0)
    while x - up >= 0 and board[x - up][y] == next_player:
        up += 1
    while x + down < len(board) and board[x + down][y] == next_player:
        down += 1
    while y - left >= 0 and board[x][y - left] == next_player:
        left += 1
    while y + right < len(board) and board[x][y + right] == next_player:
        right += 1
    while x - up_left >= 0 and y - up_left >= 0 and board[x - up_left][y - up_left] == next_player:
        up_left += 1
    while x + down_right < len(board) and y + down_right < len(board) and board[x + down_right][
        y + down_right] == next_player:
        down_right += 1
    while x + down_left < len(board) and y - down_left >= 0 and board[x + down_left][y - down_left] == next_player:
        down_left += 1
    while x - up_right >= 0 and y + up_right < len(board) and board[x - up_right][y + up_right] == next_player:
        up_right += 1
    points = 0
    if up + down - 2 >= 4: return True
    if left + right - 2 >= 4: return True
    if down_left + up_right - 2 >= 4: return True
    if up_left + down_right - 2 >= 4: return True
    return False



def enemy_five_in_a_row(board, next_player):
    board_size = len(board)
    for i in range(board_size):
        for j in range(board_size):
            if board[i][j] == next_player:
                if five_in_a_row(board, next_player, i, j):
                    return True
    return False



def process(board : list, next_player : int, x : int, y : int, nums : str, amount : int, rank:str):
    (up, down, left, right) = (0, 0, 0, 0)
    (up_left, down_left, up_right, down_right) = (0, 0, 0, 0)
    while x - up >= 0 and board[x - up][y] == next_player:
        up += 1
    while x + down < len(board) and board[x + down][y] == next_player:
        down += 1
    while y - left >= 0 and board[x][y - left] == next_player:
        left += 1
    while y + right < len(board) and board[x][y + right] == next_player:
        right += 1
    while x - up_left >= 0 and y - up_left >= 0 and board[x - up_left][y - up_left] == next_player:
        up_left += 1
    while x + down_right < len(board) and y + down_right < len(board) and board[x + down_right][y + down_right] == next_player:
        down_right += 1
    while x + down_left < len(board) and y - down_left >= 0 and board[x + down_left][y - down_left] == next_player:
        down_left += 1
    while x - up_right >= 0 and y + up_right < len(board) and board[x - up_right][y + up_right] == next_player:
        up_right += 1
    points = 0
    if up + down - 2 >= amount - 1:
        if (not_valid(board, x - up) and not_valid(board, x + down)) or (not_valid(board, x - up) == False and board[x - up][y] == -next_player and
                                                                         not_valid(board, x + down) == False and board[x + down][y] == -next_player):
            pass
        elif not_valid(board, x - up) or not_valid(board, x + down) or board[x - up][y] == -next_player or board[x + down][y] == -next_player:
            points += dict[f'connect_{nums}_has_obstacles{rank}']
        else:
            points += dict[f'connect_{nums}{rank}']
    if left + right - 2 >= amount - 1:
        if not_valid(board, y - left) and not_valid(board, y + right) or (not_valid(board, y - left) == False and board[x][y - left] == -next_player and
                                                                          not_valid(board, y + right) == False and board[x][y + right] == -next_player):
            pass
        elif not_valid(board, y - left) or not_valid(board, y + right) or board[x][y - left] == -next_player or board[x][y + right] == -next_player:
            points += dict[f'connect_{nums}_has_obstacles{rank}']
        else:
            points += dict[f'connect_{nums}{rank}']
    if up_left + down_right - 2 >= amount - 1:
        if (not_valid(board, x - up_left) or not_valid(board, y - up_left)) and (not_valid(board, x + down_right) or not_valid(board, y + down_right))\
            or (not_valid(board, x - up_left) == False and not_valid(board, y - up_left) == False and board[x - up_left][y - up_left] == -next_player and
                not_valid(board, x + down_right) == False and not_valid(board, y + down_right) == False and board[x + down_right][y + down_right] == -next_player):
            pass
        elif not_valid(board, x - up_left) or not_valid(board, y - up_left) or not_valid(board, x + down_right) or not_valid(board, y + down_right) \
             or  board[x - up_left][y - up_left] == -next_player or board[x + down_right][y + down_right] == -next_player :
            points += dict[f'connect_{nums}_has_obstacles{rank}']
        else:
            points += dict[f'connect_{nums}{rank}']
    if up_right + down_left - 2 >= amount - 1:
        if (not_valid(board, x - up_right) or not_valid(board, y + up_right)) and (not_valid(board, x + down_left) or not_valid(board, y - down_left))\
            or (not_valid(board, x - up_right) ==  False and not_valid(board, y + up_right) == False and board[x - up_right][y + up_right] == -next_player
                and not_valid(board, x + down_left) == False and not_valid(board, y - down_left) == False and board[x + down_left][y - down_left] == -next_player):
            pass
        elif (not_valid(board, x - up_right) or not_valid(board, y + up_right)) or (not_valid(board, x + down_left) or not_valid(board, y - down_left))\
            or (board[x - up_right][y + up_right] == -next_player or board[x + down_left][y - down_left] == -next_player):
            points += dict[f'connect_{nums}_has_obstacles{rank}']
        else:
            points += dict[f'connect_{nums}{rank}']
    if points > dict[f'connect_{nums}{rank}']:
        return dict[f'connect_multiple_{nums}{rank}']
    elif points == dict[f'connect_{nums}{rank}']:
        # print("yes", points, ' ', nums, ' ', rank)
        return dict[f'connect_{nums}{rank}']
    elif points > dict[f'connect_{nums}_has_obstacles{rank}']:
        return dict[f'connect_{nums}_has_obstacles{rank}']
    return 0

def four_in_a_row(board, next_player, x, y, rank):
    return process(board, next_player, x, y, 'four', 4, rank)

def three_in_a_row(board, next_player, x, y, rank):
    return process(board, next_player, x, y, 'three', 3, rank)

def two_in_a_row(board, next_player, x, y, rank):
    return process(board, next_player, x, y, 'two', 2, rank)
