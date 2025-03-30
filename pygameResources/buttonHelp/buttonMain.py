import pygame
import button
# Create display window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Buttons Demo")

# Load button images
# For further reference on *.convert_alpha() method, see:
# https://www.pygame.org/docs/ref/surface.html#pygame.Surface.convert_alpha
# quick explanation: change the pixel format of an image including per pixel alphas
start_img = pygame.image.load("start_btn.png").convert_alpha()  # Start button
exit_img = pygame.image.load("exit_btn.png").convert_alpha()  # Exit button



#create button instances
start_button = button.Button(100, 200, start_img, 0.8)
exit_button = button.Button(450, 200, exit_img, 0.8)

# Game Loop
running = True
while running:

	screen.fill((202, 228, 241))

	if start_button.draw(screen):
		print('START')
	if exit_button.draw(screen):
		print('EXIT')

	#event handler
	for event in pygame.event.get():
		#quit game
		if event.type == pygame.QUIT:
			running = False

	pygame.display.flip() # Use for the full display
    # Use pygame.display.update() for partial display updates
pygame.quit()


    
