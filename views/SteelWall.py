"""
铁墙
"""
import pygame
from base.view import *
class SteelWall(View):
    def __init__(self,**kwargs):
        super(SteelWall, self).__init__(**kwargs,img='./img/steels.gif')
