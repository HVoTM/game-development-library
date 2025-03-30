import pygame
import sys
import random
from typing import List

def drawFloor():
    screen.blit(floor_surface, (floor_Xpos, 900))
    # Adding a second floor sprite in order to create a continuous floor running effect as we move onwards
    screen.blit(floor_surface, (floor_Xpos + WIDTH, 900)) # WIDTH is the width of the screen, the next floor should be able to cover right after the first one in the running display window

def createPipe():
    randomPipePosY = random.choice(PIPE_HEIGHTS) # randomly select a pipe height from the list of pipeHeight
    # create a pipe sprite at the far right, before it can even make entry into the screen
    # we will set the X-coordinate at 850, quite far ahead even with the screen width
    bottomPipe = pipeSurface.get_rect(midtop = (WIDTH + 250, randomPipePosY)) 
    topPipe = pipeSurface.get_rect(midbottom = (WIDTH + 250, randomPipePosY - 300)) 
    return bottomPipe, topPipe

def movePipes(pipes) -> List[pygame.Rect]:  
    for pipe in pipes:
        pipe.centerx -= PIPE_SPEED
    visiblePipes = [pipe for pipe in pipes if pipe.right > -50] # list comprehension to filter out the pipes that are still visible on the screen
    return visiblePipes

def drawPipes(pipes) -> None:
    for pipe in pipes:
        # Drawing the bottom pipe
        if pipe.bottom >= HEIGHT: # if the pipe is at the bottom of the screen
            screen.blit(pipeSurface, pipe)  
        # Drawing the top pipe
        else:
            # pygame.transform.flip() is used to flip the image. Further doc: https://www.pygame.org/docs/ref/transform.html#pygame.transform.flip
            flippedPipe = pygame.transform.flip(pipeSurface, False, True) # flip the pipe sprite by y direction, not x direction
            screen.blit(flippedPipe, pipe)

def checkCollision(pipes) -> bool:
    global canScore
    for pipe in pipes:
        "Check if the bird sprite collides with the pipe sprite"
        # Luckily pygame has a collision detection program for rectangles, which is very useful for this game
        # TRUST ME, I have been through the pain of writing a collision detection algorithm from scratch
        # Further doc: https://www.pygame.org/docs/ref/rect.html#pygame.Rect.colliderect
        if bird_rect.colliderect(pipe):
            hitSound.play()
            # print("Collision detected!")

            canScore = True # reset the canScore variable so that the bird can score again
            return False
        
        "Check if the bird sprite collides with the top or the bottom of the screen"
        # using <= or >= because we want to make sure the bird's perimeter can handle the collision and make sure the bird
        # can be registered as a collision when it hits the top or the bottom of the screen as pixel perfect collision is not necessary
        if bird_rect.top <= -100 or bird_rect.bottom >= 900:
            hitSound.play()
            canScore = True
            print("Collision detected!")
            return False
    return True

def rotateSprite(bird):
    # rotate the bird sprite
    # here we are rotating depending on the direction of the flight of the bird
    # if the bird is falling, then rotate the bird downwards (-birdMovement * 3) because of the way rotozoom() works
    newBird = pygame.transform.rotozoom(bird, -BIRD_MOVEMENT * 3, 1)
    return newBird

def birdAnimation():
    "A utility safeguard function to make sure the new bird sprite is with its proper rectangle size, otherwise the bird hitbox will be weird"
    newBirdSurface = birdFrames[birdIndex]
    newBird_rect = newBirdSurface.get_rect(center = (100, bird_rect.centery)) # create a new rectangle with the centery of the previous rectangle
    return newBirdSurface, newBird_rect

def scoreDisplay(gameState):
    "Function to display the score information based on the game state"
    if gameState == 'mainGame':
        # gameFont.render(): https://www.pygame.org/docs/ref/font.html#pygame.font.Font.render
        # render(text, antialias, color, background=None) -> Surface
        scoreSurface = gameFont.render(str(int(SCORE)), True, (255, 255, 255))
        scoreRect = scoreSurface.get_rect(center = (288, 100)) 
        screen.blit(scoreSurface, scoreRect)

    if gameState == 'gameOver':
        scoreSurface = gameFont.render(f'Score: {int(SCORE)}', True, (255, 255, 255))
        scoreRect = scoreSurface.get_rect(center = (288, 100)) 
        screen.blit(scoreSurface, scoreRect)
        highScoreSurface = gameFont.render(f'High Score: {int(HIGH_SCORE)}', True, (255, 255, 255))
        highScoreRect = highScoreSurface.get_rect(center = (288, 850)) 
        screen.blit(highScoreSurface, highScoreRect)

def updateScore():
    if SCORE > HIGH_SCORE:
        HIGH_SCORE = SCORE
    return HIGH_SCORE

def pipeScoreCheck():
    global SCORE, canScore
    if pipeList:
        for pipe in pipeList:
            # if the centerx of the pipe 
            if 95 < pipe.centerx < 105 and canScore:
                SCORE += 1
                scoreSound.play()
                canScore = False
            # If the pipe is moving further to the left, then the bird can score again
            if pipe.centerx < 0:
                canScore = True

