from utils import *

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Not Microsoft Paint")




def init_grid(rows,cols,color):
    grid = []
    
    for i in range(rows):
        grid.append([])
        for _ in range(cols):
            grid[i].append(color)
    return grid

def draw_grid(win,grid):
    for i, row in enumerate(grid):
        for j,pixel in enumerate(row):
            pygame.draw.rect(win,pixel,(j * PIXEL_SIZE, i * PIXEL_SIZE, PIXEL_SIZE ,PIXEL_SIZE))

    if DRAW_GRID_LIENES:
        for i in range(ROWS + 1):
            pygame.draw.line(win,BLACK,(0,i * PIXEL_SIZE),(WIDTH, i * PIXEL_SIZE))

        for i in range(COLS + 1):
            pygame.draw.line(win,BLACK,(i * PIXEL_SIZE,0),(i * PIXEL_SIZE,HEIGHT - TOOLBAR_HEIGHT))
            

def draw(win,grid,buttons):
    win.fill(BG_COLOR)
    draw_grid(win,grid)
    for Button in buttons:
        Button.draw(win)
    pygame.display.update()

def get_row_col_from_pos(pos):
    x,y = pos
    row = y // PIXEL_SIZE
    col = x // PIXEL_SIZE

    if row >= ROWS:
        raise IndexError

    return row, col

run = True
clock = pygame.time.Clock()
grid = init_grid(ROWS,COLS, BG_COLOR)
drawin_color = BLACK

button_y = HEIGHT - TOOLBAR_HEIGHT/2 - 40
buttons = [
    Button(10,button_y,20,20,BLACK),
    Button(40,button_y,20,20,RED),
    Button(70,button_y,20,20,GREEN),
    Button(100,button_y,20,20,BLUE),
    Button(10,button_y + 30,20,20,COLOR_1),
    Button(40,button_y + 30,20,20,COLOR_2),
    Button(70,button_y + 30,20,20,COLOR_3),
    Button(100,button_y + 30,20,20,COLOR_4),
    Button(10,button_y + 60,20,20,COLOR_5),
    Button(40,button_y + 60,20,20,COLOR_6),

    Button(540,button_y,50,50,WHITE,text="Erase",text_color=BLACK),
    Button(480,button_y,50,50,WHITE,text="Clear",text_color=BLACK),
]

while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            try:
                row,col = get_row_col_from_pos(pos)
                grid[row][col] = drawin_color
            except IndexError:
                for button in buttons:
                    if not button.clicked(pos):
                        continue
                    drawin_color = button.color
                    if button.text == "Clear":
                        grid = init_grid(ROWS,COLS, BG_COLOR)
                        drawin_color = BLACK

    
    draw(WIN,grid,buttons)

pygame.quit()