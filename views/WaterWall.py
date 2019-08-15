"""
水墙
"""
import pygame
from base.view import *
class WaterWall(View):
    def __init__(self,**kwargs):
        super(WaterWall, self).__init__(**kwargs,img='./img/water.gif')
