import pygame
import time
from CellClass import Cell
pygame.init()

cellsize = 100
grid = []
rows = 12
cols = 12
block_selected = "Block"
cell_type_clicked = "None"

red = (255,0,0)
white = (255,255,255)

width = cols*cellsize
height = rows*cellsize
screen = pygame.display.set_mode([width, height])
screen.fill((0,100,0))

game_started = True

for row in range(rows):
    for col in range(cols):
        rect_x = cellsize * col
        rect_y = cellsize * row
#         print(rect_x)

        pygame.draw.rect(screen, (255,255,255), [rect_x,rect_y,cellsize,cellsize], 5)



for row in range(rows):
    grid.append([])
    for col in range(cols):
        cell = Cell(col,row,None)
        grid[row].append(cell)

grid[0][cols-1].cell_type = "Button"
top_right = grid[0][cols-1].cell_type

while game_started:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            game_started = False
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                block_selected = "Block"
                print(f"Selected: {block_selected}")
            elif event.key == pygame.K_2:
                block_selected = "Enemy"
                print(f"Selected: {block_selected}")
            elif event.key == pygame.K_3:
                block_selected = "None"
                print(f"Selected: {block_selected}")
            
            elif event.key == pygame.K_0:
                block_selected = "Void"
                print(f"Selected: {block_selected}")
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_x = pygame.mouse.get_pos()[0]
            click_y = pygame.mouse.get_pos()[1]
#            print(pygame.mouse.get_pos())
#            print(click_x)
            col_clicked = click_x // cellsize
            row_clicked = click_y // cellsize
#            print(f"row: {row_clicked} col: {col_clicked}")
            
            cell_type_clicked = grid[row_clicked][col_clicked].cell_type
#            print(f"Clicked: {cell_type_clicked}")
            
            if cell_type_clicked == "Void":
                print("You cannot place there")
            
            elif cell_type_clicked == "Button":
                pass
                
            else:
                grid[row_clicked][col_clicked].cell_type = block_selected
                
            for col in grid:
                    for cell in col:
                        cell.cell_colour(cellsize, screen)
                    
        else:
            pass
        
        pygame.display.update()
pygame.quit()