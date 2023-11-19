from settings import *
from sys import exit

#components
from game import Game
from score import Score
from preview import Preview


class Main:
    def __init__(self) -> None:
        #一般設定
        pygame.init()
        self.display_surface = pygame.display.set_mode((Window_Width,Window_Height))
        self.Clock = pygame.time.Clock()
        pygame.display.set_caption("tetris_test")

        self.game = Game()
        self.score = Score()
        self.preview = Preview()

    def run(self):
        while True:
            for Event in pygame.event.get():
                if Event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                    #離開遊戲
            #顯示
            self.display_surface.fill(Gray)
            
            self.game.run()
            self.score.run()
            self.preview.run()

            #遊戲畫面更新
            pygame.display.update()
            self.Clock.tick(60) #遊戲幀數    
    
if __name__ == '__main__':
    main = Main()
    main.run()