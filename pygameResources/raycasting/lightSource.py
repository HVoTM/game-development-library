import pygame
import math
from typing import Tuple, List
from boundary import Polygon

RED = (255, 0, 0)
LIGHTRED = (255, 102, 102)
NUM_OF_RAYS = 100
RADIAN_OFFSET = 0.00001

class Ray():
    "Class object to display each ray and do stuff with it for raycasting"
    # Constructing the ray with position and direction
    def __init__(self, position: pygame.Vector2, direction: pygame.Vector2) -> None:
        # using pygame Vector: https://www.pygame.org/docs/ref/math.html#pygame.math.Vector2
        # self.pos = pygame.math.Vector2(x, y)
        # Origin point of ray
        self.position: pygame.Vector2 = position
        # Direction, or orientation of the line in parametric form
        self.direction: pygame.Vector2 = direction
        # Scale here is used to stretch out the ending point of the light ray to cover the whole screen
        self.scale: int = 10

    def drawRay(self, screen: pygame.Surface, intersectPoint = None) -> None:
        """Utility function to show the line of ray being cast throughout the screen
        Default the intersection Point to none if there is no intersection
        """
        # https://www.pygame.org/docs/ref/draw.html#pygame.draw.line
        # After determining if there is an intersection on the screen, we draw the closest intersection point
        if intersectPoint:
            # Draw the ray starting from the light origin to the end 
            pygame.draw.line(surface=screen, color=RED, start_pos=self.position, end_pos=(intersectPoint[0], intersectPoint[1]))
            pygame.draw.circle(surface=screen, color=RED, center=(intersectPoint[0], intersectPoint[1]), radius=3)
        """
        # FIXME or so: this condition will draw only the ray if it does not intersect with any segment on the screen
        # We are trying to reduce to the necessary rays so do not draw if not necessary
        else:
            # line(surface, color, start_pos, end_pos, width=1) -> Rect
            pygame.draw.line(surface=screen, color=RED, start_pos=self.position, end_pos=self.position + self.direction * self.scale)
        """  
    def checkWall(self, segments):
        "Utility function to check the wall"
        intersectionList = []
        # For current ray, check if it hits any wall segment, then retrieve the one with the shortest distance (lowest T1, which we will compare)
        for segment in segments:
            currIntersectionPoint = self.getIntersection(segment)
            if currIntersectionPoint:
                intersectionList.append(currIntersectionPoint)
        # After checking all walls, if there are intersection points, return the one with the smallest T1
        if intersectionList:
            # Retrieve the closest segment with the intersection points by comparing and retrieving the one with the lowest T1
            closestIntersectionPoints = min(intersectionList)
            print(closestIntersectionPoints)
            return closestIntersectionPoints[1:]
            """            
            # Checking the end points to see if it collides with other segments
            endPoints1 = self.EndPointsIntersectOtherSegments(closestIntersectionPoints[1], segments=segments)
            endPoints2 = self.EndPointsIntersectOtherSegments(closestIntersectionPoints[2], segments=segments)
            ans = [closestIntersectionPoints[1]]
            if endPoints1:
                ans.append(endPoints1)
            if endPoints2:
                ans.append(endPoints2)
            return ans
            """
        return None

    def getIntersection(self, segment) -> Tuple:
        "This is the most algebraic part where we compare the parametric forms between the wall and the light ray"
        # Get the coordinate of the starting and end points of the boundary
        x1, y1 = segment[0]
        x2, y2 = segment[1]

        # Get the starting and end point of the light - the infinite segment
        x3, y3 = self.position
        x4, y4 = self.position + self.direction * self.scale

        den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if den == 0:
            return None

        t2 = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
        t1 = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / den
        # Conforming to the condition of getting an appropriate intersection
        # If they aren't, then the supposed intersection is not on the ray/segment, 
        # and there is no intersection after all.
        # NOTE 0 <= t2 <= 1 to maintain the line segment of the boundary does not exceed the actual wall length
        # NOTE t1 >= 0 to preserve the direction of the ray
        if 0 <= t2 <= 1 and t1 > 0:
            # Including the end points of that segments for the purpose of smoothening the lighting coverage
            intersect_x = x1 + t2 * (x2 - x1)
            intersect_y = y1 + t2 * (y2 - y1)
            # Moreover, we also compute t1 parameters for each endpoint, which we will use to perform if the ray casting to those endpoints also
            # cut other segments before that
            """
            # FIXME: here is to add the segment's endpoints 
            t1_start = -((x1 - x3) * (y1 - y3) - (y1 - y3) * (x1 - x3)) / den
            t1_end = -((x2 - x3) * (y2 - y3) - (y2 - y3) * (x2 - x3)) / den
            m = 3  # Number of decimal places
            t1_start = float(f"{t1_start:.{m}f}")
            t1_end = float(f"{t1_end:.{m}f}")
            """
            # Return the t1 and intersection point coordinate
            return t1, (int(intersect_x), int(intersect_y)), (x1, y1), (x2, y2)
        return None
    
    def checkNumofIntersections(self, endPoints, segment) -> int:
        "Function to check if the given end points (x, y) of that intersecting segment is intersecting with other segments before it reaches the end point"
        # Get the coordinate of the starting and end points of the boundary
        x1, y1 = segment[0]
        x2, y2 = segment[1]
        print(endPoints)
        # Get the starting and end point of the light - the infinite segment
        x3, y3 = self.position
        x4, y4 = endPoints

        den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if den == 0:
            return 0

        t2 = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
        t1 = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / den
        # Conforming to the condition of getting an appropriate intersection
        # If they aren't, then the supposed intersection is not on the ray/segment, 
        # and there is no intersection after all.
        # NOTE 0 <= t2 <= 1 to maintain the line segment of the boundary does not exceed the actual wall length
        # NOTE t1 >= 0 to preserve the direction of the ray
        if 0 <= t2 <= 1 and t1 > 0:
            return 1
        return 0
    
    def EndPointsIntersectOtherSegments(self, endPoints, segments):
        count = 0
        for segment in segments:
            count += self.checkNumofIntersections(endPoints=endPoints, segment=segment)
        if count <= 1:
            return endPoints
        

