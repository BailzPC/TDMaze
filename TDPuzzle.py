import pygame
from CellClass import Cell
pygame.init()

cellsize = 100
grid = []
rows = 15
cols = 20
block_selected = "Block"
cell_type_clicked = "None"
path_calculated = False
enemies = []

red = (255,0,0)
white = (255,255,255)

width = cols*cellsize
height = rows*cellsize
screen = pygame.display.set_mode([width, height])

game_started = True

for row in range(rows):
    for col in range(cols):
        rect_x = cellsize * col
        rect_y = cellsize * row

        pygame.draw.rect(screen, (255,255,255), [rect_x,rect_y,cellsize,cellsize], 5)

#append cells into grid

for row in range(rows):
    grid.append([])
    for col in range(cols):
        cell = Cell(col,row,"None",None)
        grid[row].append(cell)

#changes where button is, button is end goal and timer

button = grid[5][10]
button.set_cell("Button")
button.dist = 0
button_x = button.x
button_y = button.y

clock = pygame.time.Clock()
game_won = False
timer_started = False
game_speed = 1000

counter, text = 30, '30'.rjust(3)
font = pygame.font.SysFont('Consolas', 36)

while game_started:
    for event in pygame.event.get():
        
        #Timer logic, counts down every second
        if event.type == pygame.USEREVENT:
            counter -= 1
            text = str(counter).rjust(3) if counter > 0 else 'Win!'
            if counter < 1:
                game_won = True
                    
            for col in grid:
                for cell in col:
                    if cell.cell_type == "Enemy":
                        enemies.append(cell)
            
            if game_won != True:
                for enemy in enemies:
                    enemy.enemy_move(grid)
                
            for col in grid:
                for cell in col:
                    cell.cell_colour(cellsize, screen, font)
                    
        if event.type == pygame.QUIT:
            game_started = False
            
        if button.button_reached == True:
            game_started = False
        
        #Cycles through blocks to place using number keys
        
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
                
        #Recalculates all the pathfinding numbers
        
        #If in the planning phase, places block by setting
        #the tile you clicked on to block_selected, unless void or button cell
        
        elif event.type == pygame.MOUSEBUTTONDOWN and not timer_started:
            click_x = pygame.mouse.get_pos()[0]
            click_y = pygame.mouse.get_pos()[1]
            col_clicked = click_x // cellsize
            row_clicked = click_y // cellsize
            cell_type_clicked = grid[row_clicked][col_clicked].cell_type
            
            if cell_type_clicked == "Void":
                print("You cannot place there")
            
            elif cell_type_clicked == "Button":
                pygame.time.set_timer(pygame.USEREVENT, game_speed)
                if not timer_started:
                    timer_started = True
                    print("The game has begun!")
                    
            else:
                grid[row_clicked][col_clicked].set_cell(block_selected)
        
            for col in grid:
                for cell in col:
                    if cell.cell_type != "Button":
                        cell.dist = None
                        
            button.calc_path(button.dist, grid)
            path_calculated = True
            for col in grid:
                for cell in col:
                    cell.cell_colour(cellsize, screen, font)
        
        #Cycle through timer speeds clicking the button after game started
                
        elif event.type == pygame.MOUSEBUTTONDOWN and timer_started:
            click_x = pygame.mouse.get_pos()[0]
            click_y = pygame.mouse.get_pos()[1]
            col_clicked = click_x // cellsize
            row_clicked = click_y // cellsize
            
            cell_type_clicked = grid[row_clicked][col_clicked].cell_type
            
            if cell_type_clicked == "Button":
                if timer_started == True:
                    if game_speed == 1000:
                        game_speed = 500
                        print("2x")
                    elif game_speed == 500:
                        game_speed = 250
                        print("4x")
                    elif game_speed == 250:
                        game_speed = 1000
                        print("1x")
                    pygame.time.set_timer(pygame.USEREVENT, game_speed)
                    
                else:
                    print("Timer has been started!")
                
        else:
            pass
    
    #updates the screen every loop, cells colour themselves
    
    if not path_calculated:
        button.calc_path(button.dist, grid)
    for col in grid:
        for cell in col:
            cell.cell_colour(cellsize, screen, font)
    screen.blit(font.render(text, True, (0, 0, 0)), (button_x*cellsize+6, button_y*cellsize+32))
    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()