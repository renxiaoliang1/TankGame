"""
view是可以显示的控件
是所有控件的父类
"""
import pygame
class View:
    def __init__(self,**kwargs):
        """
        传任意类型
        :param kwargs:
        """
        self.x = kwargs['x']
        self.y = kwargs['y']
        #图片Surface
        self.image = pygame.image.load(kwargs['img'])
        #window
        self.window = kwargs['window']


    def display(self):
        self.window.blit(self.image,(self.x,self.y))


