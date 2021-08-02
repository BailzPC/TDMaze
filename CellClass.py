import pygame

class Cell:
    def __init__(self,x,y,cell_type):
        self.dist = None
        self.y = y
        self.x = x
        self.cell_type = None
        # wall, watever
        
    def calcpath(self,dist):
        if not self.dist:
            self.dist = dist+1
        elif self.dist > (dist+1):
            self.dist = dist+1
    
    def set_cell(self, celltype):
        self.cell_type = celltype
        print(celltype)
    
    def cell_colour(self, cellsize, screen):
        self.cellsize = cellsize
        if self.cell_type == None:
            pass
        elif self.cell_type == "Block":
            pygame.draw.rect(screen, (255,255,255), [self.x*self.cellsize,self.y*self.cellsize,self.cellsize,self.cellsize])
            pygame.display.update()
        else:
            pass
    
    def __repr__(self):
        return str(self.cell_type)