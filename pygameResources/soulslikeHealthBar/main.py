import pygame
import sys

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() # Inherit from the Sprite class
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(center=(400, 300))
        # Set the current health bar at random for now
        self.currentHealth = 1000
        self.maximumHealth = 1000
        self.targetHealth = 1000
        # Set the health bar length in pixels and the ratio of health to health bar length
        self.healthbarLength = 500
        self.healthRatio = self.maximumHealth / self.healthbarLength # number of health points per pixel
        self.healthChangeSpeed = 5 # advanced display for the actual health change between the target and the current

    def updateHealthBar(self):
        self.basicHealth()
        self.advancedHealthBar()

    "Functions to receive damage and replenish health"
    def getDamage(self, amount):
        healthLosssound.play()
        if self.targetHealth > 0:
            self.targetHealth -= amount
        if self.targetHealth < 0:
            self.targetHealth = 0 # making sure we don't go below zero
            # NOTE: but in real games, we would want to trigger a game over screen

    def getHealth(self, amount):
        healthGainSound.play()
        # Add the amount to the current health and keep it within the maximum health
        if self.targetHealth < self.maximumHealth:
            self.targetHealth += amount
        elif self.targetHealth >= self.maximumHealth:
            self.targetHealth = self.maximumHealth

    def basicHealth(self):
        "Static health bar, we will change the currentHealthBar to targetHealthBar, since we"
        # surface to draw on, Color, Rect (x, y, width, height), Stroke width <optional>
        pygame.draw.rect(screen, (255, 0, 0), (10, 10, self.targetHealth / self.healthRatio, 25)) # Draw the red health bar
        pygame.draw.rect(screen, (255, 255, 255), (10, 10, self.healthbarLength, 25), 4) # Draw the white border for the full health bar container

    def advancedHealthBar(self):
        """Animated health difference between current health and targeted health. 
        For this simulation, we will display the advanced bar right below. The advanced health bar is used in soulslike game because the update
        of the health may get interrupted by enemy's attack. In advanced gaming setting, the currentHealth will be updated to the targetHealth
        in a rate (which we have set as healthChangeSpeed) until the currentHealth reaches the targetHealth. The transition bar will be displayed
        to show the difference between the currentHealth and the targetHealth. The transition bar will be colored green if the currentHealth is
        less than the targetHealth, and yellow if the currentHealth is more than the targetHealth.
        If the player receives damage or so, the targetHealth will get updated then the currentHealth will be updated to the targetHealth
        """
        transitionWidth = 0
        transitionColor = (255, 0, 0) # RED 

        # Similar to the fundamental getHealth() and getDamage() functions, we will update the currentHealthbar to the update of targetHealthBar
        if self.currentHealth <= self.targetHealth:
            "Adding health"
            # update according to the 
            self.currentHealth += self.healthChangeSpeed
            # Get the difference between the target and the current health and display the difference with the transition bar
            transitionWidth = int((self.targetHealth - self.currentHealth) / self.healthRatio)
            transitionColor = (0, 255, 0) # GREEN
            
            
        if self.currentHealth > self.targetHealth:
            "Reducing health"
            self.currentHealth -= self.healthChangeSpeed
            # make the difference positive so that we can display the transition bar
            transitionWidth = int(-(self.targetHealth - self.currentHealth) / self.healthRatio)
            transitionColor = (255, 255, 0) # YELLOW
            
        
        # FIXED: for reducing healthbar, the expected yellow transition bar is not working. I suppose the targetHealth should be the red healthbar
        # in this case and the currenthealth being the yellow transition bar
        if transitionColor == (255, 255, 0):
            healthBar_rect = pygame.Rect(10, 45, int(self.targetHealth / self.healthRatio), 25)
        else:
            # Since we are receiving and lowering our health point, we need to use the current healthbar to show its depletion
            # the target bar will be red for the expected loss of health
            healthBar_rect = pygame.Rect(10, 45, int(self.currentHealth / self.healthRatio), 25)
        transition_rect = pygame.Rect(healthBar_rect.right, 45, transitionWidth, 25) # referencing the right side of the health bar
    
        # Draw the health bar, the transition bar, and the white border
        # surface to draw on, Color, Rect (x, y, width, height), Stroke width <optional>
        pygame.draw.rect(screen, (255, 0, 0), healthBar_rect) # Draw the red health bar
        pygame.draw.rect(screen, transitionColor, transition_rect) # Transition health bar
        pygame.draw.rect(screen, (255, 255, 255), (10, 45, self.healthbarLength, 25), 4) # Draw the white border
        
# INITIALIZATION
# pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()

# SFX
healthLosssound = pygame.mixer.Sound('roblox_oof.mp3')
healthGainSound = pygame.mixer.Sound('healthbonus.mp3')

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Health Bar Simulation')

clock = pygame.time.Clock()
# Create a player sprite, the GroupSingle class is used to create a single sprite
# player = Player()
player = pygame.sprite.GroupSingle()
player.add(Player())

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Testing damage and healing
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.sprite.getHealth(100)
            if event.key == pygame.K_DOWN:
                player.sprite.getDamage(100)
            
    screen.fill((30, 30, 30))
    # player.draw(screen)
    player.sprite.updateHealthBar()
    player.update()
    pygame.display.update()
    clock.tick(60)
