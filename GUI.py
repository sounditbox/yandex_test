import random

import pygame

pygame.init()

screen = pygame.display.set_mode((1000, 1000))
color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
screen.fill(color)
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit(0)
        if e.type == pygame.MOUSEBUTTONDOWN:
            color = random.randint(0, 255), \
                    random.randint(0, 255),\
                    random.randint(0, 255)

    screen.fill(color)
    pygame.display.flip()
