import math
import random as rnd
from random import choice

import pygame


FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600



class Ball:
    def __init__(self, screen: pygame.Surface, x, y, g=2):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        # время жизни шара в кадрах
        self.live = 80
        self.g = g

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        # описываем столкновения cо стенками
        if self.x > 800 - self.r:
            self.x = 800 - self.r
            self.vx = -self.vx
        if self.x < self.r:
            self.x = self.r
            self.vx = -self.vx
        if self.y < self.r:
            self.y = self.r
            self.vy = -self.vy
        if self.y > 600 - self.r:
            self.y = 600 - self.r
            self.vy = -self.vy

        # изменение cкорости за счет гравитации
        self.vy = self.vy + self.g

        #регистрация того, что шар прожил еще кадр
        self.live -= 1

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)

    def hittest(self, target):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте target.

        Args:
            target: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (target.x - self.x) ** 2 + (target.y - self.y) ** 2 <= (target.r + self.r) ** 2:
            return True
        else:
            return False

class Triangle:
    def __init__(self, screen: pygame.Surface, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 20
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        # время жизни треугольника в кадрах
        self.live = 80

    def move(self):
        """Переместить треугольник по прошествии единицы времени.

        Метод описывает перемещение треугольника за один кадр перерисовки. То есть, обновляет значения
        self.x и self.(размер окна 800х600).
        """
        self.x = self.x + self.vx
        self.y = self.y + self.vy

        #регистрация того, что треугольник прожил еще кадр
        self.live -= 1

    def draw(self):
        pygame.draw.polygon(self.screen, self.color,
                            [[self.x, self.y - self.r],
                             [self.x + math.sqrt(3)/2 * self.r, self.y + 1/2 * self.r],
                             [self.x - math.sqrt(3)/2 * self.r, self.y + 1/2 * self.r]])

    def hittest(self, target):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте target.

        Args:
            target: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (target.x - self.x) ** 2 + (target.y - self.y) ** 2 <= (target.r + self.r) ** 2:
            return True
        else:
            return False

class Gun:
    def __init__(self, screen, x):
        self.x = x
        self.y = 500
        self.v = 10
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = BLUE
        self.n = 1 # номер выстрела
        self.r = 15 # радиус поражения

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        if event.pos[0] - self.x == 0 and event.pos[1] - self.y < 0:
            self.an = - math.pi / 2
        if event.pos[0] - self.x == 0 and event.pos[1] - self.y > 0:
            self.an = math.pi / 2
        if event.pos[0] - self.x > 0:
            self.an = math.atan2((- event.pos[1] + self.y), (event.pos[0] - self.x))
        if event.pos[0] - self.x < 0:
            self.an = - math.atan2((event.pos[1] - self.y), (event.pos[0] - self.x))

        global balls, bullet
        bullet += 1

        if self.n % 5 != 0:
            new_ball = Ball(self.screen, self.x, self.y)
            new_ball.r += 5
            new_ball.vx = self.f2_power * math.cos(self.an)
            new_ball.vy = - self.f2_power * math.sin(self.an)
            balls.append(new_ball)

        # каждый десятный выстрел вылетает рокета (другой снаряд)
        else:
            new_ball = Triangle(self.screen, self.x, self.y)
            new_ball.vx = self.f2_power * math.cos(self.an)
            new_ball.vy = - self.f2_power * math.sin(self.an)
            balls.append(new_ball)


        self.f2_on = 0
        self.f2_power = 10
        self.n += 1
    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""

        if event.pos[0] - self.x == 0 and event.pos[1] - self.y > 0:
            self.an = -math.pi / 2
        elif event.pos[0] - self.x == 0 and event.pos[1] - self.y < 0:
            self.an = math.pi / 2
        elif event.pos[0] - self.x > 0:
            self.an = math.atan2(( - event.pos[1] + self.y), (event.pos[0] - self.x))
        elif event.pos[0] - self.x < 0:
            self.an = - math.atan2((event.pos[1] - self.y), (event.pos[0] - self.x))

        if self.f2_on:
            self.color = RED
        else:
            self.color = BLUE

    def draw(self):
        pygame.draw.line(screen, self.color, (self.x, self.y), (self.x + (20 + self.f2_power) * math.cos(self.an),
                                                         self.y + (20 + self.f2_power) * (-math.sin(self.an))), 5)
        pygame.draw.polygon(screen, self.color, [[self.x - 20, self.y],
                                                 [self.x - 30, self.y + 10],
                                                 [self.x - 30, self.y + 20],
                                                 [self.x + 30, self.y + 20],
                                                 [self.x + 30, self.y + 10],
                                                 [self.x + 20, self.y]])
        pygame.draw.circle(screen, self.color, (self.x - 15, self.y + 25), 5)
        pygame.draw.circle(screen, self.color, (self.x + 15, self.y + 25), 5)

    def move_right(self):
        self.x += self.v

    def move_left(self):
        self.x -= self.v

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = BLUE


class Target(Ball):

    def __init__(self, screen: pygame.Surface):
        # возьмем метод движения и рисования цели из класса Ball
        super().__init__(screen, x=40, y=450, g=3)
        super().move()
        super().draw()
        self.points = 0
        # время жизни цели
        self.live = 50
        self.vx = rnd.randint(5, 10)
        self.vy = rnd.randint(5, 10)
        self.x = rnd.randint(100, 700)
        self.y = rnd.randint(100, 600)
        self.r = rnd.randint(10, 50)
        self.screen = screen
        self.color = RED

    def new_target(self):
        """ Инициализация новой цели. """
        self.vx = rnd.randint(5, 10)
        self.vy = rnd.randint(5, 10)
        self.x = rnd.randint(100, 700)
        self.y = rnd.randint(100, 600)
        self.r = rnd.randint(10, 50)

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points

# второй тип мишеней
class Target1():

    def __init__(self, screen: pygame.Surface):
        self.points = 0
        self.live = 50
        self.vx = rnd.randint(5, 10)
        self.vy = rnd.randint(5, 10)
        self.x = rnd.randint(100, 700)
        self.y = rnd.randint(100, 600)
        self.a = rnd.randint(20, 50)
        self.r = 1.2 * self.a
        self.screen = screen
        self.color = (90, 0, 157)

    def new_target(self):
        """ Инициализация новой цели. """
        self.vx = rnd.randint(5, 10)
        self.vy = rnd.randint(5, 10)
        self.x = rnd.randint(100, 700)
        self.y = rnd.randint(100, 600)
        self.a = rnd.randint(10, 50)

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points

    def move(self):
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        # описываем столкновения cо стенками
        if self.x > 800 - self.a:
            self.x = 800 - self.a
            self.vx = -self.vx
        if self.x < 0:
            self.x = 0
            self.vx = -self.vx
        if self.y < 0:
            self.y = 0
            self.vy = -self.vy
        if self.y > 600 - self.a:
            self.y = 600 - self.a
            self.vy = -self.vy

        # регистрация того, что шар прожил еще кадр
        self.live -= 1

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.a, self.a))

