import pygame

class Cell:
    def __init__(self,x,y,cell_type):
        self.dist = None
        self.y = y
        self.x = x
        self.cell_type = None
        
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

        if self.cell_type == "None":
            pygame.draw.rect(screen, (0,100,0), [self.x*self.cellsize+3,self.y*self.cellsize+3,self.cellsize-6,self.cellsize-6])
            
        elif self.cell_type == "Block":
            pygame.draw.rect(screen, (120,120,120), [self.x*self.cellsize+3,self.y*self.cellsize+3,self.cellsize-6,self.cellsize-6])
            
        elif self.cell_type == "Enemy":
            pygame.draw.rect(screen, (255,0,0), [self.x*self.cellsize+3,self.y*self.cellsize+3,self.cellsize-6,self.cellsize-6])
        
        elif self.cell_type == "Void":
            pygame.draw.rect(screen, (50,50,200), [self.x*self.cellsize+3,self.y*self.cellsize+3,self.cellsize-6,self.cellsize-6])
            
        elif self.cell_type == "Button":
            pygame.draw.rect(screen, (161,113,136), [self.x*self.cellsize+3,self.y*self.cellsize+3,self.cellsize-6,self.cellsize-6])

            
        else:
            pass
    
    def __repr__(self):
        return str(self.cell_type)