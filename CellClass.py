import pygame
from fractions import Fraction
class Cell:
    def __init__(self,x,y,cell_type,button_reached,enemies_cell):
        self.dist = None
        self.y = y
        self.x = x
        self.cell_type = "None"
        self.button_reached = None
        self.enemies_cell = 0
        self.colour = (0, 100, 0)
        
#     Basic pathfinding calculation, scanning from the 'button' outwards, allows path to be recalculates with calc_path
#     anything but 'none', 'enemy' and 'button' will act as a wall to the pathfinding
    def calc_path(self, dist, grid):
        if self.cell_type != "Button" and self.dist != None and self.dist <= (dist + 1):
            return
        
        if self.dist == None or dist < self.dist:
            self.dist = dist+1

        for xoff, yoff in ((-1,0), (0,-1), (1,0), (0,1)):
            try:
                if self.y+yoff < 0 or self.x+xoff < 0:
                    continue
                neighbour = grid[self.y+yoff][self.x+xoff]
                if neighbour.cell_type in ["None", "Enemy", "Button"]:
                    neighbour.calc_path(self.dist, grid)
            except:
                pass
            
#     Pathfinding to make the enemy move and scan around it for the shortest path calculated in calc_path
#     also looks if the button has been reached by an enemy
    
    def enemy_move(self, grid):
        min_dist = self.dist
        neigh = None
        enemy_neighbour = None
    
        for xoff, yoff in ((-1,0), (0,-1), (1,0), (0,1)):
            try:
                if self.y+yoff < 0 or self.x+xoff < 0:
                    continue
                enemy_neighbour = grid[self.y+yoff][self.x+xoff]
            except:
                pass
            if enemy_neighbour.dist != None:
                if enemy_neighbour.dist < min_dist:
                    min_dist = enemy_neighbour.dist
                    neigh = enemy_neighbour
                    if neigh.cell_type == "Button":
                        neigh.button_reached = True
        neigh.enemies_cell += 1
        neigh.set_cell("Enemy")
        self.enemies_cell -= 1
        if self.enemies_cell <= 0:
            self.set_cell("None")

#     set cell function, allows easy changing from one type of cell to another using set_cell(type)
#     also updates the colour to be redrawn with cell_colour
    def set_cell(self, cell_type):
        self.cell_type = cell_type
        if cell_type == "Button":
            self.colour = (161,113,136)
        elif cell_type == "None":
            self.colour = (0,100,0)
            self.enemies_cell = 0
        elif cell_type == "Block":
            self.colour = (120,120,120)
        elif cell_type == "Enemy":
            self.colour = (255,0,0)
        elif cell_type == "Void":
            self.colour = (50,50,200)
    
#     cell colour function, updates the colour of the specific cell, usually run in a for loop for all cells
    def cell_colour(self, cellsize, screen, font):
        self.cellsize = cellsize
        pygame.draw.rect(screen, self.colour, [self.x*self.cellsize+cellsize/(100/3),self.y*self.cellsize+cellsize/(100/3),
                                               self.cellsize-cellsize/(100/6),self.cellsize-cellsize/(100/6)])
        
#         draws pathfinding number on each cell
# 
#         if self.cell_type not in ["Block", "Void", "Button"]:
#             screen.blit(font.render(str(self.dist), True, (0, 0, 0)), (self.x*cellsize+6, self.y*cellsize+32))
        