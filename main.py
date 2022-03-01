import pygame
import sys
import asyncio
import time
from config import *
from computer_player import *
from draw import *

pygame.init()

screen = draw_screen()

board = new_board()

pygame.display.update()

while True:
    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            x = pos[0] // 40
            y = pos[1] // 40
            drawX(screen, x, y)
            board[x][y] = 1
            pygame.display.update()
            asyncio.run_coroutine_threadsafe(computer_reply(screen, board), loop = asyncio.new_event_loop())
            check_if_end_game(board)
            # print(x, y)
    # next_turn = True