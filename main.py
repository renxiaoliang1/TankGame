import pygame
from pygame.locals import *
from util.local import *
import sys
from views.HeroTank import HeroTank
from views.GrassWall import GrassWall
from views.SteelWall import SteelWall
from views.BrickWall import BrickWall
from views.WaterWall import WaterWall

#保存界面上所有需要现实的控件
views = []

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

    #解析地图
    file = open('./map/1.map',encoding='utf-8')
    #全部读取
    lines = file.readlines()
    #遍历每一行
    for row in range(0,len(lines)):
        line = lines[row]
        #获取每一行字符
        for col in range(0,len(line)):
            str = line[col]
            if str == '主':
                #创建我方坦克
                tank = HeroTank(x=col*BLOCK_SIZE,y=row*BLOCK_SIZE,window=window)
                views.append(tank)


    #死循环控制程序不退出
    while True:
        #显示
        for view in views:
            view.display()
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