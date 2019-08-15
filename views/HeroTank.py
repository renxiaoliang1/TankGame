"""
我方坦克
"""
import pygame
from base.view import *
from util.local import *
class HeroTank(View):
    def __init__(self,**kwargs):
        super(HeroTank, self).__init__(**kwargs,img='./img/p1tankU.gif')
        #坦克移动速度
        self.speed = 1
    def move(self,direction):
        """
        移动坦克
        :param direction:Direction枚举类型
        :return:
        """
        if direction==Direction.UP:
            self.y -= self.speed
        elif direction ==  Direction.DOWN:
            self.y -= self.speed
        elif direction ==  Direction.RIGHT:
            self.x += self.speed
        elif direction == Direction.LEFT:
            self.x -= self.speed


