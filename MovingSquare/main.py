import pygame
import sys,time,random
from pygame.locals import *
import numpy as np

# 获取当前系统可用的字体
# print(pygame.font.get_fonts())
red = pygame.Color(255,0,0)
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
grey = pygame.Color(150,150,150)
STEP = 10
WIDTH = 640
HIGHT = 640


def finishMove(playSurface):
    finshFont = pygame.font.SysFont('arial',30)
    finshSurf = finshFont.render('Finish moving',True,white)
    finshRect = finshSurf.get_rect()
    finshRect.midtop = (0.5*WIDTH, 0.5*HIGHT)
    playSurface.blit(finshSurf, finshRect)
    pygame.display.flip()

def main():
    pygame.init()
    grade = 0
    # 创建游戏的窗口
    playSurface = pygame.display.set_mode((WIDTH, HIGHT))
    # 创建时钟对象 (可以控制游戏循环频率)
    fpsClock = pygame.time.Clock()
    pygame.display.set_caption('Moving Square')
    pos = [20,20]
    direction = 'right'
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event((pygame.QUIT)))
        if direction == 'right':
            pos[0] += STEP
            if pos[0]==WIDTH-STEP:
                direction = 'down'
        elif direction == 'down':
            pos[1] += STEP
            if pos[1] == HIGHT-STEP:
                direction = 'left'
        elif direction == 'left':
            pos[0] -= STEP
            if pos[0] == STEP:
                direction = 'up'
        elif direction == 'up':
            pos[1] -= STEP
            if pos[1] <= STEP:
                finishMove(playSurface)
                time.sleep(5)
                sys.exit()
        # 绘制
        playSurface.fill(black)
        pygame.draw.rect(playSurface, white, pygame.Rect(pos[0], pos[1], STEP, STEP))
        pygame.display.flip()  # 显示最近的屏幕
        pygame.display.update()
        fpsClock.tick(60)  # 每秒循环60次



if __name__ == "__main__":
    main()




