"""
我方坦克
"""
import pygame
from base.view import *
from util.local import *
class HeroTank(View):
    def __init__(self,**kwargs):

        #坦克移动速度
        self.speed = 1
        #获取坦克方向
        self.direction = kwargs['direction']
        #保存所有方向的图片Surface
        self.images = [
            pygame.image.load('./img/p1tankL.gif'),
            pygame.image.load('./img/p1tankR.gif'),
            pygame.image.load('./img/p1tankU.gif'),
            pygame.image.load('./img/p1tankD.gif')
        ]
        super(HeroTank, self).__init__(**kwargs, img='./img/p1tankU.gif')
        #获取坦克需要显示的图片
        self.image = self.images[self.direction.value]
    def display(self):
        #修改显示图片
        self.image = self.images[self.direction.value]
        #父类的display
        super(HeroTank, self).display()

    def move(self,direction):
        """
        移动坦克
        :param direction:Direction枚举类型
        :return:
        """
        #改变方向
        self.direction = direction
        #移动
        if direction==Direction.UP:
            self.y -= self.speed
        elif direction ==  Direction.DOWN:
            self.y -= self.speed
        elif direction ==  Direction.RIGHT:
            self.x += self.speed
        elif direction == Direction.LEFT:
            self.x -= self.speed


