import pygame
import pygame.draw as dr

pygame.init()

FPS = 30

def make_background(color1, color2, X, Y, M):
    '''
    Эта функция создает поверхность и заливает фон двумя разными цветами
    :param color1: кортеж из трех элементов, соответствующий цвету первой части фона
    :param color2: кортеж из трех элементов, соответствующий цвету второй части фона
    :param X: ширина полотна
    :param Y: высота полотна
    :param M: граница (по у), разделяющая два цвета
    :return: возвращает изготовленную поверхность
    '''
    screen = pygame.display.set_mode((X, Y))
    pygame.draw.rect(screen, (color1[0], color1[1], color1[2]), (0, 0, X, M))
    pygame.draw.rect(screen, (color2[0], color2[1], color2[2]), (0, M, X, Y - M))
    return screen
#Далее описаны необходимые функции для рисования мужчины

def draw_left_leg(x, y, size):
    '''
    Функуия, рисующая левую ногу мужчины
    :param x: координата верха ноги по х
    :param y: координата верха ноги по у
    :param size: коэффициент, пропорционально которому меняется размер ноги
    '''
    # Выбранные нами констаты, характерезующие размер руки (35, 97, 55, 100 - из строк снизу),
    # произвольны, во всех последующих функциях эти константы также выбираем произвольно,
    # но так, чтобы выполнялись пропорции, сходные с картинокой оригиналом
    # параметр size меняет только масштаб, но не пропорции.
    dr.line(screen, (0, 0, 0), (x, y),
            (x - 35 * size, y + 97 * size))
    dr.line(screen, (0, 0, 0), (x - 35 * size, y + 97 * size),
            (x - 55 * size, y + 100 * size))

def draw_right_leg(x, y, size):
    '''
    Функуия, рисующая правую ногу мужчины
    :param x: координата верха ноги по х
    :param y: координата верха ноги по у
    :param size: коэффициент, пропорционально которому меняется размер ноги
    '''
    dr.line(screen, (0, 0, 0), (x, y),
            (x + 10 * size, y + 100 * size))
    dr.line(screen, (0, 0, 0), (x + 10 * size, y + 100 * size),
            (x + 40 * size, y + 105 * size))

def draw_body(x, y, size, color):
    '''
    Функция, рисующая тело человека в виде эллипса
    :param x: координата верхней точки эллипса по х
    :param y: координата верхней точки эллипса по у
    :param size: коэффициент, пропорционально которому меняется размер туловища
    :param color: кортеж из трех элементов, соответствующий цвету туловища
    '''
    dr.ellipse(screen, (color[0], color[1], color[2]), (x - 40 * size, y, 80 * size, 150 * size))

def draw_head(x, y, size, color):
    '''
    Функция, рисующая голову человека
    :param x: координата центра головы по х
    :param y: координата центра головы по у
    :param size: коэффициент, пропорционально которому меняется размер головы
    :param color: кортеж из трех элементов, соответствующий цвету головы
    '''
    dr.circle(screen, (color[0], color[1], color[2]), (x, y), 28 * size)

def draw_left_hand(x, y, size):
    '''
    Функция, рисующая левую руку
    :param x: координата верха руки по х
    :param y: координата верха руки по у
    :param size: коэффициент, пропорционально которому меняется размер руки
    '''
    dr.line(screen, (0, 0, 0), (x, y),
            (x - 55 * size, y + 75 * size))

def draw_right_hand(x, y, size):
    '''
    Функция, рисующая правую руку
    :param x: координата верха руки по х
    :param y: координата верха руки по у
    :param size: коэффициент, пропорционально которому меняется размер руки
    '''
    dr.line(screen, (0, 0, 0), (x, y),
            (x + 55 * size, y + 75 * size))

