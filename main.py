from settings import *
from sys import exit

#components
from game import Game


class Main:
    def __init__(self) -> None:
        #通用設定
        pygame.init()
        self.Display_Surface = pygame.display.set_mode((Window_Width,Window_Height))
        self.Clock = pygame.time.Clock()
        pygame.display.set_caption("tetris_test")

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                    #離開遊戲
            #顯示
            self.Display_Surface.fill(Gray)

            #遊戲畫面更新
            pygame.display.update()
            self.Clock.tick(60) #遊戲幀數    
    
if __name__ == '__main__':
    main = Main()
    main.run()