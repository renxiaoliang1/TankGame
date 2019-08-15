import pygame
from pygame.locals import *
from util.local import *
import sys
from views.HeroTank import HeroTank

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
    tank = HeroTank(100,100,window)

    #死循环控制程序不退出
    while True:
        #显示坦克
        tank.display()
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