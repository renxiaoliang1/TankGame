"""
铁墙
"""
import pygame
class SteelWall:
    def __init__(self,x,y,window):
        #坐标
        self.x = x
        self.y = y
        #显示窗口对象
        self.window = window
        #图片Surface
        self.image = pygame.image.load('./img/steels.gif')

    def display(self):
        #把自己显示到window上
        self.window.blit(self.image,(self.x,self.y))
