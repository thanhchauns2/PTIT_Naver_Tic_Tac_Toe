import pygame
from config import *

def drawX(screen , x = 0, y = 0):
    points = ((x * square_size + from_border, y * square_size + from_border), 
             ((x + 1) * square_size - from_border, (y + 1) * square_size - from_border), 
             ((x + 1) * square_size - from_border, y * square_size + from_border), 
             (x * square_size + from_border, (y + 1) * square_size - from_border))
    pygame.draw.line(screen, X_color, (points[0][0], points[0][1]), (points[1][0], points[1][1]), tic_tac_thickness)
    pygame.draw.line(screen, X_color, (points[2][0], points[2][1]), (points[3][0], points[3][1]), tic_tac_thickness)

def drawY(screen, x = 0, y = 0):
    pygame.draw.circle(screen, O_color, ((x + 0.5) * square_size, (y + 0.5) * square_size), square_size // 3, tic_tac_thickness)

def draw_screen():
    screen = pygame.display.set_mode(screen_size)
    screen.fill(screen_color)
    i = 0
    while i < 1000:
        pygame.draw.line(screen, (0,0,0), (i, 0), (i, 1000), border_thickness)
        pygame.draw.line(screen, (0,0,0), (0, i), (1000, i), border_thickness)
        i += 40
    return screen

def new_board():
    board = [[0 for x in range(screen_size[0] // square_size)] for y in range(screen_size[1] // square_size)]
    return board

def check_if_end_game(board):
    pass