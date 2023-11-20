from settings import *
from random import choice

class Game():
    def __init__(self) -> None:
        #一般設定
        self.surface = pygame.Surface((Game_Width,Game_Height))
        self.display_surface = pygame.display.get_surface()
        self.rect = self.surface.get_rect()
        self.sprites = pygame.sprite.Group()

        #lines
        self.line_surface = self.surface.copy()
        self.line_surface.fill((0,255,0))
        self.line_surface.set_colorkey((0,255,0))
        self.line_surface.set_alpha(120)

        #tetromino
        self.tetromino = Tetromino(choice(list(Tetorminos.keys())),self.sprites)

    def draw_grid(self):
        for col in range(1,Columns):
            x = col*Cell_Size
            pygame.draw.line(self.line_surface,Line_Color,(x,0),(x,self.surface.get_height()),1)
        for row in range(1,Rows):
            y= row*Cell_Size
            pygame.draw.line(self.line_surface,Line_Color,(0,y),(self.surface.get_width(),y),1)
        self.surface.blit(self.line_surface,(0,0))
        
    def run(self):
        self.surface.fill(Gray)
        self.sprites.draw(self.surface)
        self.draw_grid()
        pygame.draw.rect(self.surface,Line_Color,self.rect,2,2)
        self.display_surface.blit(self.surface,(Padding,Padding))

class Tetromino():
    def __init__(self,shape,group):
        #setup
        self.block_positions = Tetorminos[shape]["Shape"]
        self.color = Tetorminos[shape]["Color"]

        #creat blocks
        self.blocks = [Block(group,pos,self.color) for pos in self.block_positions]


class Block(pygame.sprite.Sprite):
    def __init__(self,group,pos,color):
        #general
        super().__init__(group)
        self.image = pygame.Surface((Cell_Size,Cell_Size))
        self.image.fill(color)

        #position
        self.pos = pygame.Vector2(pos) + Block_Offset
        x = self.pos.x * Cell_Size
        y = self.pos.y * Cell_Size
        self.rect = self.image.get_rect(topleft = (x,y))