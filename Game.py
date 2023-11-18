from settings import *

class Game():
    def __init__(self) -> None:
        #一般設定
        self.Surface = pygame.Surface((Game_Width,Game_Height))
        self.Display_Surface = pygame.display.get_surface()
    
    def run(self):
        self.Display_Surface.blit(self.Surface,(Padding,Padding))