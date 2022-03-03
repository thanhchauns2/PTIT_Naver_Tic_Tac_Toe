import pygame
from positions import *
from draw import *

def analyze(my_board, next_player, x = 0, y = 0): # phân tích bàn cờ nếu như thêm vào vị trí (x, y)
    # board: mảng 2 chiều thể hiện trạng thái của bàn cờ
    # x, y: tọa độ của nước đi mới
    # return: "điểm" của bàn cờ, dương khi có vẻ sẽ thắng, âm khi ngược lại
    board = my_board[:]
    if board[x][y] != 0:
        return -1e10 # vị trí [x][y] không trống, không thể điền vào đây
    board[x][y] = next_player
    if enemy_five_in_a_row(board, -next_player):
        board[x][y] = 0
        return -1e10 # đã thua
    if enemy_five_in_a_row(board, next_player):
        board[x][y] = 0
        return 1e10 # đã thắng
    points = enemy_four_in_a_row(board, next_player) # check các trường hợp 4 quân thẳng hàng
    points = max(points, enemy_three_in_a_row(board, next_player)) # check các trường hợp 3 quân thẳng hàng
    points = max(points, enemy_two_in_a_row(board, next_player)) # check các trường hợp 2 quân thẳng hàng

    points_negative = enemy_four_in_a_row(board, -next_player) # check các trường hợp 4 quân địch thẳng hàng
    points_negative = max(points_negative, enemy_three_in_a_row(board, -next_player)) # check các trường hợp 3 quân địch thẳng hàng
    points_negative = max(points_negative, enemy_two_in_a_row(board, -next_player)) # check các trường hợp 2 quân địch thẳng hàng

    for i in range(-1, 1):
        for j in range(-1, 1):
            if x + i < 0 or y + j < 0 or x + i >= len(board) or y + j >= len(board):
                continue
            if i == 0 and j == 0:
                continue
            if board[x + i][y + j] == 0:
                points += 1

    board[x][y] = 0

    return points - points_negative * 1.25
    

def analyze_current_move(my_board, next_player): # phần tôi làm
    # phân tích trạng thái hiện tại của bàn cờ
    # board: mảng 2 chiều thể hiện trạng thái của bàn cờ
    # next_player: 1 nếu là X, -1 nếu là O
    # độ sâu: 1 nước
    # return: một pair (x, y) đưa ra tọa độ tốt nhất
    board_size_x = len(my_board)
    board_size_y = len(my_board[0])
    x = 0
    y = 0
    points = -1e10
    for i in range(board_size_x):
        for j in range(board_size_y):
            board = my_board[:]
            curr_point = analyze(board, next_player, i, j)
            if (points < curr_point):
                x = i
                y = j
                points = curr_point
    return (x, y)

def deep_analyze(board): # phần mọi người làm
    # phân tích trạng thái bàn cờ
    # board: mảng 2 chiều thể hiện trạng thái của bàn cờ
    # độ sâu, v/v: mọi người dev thế nào thì viết như thế
    # return: "điểm" của trạng thái bàn cờ, dương khi tỉ lệ thắng cao và âm khi tỉ lệ thắng thấp
    pass

# screen: màn hình hiện đang chơi, board: mảng 2 chiều thể hiện trạng thái của bàn cờ
def computer_reply(screen, board):
    # tìm nước đi của máy
    # board: mảng 2 chiều thể hiện trạng thái của bàn cờ
    # return: screen mới cùng board mới
    x, y = analyze_current_move(board, -1)
    # x, y = 0, 0
    drawO(screen, x, y)
    board[x][y] = -1
    # for i in board:
    #     print(i)
    print(x, y) 
    # pass