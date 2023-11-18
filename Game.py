from Settings import *

class Game():
    def __init__(self) -> None:
        self.Surface = pygame.surface((Game_Width,Game_Height))
        self.Display_Surface = pygame.display.get_surface()
    
    def run(self):
        self.Display_Surface.bilt(self.Surface,(0,0))