def draw_man(color1, color2, x, y, size):
    '''
    Эта функция рисует мужчину
    :param color1: кортеж из трех элементов, соответствующий цвету головы
    :param color2: кортеж из трех элементов, соответствующий цвету туловища
    :param x: координата верха головы по х
    :param y: координата верха головы по у
    :param size: коэффициент, пропорционально которому меняется размер человека
    '''
    draw_body(x, y + 43 * size, size, color2)
    draw_head(x, y + 28 * size, size, color1)
    draw_right_hand(x + 23 * size, y + 58 * size, size)
    draw_left_hand(x - 23 * size, y + 58 * size, size)
    draw_right_leg(x + 15 * size, y + 188 * size, size)
    draw_left_leg(x - 15 * size, y + 188 * size, size)

# Далее описаны все дополнительные функции, необходимые для рисования женщины
def draw_woman_body_and_head(color1, color2, x, y, size):
    '''
    Эта функция рисует треугольное тело женщины и голову на этом теле
    :param color1: цвет головы
    :param color2: цвет тела
    :param x: коордитната верхней точки головы по х
    :param y: коордитната верхней точки головы по у
    :param size: коэффициент размера
    '''
    # Рисование тела
    dr.polygon(screen, (color2[0], color2[1], color2[2]), [(x, y + 35 * size),
                                        (x + 55 * size, y + 179 * size),
                                        (x - 55 * size, y + 179 * size)])
    # Рисование головы
    dr.circle(screen, (color1[0], color1[1], color1[2]), (x, y + 28 * size), 28 * size)

def draw_woman_hands(x, y, size, flag):
    '''
    Функция рисует 2 руки девушки
    :param x: координата плеча правой руки по х
    :param y: координата плеча правой руки по у
    :param size: коэффициент размера
    :param flag: параметр, принимающий 2 значения: {0, 1}. 0 - в случае, если левая рука согнута, 1 - в противном случае.
    '''
    if flag == 0:
        # Рисуем правую руку
        dr.line(screen, (0, 0, 0), (x, y),
                (x + 70 * size, y + 75 * size))
        # Рисуем левую руку
        dr.line(screen, (0, 0, 0), (x - 15 * size, y),
                (x - 62 * size, y + 37 * size))
        dr.line(screen, (0, 0, 0), (x - 62 * size, y + 37 * size),
                (x - 99 * size, y))
    if flag == 1:
        # Рисуем левую руку
        dr.line(screen, (0, 0, 0), (x - 15 * size, y),
                (x - 85 * size, y + 75 * size))
        # Рисуем правую руку
        dr.line(screen, (0, 0, 0), (x, y),
                (x + 47 * size, y + 37 * size))
        dr.line(screen, (0, 0, 0), (x + 47 * size, y + 37 * size),
                (x + 85 * size, y))
    else:
        print('некорректно задано значение flag')

def draw_woman_legs(x, y, size):
    '''
    Функция рисует 2 ноги девушки
    :param x: координата верха правой ноги по х
    :param y: координата верха правой ноги по у
    :param size: коэффициент размера
    '''
    # Рисуем правую ногу
    dr.line(screen, (0, 0, 0), (x, y),
            (x, y + 86 * size))
    dr.line(screen, (0, 0, 0), (x, y + 86 * size),
            (x + 12 * size, y + 86 * size))
    # Рисуем левую ногу
    dr.line(screen, (0, 0, 0), (x - 40 * size, y),
            (x - 40 * size, y + 86 * size))
    dr.line(screen, (0, 0, 0), (x - 40 * size, y + 86 * size),
            (x - 52 * size, y + 86 * size))

def draw_woman(color1, color2, x, y, size, flag):
    '''
    Эта функция рисует женщин
    :param color1: цвет головы
    :param color2: цвет тела
    :param x: кооордитата верха головы по х
    :param y: кооордитата верха головы по у
    :param size: коэффициент размера
    :param flag: параметр, принимающий 2 значения: {0, 1}. 0 - в случае, если левая рука согнута, 1 - в противном случае.
    '''
    draw_woman_body_and_head(color1, color2, x, y, size)
    draw_woman_hands(x + 7 * size, y + 57 * size, size, flag)
    draw_woman_legs(x + 20 * size, y + 180 * size, size)

