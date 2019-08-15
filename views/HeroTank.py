"""
我方坦克
"""
import pygame
class HeroTank:
    def __init__(self,x,y,window):
        #坐标
        self.x = x
        self.y = y
        #显示窗口对象
        self.window = window
        #图片Surface
        self.image = pygame.image.load('./img/p1tankU.gif')

    def display(self):
        #把自己显示到window上
        self.window.blit(self.image,(self.x,self.y))
