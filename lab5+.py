import pygame
import pygame.draw as dr
from random import randint
pygame.init()
pygame.font.init()

FPS = 60
screen = pygame.display.set_mode((1200, 800))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

#создадим массив списков, каждый из которых описывает шар(координаты x, y, радиус, скоростьX, скорост Vy, цвет)
Balls = []

def new_ball():
    '''рисует новый шарик со случайными координантами, радиусом, скоростью, цветом'''
    Vx = randint(-20, 20) #скорость по оси х
    Vy = randint(-20, 20)  #скорость по оси у
    x = randint(100, 1100)
    y = randint(100, 700)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    dr.circle(screen, color, (x, y), r)
    Ball = [x, y, r, Vx, Vy, color]
    return Ball

def check(pos, Ball):
    '''
    проверяет, попал ли пользователь по шарику
    :param pos: позиция мыши
    :param Ball: информация о шаре (x, y, r, v, a, color)
    :return: 1, если попали, 0, если не попали
    '''
    if (pos[0] - Ball[0]) ** 2 + (pos[1] - Ball[1]) ** 2 <= Ball[2] ** 2: #теорема Пифагора
        return 1
    else:
        return 0

#создаем счетчик очков
def counter(n):
    '''
    фунуция выводит количество очков n
    :param n: количество очков
    '''
    counter1 = pygame.font.Font(None, 48)
    text = counter1.render(str(n), True, (255, 255, 255))
    screen.blit(text, (20, 20))

number_of_balls = 10

#создаем шары
for i in range(number_of_balls):
    Balls.append(new_ball())

pygame.display.update()
clock = pygame.time.Clock()
finished = False

#начальный счет
score = 0

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        #чтобы пользователь мог выйти
        if event.type == pygame.QUIT:
            finished = True
        #проверка на поподание
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i in Balls:
                score += check(event.pos, i)
                #если по шарику попали, его удаляют, появляется новый
                if check(event.pos, i) == 1:
                    Balls.remove(i)
                    Balls.append(new_ball())
    #движение шариков
    for i in Balls:
        dr.circle(screen, i[5], (i[0] + i[3], i[1] + i[4]), i[2])
        i[0] = i[0] + i[3]
        i[1] = i[1] + i[4]
        # описываем столкновения cо стенками
        if i[0] > 1200 - i[2]:
            i[3] = randint(-20, -1)
        if i[0] < i[2]:
            i[3] = randint(1, 20)
        if i[1] < i[2]:
            i[4] = randint(1, 20)
        if i[1] > 800 - i[2]:
            i[4] = randint(-20, -1)


    counter(score)
    pygame.display.update()
    screen.fill(BLACK)



pygame.quit()
pygame.font.quit()

