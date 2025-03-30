import pygame

# an integral part of every pygame application
pygame.init()

# this is basically the canvas we are drawing things onto
gameDisplay = pygame.display.set_mode((800, 600)) # dimension of the window should be a tuple !
pygame.display.set_caption('A bit Racey') # set the window caption (basically like a title)

clock = pygame.time.Clock()
"""use Clock to track time within the game, mostly used for FPS (Frames per Second) settings, 
the general standard is that human eye cannot perceive difference beyond 30 FPS"""

crashed = False

# --- MAIN GAME LOOP --- 
while not crashed:
    # the for loop will be present in most PyGame scripts, where events are being constantly logged
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed =True
        print(event)

    pygame.display.update()
    clock.tick(60) # setting 60 FPS

pygame.quit()
quit()
