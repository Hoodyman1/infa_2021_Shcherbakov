import pygame
import pygame.draw as dr
from random import randint
pygame.init()
pygame.font.init()

# игрок вводит имя в консоль
name = input('введите ваше имя   ')

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

def new_ball():
    '''
    рисует новый шарик со случайными координантами, радиусом, скоростью, цветом
    :return: массив со всей иформацией о шаре
    '''
    Vx = randint(-10, 10) #скорость по оси х
    Vy = randint(-10, 10)  #скорость по оси у
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

def bonus(x, y, flag):
    '''
    создает бонус
    :param x: координата левого верхнего угла бонуса по х
    :param y: координата левого верхнего угла бонуса по y
    :param flag: если флаг равен 1, то рисуем картинку 11, если 2, то 22
    '''
    if flag == 1:
        image = pygame.image.load('11.png').convert_alpha()
        screen.blit(image, (x, y))

    if flag == 2:
        image = pygame.image.load('22.png').convert_alpha()
        screen.blit(image, (x, y))



number_of_balls = 10

#создадим массив списков, каждый из которых описывает шар (координаты x, y, радиус, скорость Vx, скорост Vy, цвет)
Balls = []

#создаем шары добавляем информацию о них в массив Balls
for i in range(number_of_balls):
    Balls.append(new_ball())

pygame.display.update()
clock = pygame.time.Clock()
finished = False

#начальный счет игрока
score = 0

#метка обозначающая присутствие первой стадии бонуса на диспелее
flag1 = 0

#метка, обозначающая присутствие второй стадии бонуса на дисплее
flag2 = 0

#информация про бонус (x0, x, y, v), где x0 - начальная координата бонуса
bonus_inf = [0, 0, 0, 0]

#музыка для бонусного уровня
sound1 = pygame.mixer.Sound('скала.mp3')
sound2 = pygame.mixer.Sound('скала222.mp3')
sound3 = pygame.mixer.Sound('gop.mp3')


#считываем всех предыдущих игроков
input = open('list_of_players', 'r')
previous_list = input.readlines()
input.close()

while not finished:
    clock.tick(FPS)

    for event in pygame.event.get():
        #чтобы пользователь мог выйти
        if event.type == pygame.QUIT:
            finished = True
        #проверка на поподание, изменение счета игрока
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i in Balls:
                score += check(event.pos, i)
                #если по шарику попали, его удаляют, появляется новый
                if check(event.pos, i) == 1:
                    Balls.remove(i)
                    Balls.append(new_ball())
            # проверка на попадание по бонусу первой стадии
            if abs(event.pos[0] - (bonus_inf[1] + 150)) < 145 and abs(event.pos[1] - (bonus_inf[2] + 113)) < 105 and flag2 == 1:
                flag2 = 0
                score = score + 10
                sound2.stop()
                sound3.stop()

            # проверка на попадание по бонусу второй стадии
            if abs(event.pos[0] - (bonus_inf[1] + 150)) < 145 and abs(event.pos[1] - (bonus_inf[2] + 113)) < 105 and flag1 == 1 and flag2 == 0:
                bonus_inf[3] = 2 * bonus_inf[3]
                flag2 = 1
                flag1 = 0
                score = score - 5
                sound1.stop()
                sound2.play()
                sound3.play()

    #движение шариков
    for i in Balls:
        dr.circle(screen, i[5], (i[0] + i[3], i[1] + i[4]), i[2])
        i[0] = i[0] + i[3]
        i[1] = i[1] + i[4]
        # описываем столкновения cо стенками
        if i[0] > 1200 - i[2]:
            i[3] = randint(-10, -1)
        if i[0] < i[2]:
            i[3] = randint(1, 10)
        if i[1] < i[2]:
            i[4] = randint(1, 10)
        if i[1] > 800 - i[2]:
            i[4] = randint(-10, -1)

    # если на поле есть бонус, двигаем его по прямоугольнику

    #если стадия первая
    if flag1 == 1:

        if bonus_inf[2] <= 0.513 * bonus_inf[0]:
            bonus_inf[1] = bonus_inf[3] + bonus_inf[1]
            bonus(bonus_inf[1], bonus_inf[2], 1)

        if bonus_inf[1] >= bonus_inf[0] + 2 * (487 - bonus_inf[0]):
            bonus_inf[2] = bonus_inf[3] + bonus_inf[2]
            bonus(bonus_inf[1], bonus_inf[2], 1)

        if bonus_inf[2] >= 0.513 * bonus_inf[0] + 2 * (250 - 0.513 * bonus_inf[0]):
            bonus_inf[1] = bonus_inf[1] - bonus_inf[3]
            bonus(bonus_inf[1], bonus_inf[2], 1)

        if bonus_inf[1] <= bonus_inf[0]:
            bonus_inf[2] = bonus_inf[2] - bonus_inf[3]
            bonus(bonus_inf[1], bonus_inf[2], 1)

    #если стадия вторая
    if flag2 == 1:

        if bonus_inf[2] <= 0.513 * bonus_inf[0]:
            bonus_inf[1] = bonus_inf[3] + bonus_inf[1]
            bonus(bonus_inf[1], bonus_inf[2], 2)

        if bonus_inf[1] >= bonus_inf[0] + 2 * (487 - bonus_inf[0]):
            bonus_inf[2] = bonus_inf[3] + bonus_inf[2]
            bonus(bonus_inf[1], bonus_inf[2], 2)

        if bonus_inf[2] >= 0.513 * bonus_inf[0] + 2 * (250 - 0.513 * bonus_inf[0]):
            bonus_inf[1] = bonus_inf[1] - bonus_inf[3]
            bonus(bonus_inf[1], bonus_inf[2], 2)

        if bonus_inf[1] <= bonus_inf[0]:
            bonus_inf[2] = bonus_inf[2] - bonus_inf[3]
            bonus(bonus_inf[1], bonus_inf[2], 2)



    # каждые 20 очков будет появляться бонус, если его нет на дисплее
    if score % 20 == 0 and score != 0 and flag1 == 0 and flag2 == 0:
        #cоздаем координаты бонуса, его скорость
        x0 = randint(0, 300)
        y0 = 0.513 * x0  # изначально бонус располагается на главной диагонали экрана (0.513 - такой коэффициент, чтобы это выполнялось)
        v = randint(5, 15)

        bonus(x0, y0, 1)
        #сохраняем информацию про бонус
        bonus_inf[0] = x0
        bonus_inf[1] = x0
        bonus_inf[2] = y0
        bonus_inf[3] = v

        sound1.play()

        flag1 = 1

    counter(score)
    pygame.display.update()
    screen.fill(BLACK)

# информация про нового игрока
new_player = name + '   ' + str(score)

output = open('list_of_players', 'w')

#записываем информацию про старых игроков
for i in previous_list:
    output.write(i)
    output.write('\n')

#записываем нового игрока
output.write(new_player)

output.close()

pygame.quit()
pygame.font.quit()