# бомбы вылетают при нажатии пробела, они поражают танк
class Bomb:
    def __init__(self, screen: pygame.Surface):
        self.x = rnd.randint(50, 750)
        self.y = 10
        self.v = 20
        self.screen = screen
        self.live = 40
        self.r = 15 # радиус поражения
    def draw(self):
        pygame.draw.ellipse(screen, (102, 153, 102),
                            (self.x - 15, self.y, 30, 45))
        pygame.draw.polygon(self.screen, (102, 153, 102),
                            [[self.x, self.y + 5],
                             [self.x + 15, self.y - 10],
                             [self.x - 15, self.y - 10]])
    def move(self):
        self.y += self.v
        self.live -= 1

    def hittest(self, gun):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте gun.

        Args:
            gun: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (gun.x - self.x) ** 2 + ((gun.y + 10) - (self.y + 15)) ** 2 <= (gun.r + self.r) ** 2:
            return True
        else:
            return False

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# создаем счетчик очков
def counter(n):
    '''
    фунуция выводит количество очков n
    :param n: количество очков
    '''
    counter1 = pygame.font.Font(None, 48)
    text = counter1.render(str(n), True, (0, 0, 0))
    screen.blit(text, (20, 20))


bullet = 0
# массив для всех снарядов
balls = []
# массив для всех мишеней
targets = []

# количество мишеней
number_of_targets = 3

for i in range(number_of_targets):
    a = Target(screen)
    targets.append(a)

number_of_targets1 = 3

for i in range(number_of_targets):
    a = Target1(screen)
    targets.append(a)

clock = pygame.time.Clock()
gun = Gun(screen, 60)
gun2 = Gun(screen, 700)
target = Target(screen)

finished = False

score = 0

flag1 = 0

flag2 = 0

bombs = []

while not finished:
    screen.fill(WHITE)
    counter(score)
    gun.draw()
    gun2.draw()

    for i in bombs:
        i.draw()
        i.move()
        if i.live <= 0:
            bombs.remove(i)

        if i.hittest(gun):
            finished = True

    for i in targets:
        i.draw()

    for b in balls:
        b.draw()
        # удаляем шары, если они живут долго
        if b.live <= 0:
            balls.remove(b)

    for i in targets:
        if i.live <= 0:
            i.new_target()
            i.live = 200
        pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
            gun2.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
            gun2.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)
            gun2.targetting(event)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                flag1 = 1
            if event.key == pygame.K_a:
                flag2 = 1
            if event.key == pygame.K_SPACE:
                new_bomb = Bomb(screen)
                bombs.append(new_bomb)


        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                flag1 = 0
            if event.key == pygame.K_a:
                flag2 = 0



    if flag1 == 1:
        gun.move_right()
    if flag2 == 1:
        gun.move_left()
    # двигаем цели
    for i in targets:
        i.move()

    for b in balls:
        b.move()
        for i in targets:
            if b.hittest(i) and i.live:
                i.live = 0
                i.hit()
                i.new_target()
                i.live = 200
                if b in balls:
                    balls.remove(b)

    gun.power_up()

    # счет игрока
    full_score = 0

    for i in targets:
        full_score += i.points

    score = full_score

pygame.quit()

# описание: один танк ездит, управление клавишами a, d, второй стоит может слабо стрелять, при нажатии пробела летят торпеды,
# если они попадают в двигающийся танк, игра заканчивается, каждый пятый выстрел из танка - треугольная рокета