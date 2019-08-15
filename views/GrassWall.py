"""
草
"""
import pygame
from base.view import *
class GrassWall(View):
    def __init__(self,**kwargs):
        super(GrassWall, self).__init__(**kwargs,img='./img/grass.png')

