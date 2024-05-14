import pygame
# init the library, basic pygame syntax
pygame.init()

res = (1280, 720)
screen = pygame.display.set_mode(res)

while True:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
