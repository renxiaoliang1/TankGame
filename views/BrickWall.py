"""
砖墙
"""
import pygame
from base.view import *
class BrickWall(View):
    def __init__(self,**kwargs):
        super(BrickWall, self).__init__(**kwargs,img='./img/walls.gif')
