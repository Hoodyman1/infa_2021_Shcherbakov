import pygame

pygame.init()

FPS = 30

screen = pygame.display.set_mode((600, 600))
pygame.draw.rect(screen, (100, 100, 100), (0, 0, 600, 600))
pygame.draw.circle(screen, (255, 255, 0), (300, 300), 200)
pygame.draw.circle(screen, (0, 0, 0), (300, 300), 200, 3)
pygame.draw.rect(screen, (0, 0, 0), (200, 400, 200, 40))

pygame.draw.circle(screen, (255, 0, 0), (220, 250), 40)
pygame.draw.circle(screen, (0, 0, 0), (220, 250), 40, 3)
pygame.draw.circle(screen, (0, 0, 0), (220, 250), 15)

pygame.draw.circle(screen, (255, 0, 0), (380, 250), 30)
pygame.draw.circle(screen, (0, 0, 0), (380, 250), 30, 3)
pygame.draw.circle(screen, (0, 0, 0), (380, 250), 15)

pygame.draw.polygon(screen, (0, 0, 0), [(340,233), (333,213),
                               (488,163), (495,183)])

pygame.draw.polygon(screen, (0, 0, 0), [(263,231), (272,211),
                               (100,121), (90,141)])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()