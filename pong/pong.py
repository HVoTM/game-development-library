import pygame
import button
from sys import exit

pygame.init()

# Setting FPS (frame rate) in Pygame to control the speed
clock = pygame.time.Clock()
dt = clock.tick(30)

# inbuild timers
timer_event = pygame.event.custom_type()
pygame.time.set_timer(timer_event, 1000) # 1 second

# Font for displaying the timer
font = pygame.font.Font(None, 36)

WIDTH, HEIGHT = 1000, 600
wn = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Colors
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Instantiating the buttons
resumeButton = button.Button(450, 20, pygame.image.load("images/button_resume.png").convert_alpha(), 0.8)

# Settings for the pong ball
radius = 15
ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius # the ball will be set at the center
vel_x, vel_y = 0.5, 0.5

# For the paddles
paddle_width, paddle_height = 20, 120
paddle_y = paddle_y1 = HEIGHT/2 - paddle_height/2
paddle_x, paddle_X = 100 - paddle_width/2, WIDTH - (100 - paddle_width/2)
paddle_vel = paddle_vel1= 0

#for the gadgets
gad = act = 0 
g_left = G_left = 3

# Score for both sides
left_score = right_score = 0

run = True
paused = False
start_ticks = pygame.time.get_ticks() # Get the number of milliseconds since the Pygame module was initialized

def pauseMenu():
    global paused
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p or event.key == pygame.K_ESCAPE:
                    paused = False
        # Fill out the screen with black background color
        wn.fill(BLACK)
        # Render the pause text 
        pause_text = font.render("Paused: Press P or ESC to continue", True, WHITE)
        # Calculate the position to center the text
        text_rect = pause_text.get_rect(center=(WIDTH/2, HEIGHT/2))
        wn.blit(pause_text, text_rect)

        # We would want the resume button after "wn.fill(BLACK)"
        if resumeButton.draw(wn):
            paused = False

        pygame.display.update()
        clock.tick(30)

while run:
    wn.fill(BLACK) # set background to black
    
    # Timer
    seconds = (pygame.time.get_ticks() - start_ticks) / 1000 # calculate how many seconds
    # Render the timer text
    timer_text = font.render(f"Time: {seconds}s", True, WHITE)
    wn.blit(timer_text, (10, 10))

    # Score board
    score_text = font.render(f"Score: {left_score} - {right_score}", True, WHITE)
    wn.blit(score_text, (WIDTH - 150, 10))
    """
    # for checking the time if has passed then close the game
    if seconds > 10: # if more than 10 seconds close the game
        run = False
    """    
    # for the inputs
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_UP:
                paddle_vel = -0.7
            if i.key == pygame.K_DOWN:
                paddle_vel = 0.7
            if i.key == pygame.K_w:
                paddle_vel1 = -0.7
            if i.key == pygame.K_s:
                paddle_vel1 = 0.7
            # Testing the gadgets functionality
            if i.key == pygame.K_RIGHT and g_left > 0:
                gad = 1
            if i.key == pygame.K_d and G_left > 0 :
                act = 1
            # Pause menu
            if i.key == pygame.K_p or i.key == pygame.K_ESCAPE:
                paused = True
                pauseMenu()

        elif i.type == pygame.KEYUP:
            paddle_vel = 0 
            paddle_vel1 = 0 

    # The Balls' movement controls    
    # Resetting the ball's position if it goes out of the screen
    # For y-axis consideration        
    if (ball_y <= 0 + radius) or (ball_y >= HEIGHT - radius):
        vel_y *= -1

    # For x-axis consideration
    if (ball_x >= WIDTH - radius):
        ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
        vel_x, vel_y = 0.5, 0.5
        vel_x *= -1
        left_score += 1
    if (ball_x <= 0 + radius):
        ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
        vel_x, vel_y = 0.5, 0.5 
        right_score += 1

    #paddle's movement controls
    if paddle_y >= HEIGHT - paddle_height:
        paddle_y = HEIGHT - paddle_height
    if paddle_y <= 0:
        paddle_y = 0
    if paddle_y1 >= HEIGHT - paddle_height:
        paddle_y1 = HEIGHT - paddle_height
    if paddle_y1 <= 0:
        paddle_y1 = 0

    if paddle_X <= ball_x <= paddle_X + paddle_width:
        if paddle_y <= ball_y <= paddle_y + paddle_height:
            ball_x = paddle_X
            vel_x *= -1
    
    if paddle_x <= ball_x <= paddle_x + paddle_width:
        if paddle_y1 <= ball_y <= paddle_y1 + paddle_height:
            ball_x = paddle_x + paddle_width
            vel_x *= -1  
   
    if gad == 1:
        if paddle_X <= ball_x <= paddle_X + paddle_width:
            if paddle_y <= ball_y <= paddle_y + paddle_height:
                ball_x = paddle_X
                vel_x *= -3.5
                gad = 0 

    if act == 1:
        if paddle_x <= ball_x <= paddle_x + paddle_width:
            if paddle_y1 <= ball_y <= paddle_y1 + paddle_height:
                ball_x = paddle_x + paddle_width
                vel_x *= -3.5
                act = 0  
    
    #raw movements
    paddle_y += paddle_vel
    paddle_y1 += paddle_vel1
    ball_x += vel_x
    ball_y += vel_y
 
    #drawings
    pygame.draw.circle(wn, WHITE, (ball_x, ball_y), radius)
    pygame.draw.rect(wn, RED, pygame.Rect(paddle_x, paddle_y1, paddle_width, paddle_height))
    pygame.draw.rect(wn, RED, pygame.Rect(paddle_X, paddle_y, paddle_width, paddle_height))
    if gad == 1:
        pygame.draw.circle(wn, WHITE, (paddle_X + 10, paddle_y + 10), 4)
    if act == 1:
        pygame.draw.circle(wn, WHITE, (paddle_x + 10, paddle_y1 + 10), 4)

    pygame.display.update()