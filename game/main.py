import setting as s
import pygame
import random

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((s.settings.WIDTH, s.settings.HEIGHT))
pygame.display.set_caption("test game")
clock = pygame.time.Clock()

running = True
while running:
    clock.tick(s.settings.FPS)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    screen.fill(s.settings.BLACK)
    pygame.display.flip()

pygame.quit()