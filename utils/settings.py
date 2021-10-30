import pygame
pygame.init()
pygame.font.init()


WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,255,0)
GREEN = (0,0,255)
COLOR_1 = (56, 65, 123)
COLOR_2 = (80, 92, 174)
COLOR_3 = (116, 243, 253)
COLOR_4 =  (93,67,54)
COLOR_5 = (188,214,188)
COLOR_6 = (248,228,204)

FPS = 200

WIDTH, HEIGHT = 600,700

ROWS = COLS = 50

TOOLBAR_HEIGHT = HEIGHT - WIDTH

PIXEL_SIZE = WIDTH // ROWS

BG_COLOR = WHITE

DRAW_GRID_LIENES = False

def get_font(size):
    return pygame.font.SysFont("comicsans", size)