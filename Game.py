from settings import *

class Game():
    def __init__(self) -> None:
        #一般設定
        self.surface = pygame.Surface((Game_Width,Game_Height))
        self.display_surface = pygame.display.get_surface()
        self.rect = self.surface.get_rect()

    def draw_grid(self):
        for col in range(1,Columns):
            x = col*Cell_Size
            pygame.draw.line(self.surface,Line_Color,(x,0),(x,self.surface.get_height()),1)
        for row in range(1,Rows):
            y= row*Cell_Size
            pygame.draw.line(self.surface,Line_Color,(0,y),(self.surface.get_width(),y),1)
        
    def run(self):
        self.draw_grid()
        pygame.draw.rect(self.surface,Line_Color,self.rect,2)
        self.display_surface.blit(self.surface,(Padding,Padding))