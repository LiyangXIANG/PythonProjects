# encoding: utf-8
# Modified from ref: https://www.iteye.com/blog/xiaojingjing-2432839
import pygame
import sys
import random
import numpy as np

# 全局定义
SCREEN_X = 600
SCREEN_Y = 600
UNIT = 15  # 点以UNIT为单位

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
GREY = (120,120,120)

def setSpeed(grade):
    level = np.floor(grade/100)+1
    speed = level*2
    return speed

# 蛇类
class Snake(object):
    # 初始化各种需要的属性 [开始时默认向右/身体块x5]
    def __init__(self):
        self.direction = pygame.K_RIGHT
        self.body = []
        for x in range(5):
            self.addnode()

    # 在前端增加蛇块
    def addnode(self):
        left,top = (0,0)
        if self.body:
            left,top = (self.body[0].left,self.body[0].top)
        node = pygame.Rect(left,top,UNIT,UNIT)
        if self.direction == pygame.K_LEFT:
            node.left -= UNIT
        elif self.direction == pygame.K_RIGHT:
            node.left += UNIT
        elif self.direction == pygame.K_UP:
            node.top -= UNIT
        elif self.direction == pygame.K_DOWN:
            node.top += UNIT
        self.body.insert(0,node)

    # 删除最后一个块
    def delnode(self):
        self.body.pop()

    # 死亡判断
    def isdead(self):
        # 撞墙
        if self.body[0].x  not in range(SCREEN_X):
            return True
        if self.body[0].y  not in range(SCREEN_Y):
            return True
        # 撞自己
        if self.body[0] in self.body[1:]:
            return True
        return False

    # 移动！
    def move(self):
        self.addnode()
        self.delnode()

    # 改变方向 但是左右、上下不能被逆向改变
    def changedirection(self,curkey):
        LR = [pygame.K_LEFT,pygame.K_RIGHT]
        UD = [pygame.K_UP,pygame.K_DOWN]
        if curkey in LR+UD:
            if (curkey in LR) and (self.direction in LR):
                return
            if (curkey in UD) and (self.direction in UD):
                return
            self.direction = curkey


# 食物类
# 方法： 放置/移除
# 点以UNIT为单位
class Food:
    def __init__(self):
        self.rect = pygame.Rect(-UNIT,0,UNIT,UNIT)

    def remove(self):
        self.rect.x=-UNIT

    def set(self):
        if self.rect.x == -UNIT:
            allpos = []
            # 不靠墙太近 UNIT ~ SCREEN_X-UNIT 之间
            for pos in range(UNIT,SCREEN_X-UNIT,UNIT):
                allpos.append(pos)
            self.rect.left = random.choice(allpos)
            self.rect.top  = random.choice(allpos)



def show_text(screen, pos, text, color, font_bold = False, font_size = 60, font_italic = False):
    #获取系统字体，并设置文字大小
    cur_font = pygame.font.SysFont("宋体", font_size)
    #设置是否加粗属性
    cur_font.set_bold(font_bold)
    #设置是否斜体属性
    cur_font.set_italic(font_italic)
    #设置文字内容
    text_fmt = cur_font.render(text, 1, color)
    #绘制文字
    screen.blit(text_fmt, pos)


def main():
    pygame.init()
    screen_size = (SCREEN_X,SCREEN_Y)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption('Hungry Snake 2')
    clock = pygame.time.Clock()
    scores = 0
    isdead = False

    # 蛇/食物
    snake = Snake()
    food = Food()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                snake.changedirection(event.key)
                # 死后按space重新
                if event.key == pygame.K_SPACE and isdead:
                    return main()


        screen.fill(BLACK)

        # 画蛇身 / 每一步+1分
        if not isdead:
            scores+=1
            snake.move()
        for rect in snake.body:
            pygame.draw.rect(screen,WHITE,rect,0)

        # 显示死亡文字
        isdead = snake.isdead()
        if isdead:
            show_text(screen,(10,int(SCREEN_X/2-50)),'YOU ARE DEAD!',RED,False,50)
            show_text(screen,(10,int(SCREEN_X/2+10)),'press space to try again...',RED,False,30)

        # 食物投递
        food.set()

        # 食物处理 / 吃到+50分
        # 当食物rect与蛇头重合,吃掉 -> Snake增加一个Node
        if food.rect == snake.body[0]:
            scores += 50
            food.remove()
            food.set()
            snake.addnode()

        # 食物投递
        pygame.draw.rect(screen,RED,food.rect,0)

        # 显示分数文字
        show_text(screen,(10,SCREEN_Y-40),'Scores: '+str(scores),GREY,False,40)

        pygame.display.update()
        clock.tick(setSpeed(scores))


if __name__ == '__main__':
    main()