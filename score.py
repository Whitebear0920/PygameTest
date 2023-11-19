from settings import *

class Score:
    def __init__(self) -> None:
        self.sureface = pygame.Surface((SideBar_Width,Game_Height * Score_Height_Fraction - Padding))
        self.rect = self.sureface.get_rect(bottomright = (Window_Width - Padding,Window_Height - Padding))
        self.display_sureface = pygame.display.get_surface()

    def run(self):
        self.display_sureface.blit(self.sureface,self.rect)
