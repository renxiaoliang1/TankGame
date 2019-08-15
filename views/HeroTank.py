"""
我方坦克
"""
import pygame
from base.view import *
class HeroTank(View):
    def __init__(self,**kwargs):
        super(HeroTank, self).__init__(**kwargs,img='./img/p1tankU.gif')

    def move(self,direction):
        """
        移动坦克
        :param direction:Direction枚举类型
        :return:
        """
        #TODO
        print("移动")

