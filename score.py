from settings import *

class Score:
    def __init__(self) -> None:
        self.Sureface = pygame.Surface((SideBar_Width,Game_Height * Socre_Height_Farction - Padding))
        self.Display_Sureface = pygame.display.get_surface()