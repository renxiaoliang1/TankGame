import pygame
from pygame.locals import *
from util.utils import *
import sys


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

    #加载地图
    parseMap('./map/1.map',window,views)


    #获取坦克
    tank = list(filter(lambda view:isinstance(view,HeroTank),views))[0]

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

        #获取按压事件
        status = pygame.key.get_pressed()
        #判断是否有按键按压
        if 1 in status:
            #有按键按压
            if status[K_a]:
                tank.move(Direction.LEFT)
            elif status[K_d]:
                tank.move(Direction.RIGHT)
            elif status[K_w]:
                tank.move(Direction.UP)
            elif status[K_s]:
                tank.move(Direction.DOWN)

if __name__ == '__main__':
    start()