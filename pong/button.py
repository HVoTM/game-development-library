import pygame

# Class for the buttons
class Button():
    def __init__(self, x, y, image, scale):
        # Know the width and height of the image
        width = image.get_width()  
        height = image.get_height()
        # Equate the image to the scaled image
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        
        # Create a darker version of the image for the pressed state
        self.image_pressed = self.image.copy()
        self.image_pressed.fill((50, 50, 50), special_flags=pygame.BLEND_RGB_SUB)
        
        # Get the rectangle of the image for the button position in the screen for positioning
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        # Initialize the action is not activated
        action = False
        # Get mouse position
        pos = pygame.mouse.get_pos()

		# Check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # Draw button on screen
        if self.clicked:
            surface.blit(self.image_pressed, (self.rect.x, self.rect.y))
        else:
            surface.blit(self.image, (self.rect.x, self.rect.y))
        
        return action
