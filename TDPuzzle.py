import pygame
import time
from CellClass import Cell
pygame.init()

cellsize = 100
grid = []
rows = 10
cols = 10

red = (255,0,0)
white = (255,255,255)

width = rows*cellsize
height = cols*cellsize
screen = pygame.display.set_mode([width, height])

game_started = True

for row in range(rows):
    for col in range(cols):
        rect_x = cellsize * col
        rect_y = cellsize * row
#         print(rect_x)

        pygame.draw.rect(screen, (255,255,255), [rect_x,rect_y,cellsize,cellsize], 5)

pygame.display.update()

for row in range(rows):
    grid.append([])
    for col in range(cols):
        cell = Cell(col,row,None)
        grid[row].append(cell)

while game_started:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            click_x = pygame.mouse.get_pos()[0]
            click_y = pygame.mouse.get_pos()[1]
#             print(pygame.mouse.get_pos())
#             print(click_x)
            col_clicked = click_x // cellsize
            row_clicked = click_y // cellsize
            print(f"row: {row_clicked} col: {col_clicked}")
            grid[row_clicked][col_clicked].cell_type = "Block"
            #print(grid)
            for col in grid:
                for cell in col:
                    cell.cell_colour(cellsize, screen)
#             pygame.draw.rect(screen, white, [col_clicked*cellsize,row_clicked*cellsize,cellsize,cellsize])
#             pygame.display.update()
        
        else:
            pass
    
        
pygame.quit()