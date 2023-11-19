from settings import *

class Preview():
    def __init__(self) -> None:
        self.surface = pygame.Surface((SideBar_Width,Window_Height * Preview_Height_Fraction -Padding))
        self.rect = self.surface.get_rect(topright = (Window_Width - Padding,Padding))
        self.display_surface = pygame.display.get_surface()
    
    def run(self):
        self.display_surface.blit(self.surface,self.rect)