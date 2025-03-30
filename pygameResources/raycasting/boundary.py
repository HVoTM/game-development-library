import pygame

from typing import List, Tuple

BLACK = (0, 0, 0)

class Polygon():
    "A Polygon class that we will use to render the interaction with the light sources"
    def __init__(self, points: List[Tuple[int]]):
        self.points = points
        # Segments are the information we will be using to compare intersection with the ray in the light source
        self.segments = self.createSegments(points)

    def createSegments(self, points: List[Tuple[int]]):
        segments = []
        for i in range(len(points)):
            startingPoint = points[i]
            endingPoint = points[(i+1)%len(points)]
            segments.append((startingPoint, endingPoint))
        # Each segment of a polygon will contain a list of two tuples, starting xy-position and ending xy-position
        return segments

    def drawBoundary(self, screen: pygame.Surface) -> None:
        "Utility function to draw the polygons, this will draw the polygons based on the points"
        pygame.draw.polygon(screen, color=BLACK, points=self.points, width=1)