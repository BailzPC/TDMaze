import pygame
# pygame.font.init()
# myfont = pygame.font.SysFont('Comic Sans MS', 30)


class Cell:
    def __init__(self,x,y,cell_type):
        self.dist = None
        self.y = y
        self.x = x
        self.cell_type = None

    def calcpath(self, dist, grid):
        if self.cell_type != "Button" and self.dist != None and self.dist <= (dist + 1):
            return
        
        if self.dist == None or dist < self.dist:
            self.dist = dist+1

        for xoff, yoff in ((-1,0), (0,-1), (1,0), (0,1)):
            try:
                neighbour = grid[self.y+yoff][self.x+xoff]
                if neighbour.cell_type in [None, "Enemy", "Button"]:
                    neighbour.calcpath(self.dist, grid)
            except:
                pass
        
    def set_cell(self, celltype):
        self.cell_type = celltype
        print(celltype)
    
    def cell_colour(self, cellsize, screen):
        self.cellsize = cellsize

        if self.cell_type == "None":
            pygame.draw.rect(screen, (0,100,0), [self.x*self.cellsize+3,self.y*self.cellsize+3,self.cellsize-6,self.cellsize-6])
#             textsurface = myfont.render(str(self.dist), False, (0, 0, 0))
#             screen.blit(textsurface, (self.x*cellsize+6, self.y*cellsize+30))
            
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