class LightParticle():
    "This class will represent the light source that disperse the multiple rays we will be using for castin"
    def __init__(self, x, y):
        # Light source origins
        self.OriginPos = pygame.Vector2(x, y)
        print(self.OriginPos.y)
        # List of rays to shine upon: origin and ray direction
        self.rays = self.updateRays()

    def updateRays(self) -> List[Ray]:
        rays = []
        # 
        for i in range(NUM_OF_RAYS):
            angle = i * (360 / NUM_OF_RAYS)
            direction = pygame.Vector2(math.cos(math.radians(angle)), math.sin(math.radians(angle)))
            rays.append(Ray(self.OriginPos, direction))
            """
            # Adding two extra rays, with +/- 0.00001 radians offset for covering the wall behind any segment corners
            directionOffPlus = pygame.Vector2(math.cos(math.radians(angle)+RADIAN_OFFSET), math.sin(math.radians(angle)+RADIAN_OFFSET))
            directionOffMinus = pygame.Vector2(math.cos(math.radians(angle)-RADIAN_OFFSET), math.sin(math.radians(angle)-RADIAN_OFFSET))
            rays.extend([Ray(self.OriginPos, directionOffMinus), Ray(self.OriginPos, direction), Ray(self.OriginPos, directionOffPlus)])
            """
        return rays
    
    def displayLightRays(self, screen:pygame.Surface, WallSegments):
        # Draw the center for visual representation of the source
        pygame.draw.circle(surface=screen, center=self.OriginPos, color=RED, radius=5) # if we set the width, then the circle will be a hollow circle with a weighted width stroke
        intersectionPtList = []
        for ray in self.rays:
            curr_intersectionPt = ray.checkWall(WallSegments)
            if curr_intersectionPt:
                for x, y in curr_intersectionPt:
                    print(x, y)
                    intersectionPtList.append((x, y)) # We just want the last two for coordinates
                    ray.drawRay(screen=screen, intersectPoint=(x, y))
        # self.ray.drawRay(screen=screen, intersectPoint=self.ray.checkWall(WallSegments))
        # Draw the connection between the intersection points

        # This step is to connect between the rays
        # if intersectionPtList:
        #   self.connectIntersectionPoints(screen=screen, points=intersectionPtList)

    def updateSourcePosition(self, newOrigin: pygame.Vector2):
        "Utility function to update whenever the mouse move"
        self.OriginPos = pygame.Vector2(newOrigin)
        self.rays = self.updateRays()

    def connectIntersectionPoints(self, screen: pygame.Surface, points: List[Tuple[int, int]])-> None:
        "Connect the intersection of those points to visualize the visibility area"
        if len(points) > 1:
            points.sort(key=lambda point: math.atan2(point[1] - self.OriginPos.y, point[0] - self.OriginPos.x))
            # print(points)
            pygame.draw.polygon(screen, color=LIGHTRED, points=points, width=1)
            # pygame.draw.polygon(screen, color=RED, points=points)
            
