import pygame

pygame.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

gameDisplay = pygame.display.set_mode((800,600))
gameDisplay.fill(BLACK)

# -------------------------------------------------
# ----- Pixel drawing --------------------
# -------------------------------------------------

# assigning the entire pixel array to a value using pygame.PixelArray()
pixAr = pygame.PixelArray(gameDisplay)
pixAr[10][20] = GREEN # MODIFY: set the color of this specified pixel to green

# Drawing a line
# Parameters: on where do we want to draw, what color, specify the two coordinates the draw the line between, thickness
pygame.draw.line(gameDisplay, BLUE, (100,200), (300,450),5)

# Drawing a rectangle
# Parameters: where to draw onto, color, top right x and y, followed by width and height
pygame.draw.rect(gameDisplay, RED, (400,400,50,25))

# Drawing a circle
# Parameters: where to draw, color, center point coordinate, radius
pygame.draw.circle(gameDisplay, WHITE, (150,150), 75)

# Drawing a polygon
# parameters: where to draw onto, color, a tuple representing the coordinates of each corner of the polygon
pygame.draw.polygon(gameDisplay, GREEN, ((25,75),(76,125),(250,375),(400,25),(60,540)))

# Now for some basic function to call upon these values and display them without shutting down
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # always important line if we need to update all the objects and everything to be shown on the window display
    # whether they change coordinates, expand, are removed, duplicated, added - Basically to update for every frame refreshed
    pygame.display.update()
