import pygame
import time
import random
from typing import Optional

pygame.init()

# GAME PARAMETERS 
WIDTH = 800
HEIGHT = 600

# RGB Color references
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 255)
BRIGHT_RED = (255, 0, 0)
BRIGHT_GREEN = (0, 255, 0)
# ===========================
BLOCK_COLOR = (53, 145, 253)
car_width = 73 # we define the car  width to identify where both edges of the car are for boundary check for hit
gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('A bit Racey') # あ　ビット　レイス

clock = pygame.time.Clock()
# load the sprite (our avatar,in this case)
carImg = pygame.image.load('racecar.png')
# Load the game icon
gameIcon = pygame.image.load('caricon.png')
pygame.display.set_icon(gameIcon)

# SOme other main parameters to control the flow of the game
pause = False
# game_exit = True
# ------------------------------------------------------
# --------------------------------UTILITY FUNCTIONS ------------------------------------
# ------------------------------------------------------
def car(x, y):
    "Function to draw the car"
    gameDisplay.blit(carImg, (x, y)) # blit() is to draw the image to the screen

def things(thingx, thingy, thingw, thingh, color): # draw obstacles
    "Draw a rectangle on the screen with a given set of coordinate and properties"
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def things_dodged(count):
    "Scoreboard to keep count of each block dodged by the player"
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(count), True, BLACK)
    gameDisplay.blit(text, (0, 0)) # set it on the top left corner of the window display

def text_objects(text, font):
    "Render the text objects for display"
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect() # get a rectangle to align the text to a text box

# UNUSED FUNCTION
# def message_display(text):
#     "Display the message onto the screen since Pygame does not have a specific display function from the library and end this game iteration to reset after quick sleep"
#     # For more reference to font's methods: https://www.pygame.org/docs/ref/font.html
#     largeText = pygame.font.Font('freesansbold.ttf', 115)
#     TextSurf, TextRect = text_objects(text, largeText)
#     TextRect.center = ((WIDTH/2), (HEIGHT/2))
#     gameDisplay.blit(TextSurf, TextRect)

#     pygame.display.update() # need to update the pygame display for the added element in the code line above
#     time.sleep(2)
#     game_loop()

def crash():
    "Crash scenario and gameover"
    largeText = pygame.font.SysFont("comicsansms", 115)
    TextSurf, TextRect = text_objects("You Crashed!!!", largeText)
    TextRect.center = ((WIDTH/2), (HEIGHT/2))
    gameDisplay.blit(TextSurf, TextRect)
    # the game will loop and restart after the 2 seconds
    # TODO: we need to define a restart and exit key besides just having the car crash as the main activator for the program termination

    while True:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_loop()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
        # gameDisplay.fill(WHITE)
        button("Play Again",150,450,100,50,GREEN, BRIGHT_GREEN,game_loop)
        button("Quit",550,450,100,50,RED, BRIGHT_RED, pygame.quit)

        pygame.display.update()
        clock.tick(15) 

def button(msg, x, y, w, h, ic, ac, action=None):
    """
    Create a button function to dynamically create other buttons
    msg: What do you want the button to say on it.
    x: The x location of the top left coordinate of the button box.
    y: The y location of the top left coordinate of the button box.
    w: Button width.
    h: Button height.
    ic: Inactive color (when a mouse is not hovering).
    ac: Active color (when a mouse is hovering).
    action: default, optional action if there is a keyboard or mouse click on the button
    """
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed() # this is to identify if there is a press on the mouse
    if x + w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    # NOTE: differ between font.Font() with font.SysFont()
    # this part will continue to display the button until a certain button is clicked on or an event takes place 
    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w/2)), (y + (h/2)))
    gameDisplay.blit(textSurf, textRect)

