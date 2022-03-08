import pygame
import sys
import asyncio
import time
from config import *
from computer_player import *
from draw import *
from tkinter import *

def window_game():
    pygame.init()

    screen = draw_screen()

    board = new_board()

    pygame.display.update()

    game_over = False

    while True:
        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONUP:
                if game_over:
                    pygame.quit()
                pos = pygame.mouse.get_pos()
                x = pos[0] // 40
                y = pos[1] // 40
                if board[x][y] != 0:
                    continue
                drawX(screen, x, y)
                board[x][y] = 1
                if check_if_end_game(screen, board):
                    pygame.display.update()
                    ev1 = pygame.event.get()
                    game_over = True
                    continue

                pygame.display.update()
                computer_reply(screen, board)
                if check_if_end_game(screen, board):
                    pygame.display.update()
                    ev = pygame.event.get()
                    game_over = True
                    continue

                pygame.display.update()

root = Tk()
root.title("Caro")
root.geometry("400x400")

def myClick():
	lb = Label(root, text = "Hello world!")
	lb.grid(row = 3, column = 0)

Label(root, text = 'Tên đăng nhập').grid(row = 0, column = 0)
Label(root, text = 'Mật khẩu').grid(row = 1, column = 0)

username = Entry(root, width = 15)
username.grid(row = 0, column = 1)

password = Entry(root, width = 15)
password.grid(row = 1, column = 1)

button = Button(root, text = "Đăng nhập", command = window_game).grid(row = 2, column = 0)
notifi = Text(root, height = 1, width = 15)
notifi.grid(row = 2, column = 1)
root.mainloop()