# Рисуем мороженое. Cнизу функция, которая это делает.
def icecream(surface, color, color1, color2, color3, x, y, size):
    '''
    Функция рисует мороженое на произвольной поверхности
    :param surface: поверхность на которой нужно нарисовать мороженое
    :param color: цвет вафли
    :param color1: цвет 1 шарика мороженого
    :param color2: цвет 2 шарика мороженого
    :param color3: цвет 3 шарика мороженого
    :param x: координата кончика рожка по х (координата в соответствующем surface)
    :param y: координата кончика рожка по у (координата в соответствующем surface)
    :param size: коэффициент размера
    '''
    dr.polygon(surface, (color[0], color[1], color[2]), [(x, y),
                                                           (x + 20 * size, y - 40 * size),
                                                           (x - 20 * size, y - 40 * size)])
    dr.circle(surface, (color1[0], color1[1], color1[2]), (x - 10 * size, y - 45 * size), 10 * size)
    dr.circle(surface, (color2[0], color2[1], color2[2]), (x + 10 * size, y - 45 * size), 10 * size)
    dr.circle(surface, (color3[0], color3[1], color3[2]), (x, y - 60 * size), 10 * size)

#Рисуем воздушный шар в виде сердца
def draw_ballon(surface, color, x, y, size):
    '''
    Функция риует воздушный шар в виде сердца на палочке
    :param surface: поверхность на которой нужно нарисовать воздушный шар
    :param color: цвет шара
    :param x: координата нижнего кончика шара по х
    :param y: координата нижнего кончика шара по у
    :param size: коэффициент размера
    '''
    dr.polygon(surface, (color[0], color[1], color[2]), [(x, y),
                                                           (x + 20 * size, y - 40 * size),
                                                           (x - 20 * size, y - 40 * size)])
    dr.circle(surface, (color[0], color[1], color[2]), (x - 10 * size, y - 40 * size), 10*size)
    dr.circle(surface, (color[0], color[1], color[2]), (x + 10 * size, y - 40 * size), 10 * size)
    dr.line(surface, (0, 0, 0), (x, y),
            (x, y + 70 * size))
def rot(surface, angle):
    '''
    Функция, делающая поворот поверхности
    :param surface: вращаемая поверхность
    :param angle: угол поворота
    :return: возвращает поверннутую поверхность
    '''
    new_surface = pygame.transform.rotate(surface, angle)
    return new_surface

#Все функции готовы, рисуем картинку

screen = make_background((204, 255, 255), (51, 204, 51), 1000, 800, 400)
draw_man((244, 227, 215), (167, 147, 172), 250, 350, 1)
draw_woman((244, 227, 215), (255, 85, 221), 405, 350, 1, 1)
draw_woman((244, 227, 215), (255, 85, 221), 590, 350, 1, 0)
draw_man((244, 227, 215), (167, 147, 172), 745, 350, 1)

#Создаем поверхность с прозрачным фоном для 1 мороженого
icecream1_screen = pygame.Surface((500, 500)).convert_alpha()
icecream1_screen.fill([0, 0, 0, 0])

icecream(icecream1_screen, (255, 204, 0), (85, 0, 0), (255, 0, 0), (255, 255, 255), 200, 300, 1)
icecream1_screen_1 = rot(icecream1_screen, -25)
screen.blit(icecream1_screen_1, (555, 133)) #Подгоняем координаты, чтобы мороженое попало в руку мужчине

#Создаем поверхность с прозрачным фоном для воздушного шарика
baloon_screen = pygame.Surface((500, 500)).convert_alpha()
baloon_screen.fill([0, 0, 0, 0])

draw_ballon(baloon_screen, (255, 0, 0), 50, 200, 1)
baloon_screen_1 = rot(baloon_screen, 20)
screen.blit(baloon_screen_1, (32, 74)) #Подгоняем координаты, чтобы шарик попало куда надо

#Рисуем 2 большое мороженое
icecream(screen, (255, 204, 0), (85, 0, 0), (255, 0, 0), (255, 255, 255), 497, 300, 2)

#Рисуем ножку для большого мороженого
dr.line(screen, (0, 0, 0), (497, 300), (497, 410))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()