def loadBirdSprites(color):
    "Function to load the bird sprites based on the color of the bird"
    bird_Downflap = pygame.transform.scale2x(pygame.image.load(f'sprites/{color}bird-downflap.png').convert_alpha())
    bird_Midflap = pygame.transform.scale2x(pygame.image.load(f'sprites/{color}bird-midflap.png').convert_alpha())
    bird_Upflap = pygame.transform.scale2x(pygame.image.load(f'sprites/{color}bird-upflap.png').convert_alpha())
    return [bird_Downflap, bird_Midflap, bird_Upflap]

def loadPipeSprites(color):
    "Function to load the pipe sprites based on the color of the pipe"
    return pygame.transform.scale2x(pygame.image.load(f'sprites/pipe-{color}.png').convert_alpha())

def fadeBackground(screen, background1, background2, duration):
    "Function to fade the background from background1 to background2 in a given duration"
    fade_surface = pygame.Surface((WIDTH, HEIGHT))
    for alpha in range(0, 256, 5):
        fade_surface.set_alpha(alpha)
        screen.blit(background1, (0, 0))
        screen.blit(fade_surface, (0, 0))
        pygame.display.update()
        pygame.time.delay(duration // 51)  # 51 steps for alpha from 0 to 255
    for alpha in range(255, -1, -5):
        fade_surface.set_alpha(alpha)
        screen.blit(background2, (0, 0))
        screen.blit(fade_surface, (0, 0))
        pygame.display.update()
        pygame.time.delay(duration // 51)

# GAME PARAMETERS & VARIABLES
WIDTH, HEIGHT = 576, 1024
GRAVITY_SPEED = 0.25
BIRD_MOVEMENT = 0
GAME_ACTIVE = True
DEATHFALL = False
FALL_ANIMATION_COMPLETE = False
FLOOR_SPEED = 2
PIPE_SPEED = 5

# https://www.pygame.org/docs/ref/mixer.html#pygame.mixer.pre_init
# The purpose of pre_init() is to preset the mixer init arguments before the pygame.init() is called
# This is to avoid the delay caused by the pygame.mixer.init() function
# NOTE: pre_init() must be called before the pygame.init() function
# pygame.mixer.pre_init(frequency = 44100, size = 16, channels = 1, buffer = 512)

pygame.init()

canScore = True
SCORE = 0
HIGH_SCORE = 0  
# moreover on font and such: https://www.pygame.org/docs/ref/font.html
# creating a new pygame's Font object
gameFont = pygame.font.Font('04B_19.ttf', 40)

screen = pygame.display.set_mode((WIDTH, HEIGHT)) # set the screen size
# Initialize the clock to manipulate the frames per second
# it may take a while to understand how the clock affects the game loop
clock = pygame.time.Clock()

"--------------------LOADING THE RESOURCE FILES ------------------"
# Background sprites
background_day = pygame.image.load('sprites/background-day.png').convert() # convert the image into a type of image that pygame can manipulate
background_day = pygame.transform.scale2x(background_day) # scale the background image 2x 
background_night = pygame.image.load('sprites/background-night.png').convert()
background_night = pygame.transform.scale2x(background_night)
current_background = background_day

floor_surface = pygame.image.load('sprites/base.png').convert()
floor_surface = pygame.transform.scale2x(floor_surface)
floor_Xpos = 0

# Import the bird sprite ----
# further on pygame.rect: https://www.pygame.org/docs/ref/rect.html
# bird_rect = birdSurface.get_rect(center = (100, 512)) # center the bird sprite in the middle of the screen
birdColors = ['blue', 'red', 'yellow']
birdFrames = loadBirdSprites(color=random.choice(birdColors)) # list of bird sprites for animation
birdIndex = 0
birdSurface = birdFrames[birdIndex]
bird_rect = birdSurface.get_rect(center = (100, 512)) # center the bird sprite in the middle of the screen
# Create a new event type by adding 1 to the previous latest event
BIRD_FLAPS = pygame.USEREVENT + 1 
pygame.time.set_timer(BIRD_FLAPS, 200) # every 200 milliseconds, change the bird sprite

# birdSurface = pygame.image.load('sprites/bluebird-midflap.png').convert_alpha() # convert_alpha() is used for images with transparency, if not, rotateSprite() will create black background for the bird sprite
# birdSurface = pygame.transform.scale2x(birdSurface)
# # points on a rectangle you can use in pygame: topleft, midtop, topright, midleft, center, midright, bottomleft, midbottom, bottomright

# Import the pipe sprite    
pipeColors = ['green', 'red']
pipeSurface = loadPipeSprites(color=random.choice(pipeColors))
# NOTE: pipeSurface is just an image object, we can use this to create multiple pipe sprites as we append it to pipeList down here
pipeList = [] # list to store the pipe sprites
SPAWNPIPE = pygame.USEREVENT # create a user event to spawn the pipes | NOTE: event is important for the game loop
pygame.time.set_timer(SPAWNPIPE, 1000) # every 1000 milliseconds, spawn a pipe
PIPE_HEIGHTS = [400, 500, 600, 700, 800]

# Game Over Screen
startNewGameSurface = pygame.transform.scale2x(pygame.image.load('sprites/message.png').convert_alpha())
startNewGameRect = startNewGameSurface.get_rect(center = (288, 512))

# ---- AUDIO ----
flapSound = pygame.mixer.Sound('audio/wing.wav')
hitSound = pygame.mixer.Sound('audio/hit.wav')
scoreSound = pygame.mixer.Sound('audio/point.wav')
newGamesound = pygame.mixer.Sound('audio/swoosh.wav')
deathSound = pygame.mixer.Sound('audio/die.wav')

#---------------------GAME LOOP----------------------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() # make sure the program exits!
        if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
            "NOTE: using both keydown and mousebuttondown is a hassle, maybe it's better to just use one of them"
            # SPACEBAR key: bird jumps and moves upwards, adding GAME_ACTIVE to make sure the falling animation does not get interrupted 
            if ((event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1)) and GAME_ACTIVE:
                # have to set the bird movement to 0 so that the bird does not keep falling
                # as the gravity will accumulate gradually so just adding 6 pixels would not suffice to counteract the gravity
                BIRD_MOVEMENT = 0
                BIRD_MOVEMENT -= 8 # the bird moves upwards by 8 pixels 
                flapSound.play() 
            
            if ((event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 )) and not GAME_ACTIVE and FALL_ANIMATION_COMPLETE:
                # RESETTING THE GAME
                SCORE = 0
                GAME_ACTIVE = True
                DEATHFALL = False
                FALL_ANIMATION_COMPLETE = False
                # reset the pipe assets
                pipeList.clear() 
                # RESET THE BIRD POSITION and load random new sprites
                birdFrames = loadBirdSprites(color=random.choice(birdColors))
                pipeSurface = loadPipeSprites(color=random.choice(pipeColors))
                newGamesound.play()
                bird_rect.center = (100, 512)
                BIRD_MOVEMENT = 0
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        # User-defined event
        if event.type == SPAWNPIPE:
            # print("Pipe spawned!")  # check if the pipe is spawned every 1200 milliseconds
            # since createPipe() returns a tuple of two pipes, we can use extend() to add the two pipes to the pipeList
            pipeList.extend(createPipe()) 

        if event.type == BIRD_FLAPS:
            birdIndex = (birdIndex + 1) % 3
            """
            # short form of the above code
                 
            if birdIndex > 2:
                birdIndex = 0
            else:
                birdIndex += 1  # increment the birdIndex by 1 
            """
            birdSurface = birdFrames[birdIndex]
            # get the new sprite and rectangle coordinate for the bird
            # birdSurface, bird_rect = birdAnimation()
    
    # Background
    screen.blit(background_day, (0, 0))
    # Implementing Game Logic for ACTIVE GAMEPLAY
    if GAME_ACTIVE:
        # Bird
        BIRD_MOVEMENT += GRAVITY_SPEED
        rotatedBird = rotateSprite(birdSurface)
        bird_rect.centery += BIRD_MOVEMENT # we can access the y-coordinate of the bird sprite using the centery attribute
        # The screen will display the bird rotation being controlled by the movement of the bird: if it is falling, rotating down, and vice versa  
        screen.blit(rotatedBird, bird_rect)

        GAME_ACTIVE = checkCollision(pipeList)
        # Pipes: update the pipes' positions, also this function will do asset management, keeping the necessary pipes
        # and remove pipes that are out of the screen
        pipeList = movePipes(pipeList)
        # BUG CHECK: print(pipeList)
        drawPipes(pipeList)
        # --- Score Check ---
        pipeScoreCheck()
        scoreDisplay("mainGame")
        
    # GAME OVER !
    else:
        # Adding deathfall animation
        if not DEATHFALL:
            DEATHFALL = True
            BIRD_MOVEMENT = 0
            deathSound.play()
        
        # adding a falling animation for the bird and check if it passes the screen height
        # then we conclude the animation
        if bird_rect.centery < 1000:
            BIRD_MOVEMENT += GRAVITY_SPEED
            bird_rect.centery += BIRD_MOVEMENT
            rotatedBird = rotateSprite(birdSurface)
            screen.blit(rotatedBird, bird_rect)
        else:
            FALL_ANIMATION_COMPLETE = True
        # Fall animation is complete then we display the game over screen
        if FALL_ANIMATION_COMPLETE:
            # Reset the pipe asset
            # pipeList.clear()
            # Update the high score
            if SCORE > HIGH_SCORE:
                HIGH_SCORE = SCORE
            scoreDisplay("gameOver")
            screen.blit(startNewGameSurface, startNewGameRect)

    # Update the floor position so that it moves to the left
    floor_Xpos -= FLOOR_SPEED
    drawFloor()
    # Reset the floor position so that the floor does not run out of the screen and stop
    if floor_Xpos <= -WIDTH: 
        # this is the point between the first and the second floor sprite
        # meaning as soon as the first floor sprite runs out of the screen, we reset the floor position 
        # so that the first floor is now adjacent to the second floor sprite to the right
        floor_Xpos = 0

    pygame.display.update()
    clock.tick(120) # 120 frames per second

    