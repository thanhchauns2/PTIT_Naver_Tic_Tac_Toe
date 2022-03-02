import pygame
from positions import *

def analyze(board, next_player, x = 0, y = 0): # phân tích bàn cờ nếu như thêm vào vị trí (x, y)
    # board: mảng 2 chiều thể hiện trạng thái của bàn cờ
    # x, y: tọa độ của nước đi mới
    # return: "điểm" của bàn cờ, dương khi có vẻ sẽ thắng, âm khi ngược lại
    if board[x][y] != 0:
        return -1e10 # vị trí [x][y] không trống, không thể điền vào đây
    board[x][y] = next_player
    if enemy_five_in_a_row(board, next_player):
        return -1e10 # đã thua
    if five_in_a_row(board, next_player, x, y):
        return 1e10 # đã thắng
    points =  four_in_a_row(board, next_player, x, y) > 0 # check các trường hợp 4 quân thẳng hàng
    points = max(points, three_in_a_row(board, next_player, x, y)) # check các trường hợp 3 quân thẳng hàng
    points = max(points, two_in_a_row(board, next_player, x, y)) # check các trường hợp 2 quân thẳng hàng

    points_negative = enemy_four_in_a_row(board, -next_player) > 0 # check các trường hợp 4 quân địch thẳng hàng
    points_negative = min(points_negative, enemy_three_in_a_row(board, -next_player, x, y)) # check các trường hợp 3 quân địch thẳng hàng
    points_negative = min(points_negative, enemy_two_in_a_row(board, -next_player, x, y)) # check các trường hợp 2 quân địch thẳng hàng

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
            board = my_board
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
async def computer_reply(screen, board):
    # tìm nước đi của máy
    # board: mảng 2 chiều thể hiện trạng thái của bàn cờ
    # return: screen mới cùng board mới
    pass