import pygame
from pygame.locals import *
from util.local import *
import sys
from views.HeroTank import HeroTank
from views.GrassWall import GrassWall
from views.SteelWall import SteelWall
from views.BrickWall import BrickWall
from views.WaterWall import WaterWall

def start():
    #初始化游戏
    pygame.init()
    #显示窗口
    window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    #修改游戏标题和图片
    pygame.display.set_caption("坦克大战")
    #修改游戏图标
    iconImage = pygame.image.load('./img/star.gif')
    #设置图标
    pygame.display.set_icon(iconImage)
    #创建坦克对象
    tank = HeroTank(x=100,y=100,window=window)
    grass = GrassWall(x=160,y=160,window=window)
    water = WaterWall(x=220,y=220,window=window)
    steel = SteelWall(x=280,y=280,window=window)
    brick = BrickWall(x=340,y=340,window=window)

    #死循环控制程序不退出
    while True:
        #显示坦克
        tank.display()
        grass.display()
        steel.display()
        water.display()
        brick.display()
        #刷新
        pygame.display.flip()


        #处理事件
        eventList = pygame.event.get()
        #遍历事件
        for eventEle in eventList:
            if eventEle.type == QUIT:
                #退出游戏界面
                pygame.quit()
                #退出程序
                sys.exit()

if __name__ == '__main__':
    start()