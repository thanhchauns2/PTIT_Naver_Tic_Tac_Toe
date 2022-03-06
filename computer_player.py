import pygame
from positions import *
from draw import *

def analyze(my_board, next_player, x, y): # phân tích bàn cờ nếu như thêm vào vị trí (x, y)
    board = my_board[:]
    point = 0
    board[x][y] = next_player
    pointAttack = 0
    pointAttack = max(pointAttack, four_in_a_row(board, next_player, x, y))
    pointAttack = max(pointAttack, three_in_a_row(board, next_player, x, y))
    pointAttack = max(pointAttack, two_in_a_row(board, next_player, x, y))
    board[x][y] = -next_player
    pointDefense = 0
    pointDefense = max(pointDefense, four_in_a_row(board, next_player * -1, x, y))
    pointDefense = max(pointDefense, three_in_a_row(board, next_player * -1, x, y))
    pointDefense = max(pointDefense, two_in_a_row(board, next_player * -1, x, y))
    board[x][y] = 0
    return max(pointAttack, pointDefense + 100)

def analyze_current_move(table, next_player): # phần tôi làm
    point , position_x, position_y = 0, 0, 0
    ntable = len(table)
    for x in range(ntable):
        for y in range(ntable):
            if table[x][y] == 0:
                cur_point = analyze(table, next_player, x, y)
                if point < cur_point:
                    point = cur_point
                    position_x = x
                    position_y = y
    return (position_x, position_y)

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
    position = analyze_current_move(board, -1)
    # x, y = 0, 0
    drawO(screen, position[0], position[1])
    board[position[0]][position[1]] = -1
    # for i in board:
    #     print(i)
    # pass