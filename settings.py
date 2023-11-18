import pygame
import pyautogui

#遊戲大小
Columns = 10
Rows = 20
Cell_Size = 40
Game_Width = Columns*Cell_Size
Game_Height = Rows*Cell_Size

#側邊欄位大小
SideBar_Width = 200
Preview_Height_Farction = 0.7
Socre_Height_Farction = 1-Preview_Height_Farction

#整體視窗大小
Padding = 20
Window_Width = Game_Width+SideBar_Width+Padding*3
Window_Height = Game_Height+Padding*2

#遊戲特性
Update_Start_Speed = 500 #程式每次更新間隔(ms)
Move_Wait_Time = 100
Rotate_Wait_Time = 200
Block_Offset = pygame.Vector2(Columns // 2, -1)

#顏色
Yellow = '#f1e60d'
Red = '#e51b20'
Blue = '#204b9b'
Green = '#56b32e'
Purple = '#7b217f'
Cyan = '#6cc6d9'
Orange = '#f07e13'
Gray = '#1C1C1C'
Line_Color = '#FFFFFF'

#方塊設定
Tetorminos = {
    "T" : {"Shape" : [(0,0), (-1,0), (1,0), (0,-1)], "Color":Purple},
    "O" : {"Shape" : [(0,0), (0,-1), (1,0), (1,-1)], "Color":Yellow},
    "J" : {"Shape" : [(0,0), (0,-1), (0,1), (-1,1)], "Color":Blue},
    "L" : {"Shape" : [(0,0), (0,-1), (0,1), (1,1)], "Color":Orange},
    "I" : {"Shape" : [(0,0), (0,-1), (0,-2), (0,1)], "Color":Cyan},
    "S" : {"Shape" : [(0,0), (-1,0), (0,-1), (1,-1)], "Color":Green},
    "Z" : {"Shape" : [(0,0), (1,0), (0,-1), (-1,-1)], "Color":Red}
}