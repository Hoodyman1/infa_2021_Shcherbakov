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


class Ball:
    def __init__(self):
        self.Vx = randint(-20, 20)
        self.Vy = randint(-20, 20)
        self.x = randint(100, 1100)
        self.y = randint(100, 700)
        self.r = randint(10, 100)
        self.color = COLORS[randint(0, 5)]

    def check(self, pos):
        '''проверка на попадание по шарику'''
        if (pos[0] - self.x) ** 2 + (pos[1] - self.y) ** 2 <= self.r ** 2:
            return 1
        else:
            return 0

    def move(self):
        '''движение шарика'''
        dr.circle(screen, self.color, (self.x + self.Vx, self.y + self.Vy), self.r)
        self.x = self.x + self.Vx
        self.y = self.y + self.Vy
        # описываем столкновения cо стенками
        if self.x > 1200 - self.r:
            self.Vx = randint(-20, -1)
        if self.x < self.r:
            self.Vx = randint(1, 20)
        if self.y < self.r:
            self.Vy = randint(1, 20)
        if self.y > 800 - self.r:
            self.Vy = randint(-20, -1)


# создаем счетчик очков
def counter(n):
    '''
    фунуция выводит количество очков n
    :param n: количество очков
    '''
    counter1 = pygame.font.Font(None, 48)
    text = counter1.render(str(n), True, (255, 255, 255))
    screen.blit(text, (20, 20))


# создадим массив шаров
Balls = []

number_of_balls = 10

# создаем шары
for i in range(number_of_balls):
    new_Ball = Ball()
    Balls.append(new_Ball)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

# начальный счет
score = 0


while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        # чтобы пользователь мог выйти
        if event.type == pygame.QUIT:
            finished = True
        # проверка на поподание
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i in Balls:
                score += i.check(event.pos)
                # если по шарику попали, его удаляют, появляется новый
                if i.check(event.pos) == 1:
                    Balls.remove(i)
                    new_Ball = Ball()
                    Balls.append(new_Ball)

    # движение шариков
    for i in Balls:
        i.move()
        # реализовано странное взаимодействие шаров
        for j in Balls:
            if i != j:
                if (i.x - j.x) ** 2 + (i.y - j.y) ** 2 <= (i.r + j.r) ** 2:
                    i.Vx = -i.Vx
                    j.Vx = -j.Vx
                    i.Vy = -i.Vy
                    j.Vy = -j.Vy

    counter(score)
    pygame.display.update()
    screen.fill(BLACK)


pygame.quit()
pygame.font.quit()