def intro():
    """Intro menu for the game"""
    intro = True
    while intro:
        for event in pygame.event.get():
            if event == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_loop()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

        # NOTE: ive gotta be careful with the indentation here, leave it in the outermost loop of the running loop in the intro
        gameDisplay.fill(WHITE)
        largeText = pygame.font.SysFont('comicsansms', 114)
        TextSurf, TextRect = text_objects('A Bit Racey', largeText)
        TextRect.center = ((WIDTH/2), (HEIGHT/2))
        gameDisplay.blit(TextSurf, TextRect)
        
    
        button("GO!",150,450,100,50, GREEN, BRIGHT_GREEN,game_loop)
        button("Quit",550,450,100,50, RED, BRIGHT_RED, pygame.quit) 
        # NOTE: as we pass a function as an argument to another function, remember to exclude out the parentheses: pygame.quit() -> pygame.quit
        # additionally, we can store functions in lists, dictionaries, or other data structures to organize and manage them
        pygame.display.update() # need to update the pygame display for the added element in the code line above
        clock.tick(15) # displaying a title at 15 FPS 
        # TODO: add some functional buttons for the player to use and click to play or exit

def paused():
    "Pause menu"
    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((WIDTH/2),(HEIGHT/2))
    gameDisplay.blit(TextSurf, TextRect)
    while paused:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_loop()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit() # I just think this quit is to be a safeguard for closing all instance of the window display
        # Uncomment the fille if you want the window to be cleared before paused is shown
        gameDisplay.fill(WHITE)
        button("Continue",150,450,100,50,GREEN,BRIGHT_GREEN, game_loop)
        button("Quit",550,450,100,50,RED,BRIGHT_RED,pygame.quit)

        pygame.display.update()
        clock.tick(15)  

# define a game loop for a more compact look on the program
def game_loop():
    global pause
    
    x = (WIDTH * 0.45)
    y = (HEIGHT * 0.8)
    x_change = 0

    # initialize a random object on the road in the game
    thing_startx = random.randrange(0, WIDTH) # where, randomized the x, horizontal component
    thing_starty = -600 # specify as -600 so the player has a moment to get situated before the obstacle appears on the screen
    thing_speed = 7
    thing_width = 100 # obstacle properties width-height
    thing_height = 100

    # Counter for the score
    dodged = 0
    thingCount = 1
    game_exit = False # this is the main variable to break the game loop if an event-ending scenario takes place
    # The MAIN LOOP, every action and condition statement for the features of the game must be included in this loop block
    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.KEYDOWN:
                # movement set
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT: # setting elif will cause a kind of unresponsive, jerky movement
                    x_change = 5
                # pause event laid out
                if event.key == pygame.K_p:
                    pause = True
                    paused()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        gameDisplay.fill(WHITE)
        x += x_change # bascially use x to move the car image in the car function in a horizontal axis with the window

        # obstacle rolling animation in the window display
        things(thing_startx, thing_starty, thing_width, thing_height, BLOCK_COLOR)
        thing_starty += thing_speed # obstacle to be dropping down (vertically), which will increment by thing_speed for every frame, OR move down by *thing_speed* pixels
        # car movement
        car(x, y)
        # checking score
        things_dodged(dodged)

        # Setting the boundary for the car, if hit, game over
        if x > WIDTH - car_width or x < 0:
            crash()                
        # Check if obstacle roll down to the end of the height -> we will reinitialize the objects at the top with a randomized x coordinate
        if thing_starty > HEIGHT:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, WIDTH)
            # increment the dodge counter
            dodged += 1
            # NOTE: each time a block is regenerated (not colliding with the car), we increase the difficulty with the speed and the size of the block respective to how far 
            # the player has gone without crashing
            thing_speed += 1
            thing_width += (dodged * 1.2)

        # Conditional check for collision with the obstacle - the block we generated
        # 1. check for if they overlap in height perspective
        if y < thing_starty + thing_height: # REMINDER: y-coordinate start from the top side of the block so we will need to append with the trailing length of the block
            print('Y collision - crossover')

            # this is to check if the car is hitting sideway on the obstacle, if both x and y collides, call upon crash()
            if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
                print('X collision - crossover')
                crash()
        
        pygame.display.update()
        clock.tick(60)

intro()
game_loop()
pygame.quit()
quit()