# Reference: https://en.wikipedia.org/wiki/Ray_casting
import pygame
import sys
import random
import math
from typing import List, Tuple, Optional, Any
from lightSource import Ray, LightParticle
from boundary import Polygon

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
WIDTH, HEIGHT = 1000, 800

def drawRandomPolygons(surface: pygame.Surface, num_points: int) -> List[Tuple[int]]:
    points = []
    for _ in range(num_points):
        x = random.randint(0, surface.get_width())
        y = random.randint(0, surface.get_height())
        points.append((x, y))
    # color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return points

def drawRandomConvexPolygon(surface: pygame.Surface, num_points: int) -> List[Tuple[int, int]]:
    "Convex vs Concave: https://study.com/academy/lesson/what-is-a-convex-polygon-definition-examples.html#:~:text=A%20convex%20polygon%20is%20any,no%20vertices%20that%20point%20inward."
    center_x = random.randint(100, surface.get_width() - 100)
    center_y = random.randint(100, surface.get_height() - 100)
    radius = random.randint(50, 100)
    # Angle step determines the angle between each point
    angle_step = 360 / num_points
    points = []

    for i in range(num_points):
        # A small random variation is added to each angle to create randomness
        angle = angle_step * i + random.uniform(-angle_step / 4, angle_step / 4)
        x = center_x + int(radius * math.cos(math.radians(angle)))
        y = center_y + int(radius * math.sin(math.radians(angle)))
        points.append((x, y))
    return points

# Polygons presets for testing
poly1 = [(10, 20), (100, 15), (75, 178), (10, 60)]
poly2 = [(250, 60), (440, 90), (550, 250), (170, 70)]
poly3 = [(600, 350), (780, 560), (740, 550), (550, 450)]
poly4 = [(240, 500), (470, 450), (600, 590), (220, 580)]
poly5 = [(88, 390), (310, 250), (180, 550)]
poly6 = [(0,0), (WIDTH, 0), (WIDTH, HEIGHT), (0, HEIGHT)]
# Initialize the pygame 
pygame.init()
# Set the background
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Raycasting')
clock = pygame.time.Clock()

# Temporarily set it as a fixed location until we figure out the intersection thing
newLightSource = LightParticle(WIDTH/2, HEIGHT/2)

# Generate the 5 random polygons for init
# A tuple contains: List of xy-coordinate, RGB tuple
# polygons = [drawRandomConvexPolygon(screen, num_points=4) for _ in range(5)]
boundaries = [Polygon(poly1), Polygon(poly2), Polygon(poly3), Polygon(poly4), Polygon(poly5)]
# Setting segments for the wall
ScreenBoundary = Polygon(poly6)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Always draw the background first, then we draw stuff onto it
    screen.fill((255, 255, 255))
    # Polygons
    for boundary in boundaries:
        boundary.drawBoundary(screen=screen)

    # We break down all boundaries's segments then breakdown them into a list containing lists, each containing 2 tuples for starting and ending coordinates
    wallSegments = [segment for boundary in boundaries for segment in boundary.segments]
    newLightSource.displayLightRays(screen, WallSegments=wallSegments)

    # Cursor tracking
    pygame.draw.circle(screen, (255, 0, 0), pygame.mouse.get_pos(), radius=2, width=10)
    # Update new light source's position
    newLightSource.updateSourcePosition(pygame.mouse.get_pos())
    pygame.display.update()
    clock.tick(120)