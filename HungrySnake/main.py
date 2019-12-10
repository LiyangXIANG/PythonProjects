import pygame
import sys,time,random
from pygame.locals import *
import numpy as np

pygame.init()
# 获取当前系统可用的字体
# print(pygame.font.get_fonts())
red = pygame.Color(255,0,0)
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
grey = pygame.Color(150,150,150)
STEP = 10
WIDTH = 640
HIGHT = 640
speed = STEP
grade = 0
changeDirection = False

def gameOver(playSurface):
    # gameOverFont = pygame.font.Font('arial',72)
    gameOverFont = pygame.font.SysFont('arial', 72)
    gameOverSurf = gameOverFont.render('Game Over!',True,red)
    gameOverRect = gameOverSurf.get_rect()
    gameOverRect.midtop = (WIDTH/2,10)
    # 调用blit方法绘制图像
    playSurface.blit(gameOverSurf,gameOverRect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    sys.exit()

def showGrade(playSurface,grade):
    gradeFont = pygame.font.SysFont('arial',30)
    gradeSurf = gradeFont.render('Grade:'+str(grade),True,white)
    gradeRect = gradeSurf.get_rect()
    gradeRect.midtop = (0.8*WIDTH, 10)
    playSurface.blit(gradeSurf, gradeRect)
    pygame.display.flip()


def getSpeed(grade,base=0.5):
    '''
    get current speed for the snake movement according to the grade: from slow to fast
    :param grade:
    :param base: initial time to move a step forward. default=0.5s
    :return:
    '''
    level = np.floor(grade/100) + 1
    speed = base/2
    return speed

def getGrade(eat,grade):
    '''
    get current grade after a move
    :param eat:
    :param grade:
    :return:
    '''
    if eat:
        grade += 20
    return grade

def generateReward(rewardPos,snakeSegments):
    '''
    随机生成奖励的位置
    :param rewardPos
    :param snakeSegments:
    :return:
    '''
    if rewardPos[0] == snakeSegments[0][0] and rewardPos[1]==snakeSegments[0][1]:
        # 重新生成奖励位置
        eat = True
        x = random.randrange(STEP, WIDTH - STEP, STEP)
        y = random.randrange(STEP, HIGHT - STEP, STEP)
        # 不能生成在蛇身体上
        while [x, y] in snakeSegments:
            x = random.randrange(STEP, WIDTH - STEP, STEP)
            y = random.randrange(STEP, HIGHT - STEP, STEP)
        rewardPos = [x, y]
    else:
        eat = False
    return rewardPos,eat

def move(direction,snakeSegments):
    '''
    action of how snake move automatically after click the button to choose a direction
    :param direction:
    :param snakeSegments:
    :return:
    '''
    # while True:
    head = snakeSegments[0]
    head_x = head[0]
    head_y = head[1]
    if direction == 'right':
        head = [head_x+STEP,head_y]
    elif direction =='left':
        head = [head_x - STEP, head_y]
    elif direction =='up':
        head = [head_x, head_y-STEP]
    elif direction == 'down':
        head = [head_x, head_y+STEP]
    return head



def main():
    pygame.init()
    grade = 0
    # 创建游戏的窗口
    playSurface = pygame.display.set_mode((WIDTH,HIGHT))
    # 创建时钟对象 (可以控制游戏循环频率)
    fpsClock = pygame.time.Clock()
    pygame.display.set_caption('Hungry Snake')

    snakeHead_x = 100
    snakeHead_y = 100
    snakeSegments = [[snakeHead_x,snakeHead_y],[snakeHead_x-STEP,snakeHead_y],[snakeHead_x-2*STEP,snakeHead_y]]
    rewardPos = [WIDTH/2,HIGHT/2]
    direction = 'right'

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    direction = 'right'
                elif event.key == pygame.K_LEFT or event.key == ord('a'):
                    direction = 'left'
                elif event.key == pygame.K_UP or event.key == ord('w'):
                    direction = 'up'
                elif event.key == pygame.K_DOWN or event.key == ord('s'):
                    direction = 'down'
                elif event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event((pygame.QUIT)))

            snakeHead = move(direction,snakeSegments)
            snakeSegments.insert(0, snakeHead)

            # 判断是否吃到奖赏,吃到的话，就重新生成奖赏位置
            if rewardPos[0] == snakeSegments[0][0] and rewardPos[1] == snakeSegments[0][1]:
                # 重新生成奖励位置
                eat = True
                x = random.randrange(STEP, WIDTH - STEP, STEP)
                y = random.randrange(STEP, HIGHT - STEP, STEP)
                # 不能生成在蛇身体上
                while [x, y] in snakeSegments:
                    x = random.randrange(STEP, WIDTH - STEP, STEP)
                    y = random.randrange(STEP, HIGHT - STEP, STEP)
                rewardPos = [x, y]
            else:  # 吃不到，则去掉最后一截蛇身
                eat = False
                snakeSegments.pop()
            # 获取成绩
            grade = getGrade(eat, grade)

            # 刷新pygame显示层
            playSurface.fill(black)
            for pos in snakeSegments:
                pygame.draw.rect(playSurface, white, pygame.Rect(pos[0], pos[1], STEP, STEP))
                pygame.draw.rect(playSurface, red, pygame.Rect(rewardPos[0], rewardPos[1], STEP, STEP))

            pygame.display.flip()  # 显示最近的屏幕

            # display grade
            showGrade(playSurface, grade)

            # 判断是否死亡
            snakeHead = snakeSegments[0]
            if snakeHead[0] > WIDTH or snakeHead[0] < 0:
                gameOver(playSurface)
            if snakeHead[1] > HIGHT or snakeHead[1] < 0:
                gameOver(playSurface)
            for pos in snakeSegments[1:]:
                if snakeHead[0] == pos[0] and snakeHead[1] == pos[1]:
                    gameOver(playSurface)

            pygame.display.update()
            fpsClock.tick(60)  # 每秒循环60次


if __name__ == "__main__":
    main()




