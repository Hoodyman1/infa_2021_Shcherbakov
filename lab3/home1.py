import pygame
import math

pygame.init()

FPS = 30

screen = pygame.display.set_mode((1000, 800))

#фон
pygame.draw.rect(screen, (204, 255, 255), (0, 0, 1000, 400))
pygame.draw.rect(screen, (51, 204, 51), (0, 400, 1000, 400))
#дом
pygame.draw.rect(screen, (153, 102, 0), (160, 350, 250, 200))
pygame.draw.rect(screen, (0, 0, 0), (160, 350, 250, 200), 2)
#крыша
pygame.draw.polygon(screen, (255, 0, 102), [(160,350), (410,350),
                               (285,220)])

pygame.draw.polygon(screen, (0, 0, 0), [(160,350), (410,350),
                               (285,220)], 2)

#окно
pygame.draw.rect(screen, (0, 204, 204), (255, 425, 60, 50))
pygame.draw.rect(screen, (204, 102, 51), (255, 425, 60, 50), 2)

#облака
pygame.draw.circle(screen, (255, 255, 255), (450, 100), 50)
pygame.draw.circle(screen, (0, 0, 0), (450, 100), 50, 2)

pygame.draw.circle(screen, (255, 255, 255), (500, 100), 50)
pygame.draw.circle(screen, (0, 0, 0), (500, 100), 50, 2)

pygame.draw.circle(screen, (255, 255, 255), (550, 100), 50)
pygame.draw.circle(screen, (0, 0, 0), (550, 100), 50, 2)

pygame.draw.circle(screen, (255, 255, 255), (600, 100), 50)
pygame.draw.circle(screen, (0, 0, 0), (600, 100), 50, 2)

pygame.draw.circle(screen, (255, 255, 255), (550, 60), 50)
pygame.draw.circle(screen, (0, 0, 0), (550, 60), 50, 2)

pygame.draw.circle(screen, (255, 255, 255), (500, 60), 50)
pygame.draw.circle(screen, (0, 0, 0), (500, 60), 50, 2)

#дерево

pygame.draw.rect(screen, (51, 0, 0), (700, 350, 30, 180))

#листва

pygame.draw.circle(screen, (0, 102, 51), (700, 220), 50)
pygame.draw.circle(screen, (0, 0, 0), (700, 220), 50, 2)

pygame.draw.circle(screen, (0, 102, 51), (640, 260), 50)
pygame.draw.circle(screen, (0, 0, 0), (640, 260), 50, 2)

pygame.draw.circle(screen, (0, 102, 51), (760, 260), 50)
pygame.draw.circle(screen, (0, 0, 0), (760, 260), 50, 2)

pygame.draw.circle(screen, (0, 102, 51), (700, 290), 50)
pygame.draw.circle(screen, (0, 0, 0), (700, 290), 50, 2)


pygame.draw.circle(screen, (0, 102, 51), (660, 340), 50)
pygame.draw.circle(screen, (0, 0, 0), (660, 340), 50, 2)

pygame.draw.circle(screen, (0, 102, 51), (750, 345), 50)
pygame.draw.circle(screen, (0, 0, 0), (750, 345), 50, 2)

#cолнце
da = 2*math.pi/25
a = 0
for i in range(25):#triangle

    pygame.draw.polygon(screen, (255, 204, 204), [(970 - (1-math.cos(a))*70, 100 - 70*math.sin(a)),
                                (970 - (1-math.cos(a + da))*70, 100 - 70*math.sin(a + da)),
                                (975 - (1-math.cos(a + da/2))*75, 100 - 75*math.sin(a + da/2))])

    pygame.draw.polygon(screen, (0, 0, 0), [(970 - (1 - math.cos(a)) * 70, 100 - 70 * math.sin(a)),
                                      (970 - (1 - math.cos(a + da)) * 70, 100 - 70 * math.sin(a + da)),
                                      (975 - (1 - math.cos(a + da / 2)) * 75, 100 - 75 * math.sin(a + da / 2))], 3)
    a = a + da
pygame.draw.circle(screen, (255, 204, 204), (900, 100), 71)




pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()