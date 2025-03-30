# flappy-bird-assets

Assets to develop the Flappy Bird Game
# TODO
- [x] asset management with pipes: reset pipe right after death, do not wait until game restarts
    - FIXED: move the pipelist clear from when restarting new game by pressing the SPACEBAR key to where GAME_ACTIVE == False
- [x] add FALLING DEATH animation
- [x] sprites selection for bird: red, yellow color. OR just randomized them for every new game
- [x] pipe color changes: green and red for new game
- [] knowing how to set background for night background cover, like maybe fading into it?
- [] adding an AI Reinforcement learning agent to learn 
- [] adding gradual difficulty, such as:
    - [x] different pipe gaps
    - [x] closer pipe spawn -> Faster spawn rate
    - [] moving pipes

# NOTE/CONCEPTS
## Text in pygame
1. Create a font (style, size)
2. Render the font (text, colour)
3. Use the resulting text surface

## Audio and Sound Effects
- pygame.mixer()
- problem with pygame.mixer.init() so we have to use `pygame.mixer.pre_init()` before `pygame.init()` so we can have the resources value not being delayed. It is a common practice

## Fading background/ Scrolling background
### Scrolling, infinite background
- Load 2 sprites of the same background next to each other
- For this example, the background will roll to the left
- So we will gradually decrement the x-coordinate of both by a standard value
- Then, whenever the first background is out of the screen, we attach it to the rightmost x-coordinate, which is usually not in the screen yet.
- Repeated this process then we gud
- NOTE: we have to make sure the background matches the width of the screen (or height, depending on which direction you want to scroll over) so that the image does not overflow or cause some asymmetry when scrolling indefinitely.
- I am sure that there some better way to implement this 

## IMPORTANT _ NOTEWORTHY - User-event time trigger
- source: https://www.pygame.org/docs/ref/time.html#pygame.time.set_timer
> repeatedly create an event on the event queue

```py
BIRD_FLAPS = pygame.USEREVENT + 1 
pygame.time.set_timer(BIRD_FLAPS, 200) # every 200 milliseconds, change the bird sprite
```

# Log
- When adding randomized choice for bird skins and fall animation (both deathfall and fall_animation_complete), error arised: if you kept repeatedly hitting the space button when death animation is still ongoing, there seemed to be a mashup of game reset and game ending