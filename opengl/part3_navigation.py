# Help from this guy! : https://pythonprogramming.net/opengl-rotating-cube-example-pyopengl-tutorial/
import pygame
from pygame.locals import * # importing all of pygame locals
from OpenGL.GL import * # your typical OpenGL functions
from OpenGL.GLU import * # fancier OpenGL functions

# Define the location/coordinate of each vertex
# we are defining a cube with 8 vertices, or 8 corners, like how it should look geometrically
vertices= (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
    )

# Define the edges
# each tuple corresponds to a pair of vertex
# the first one will draw the edges betwene vertex 0 (1, -1, -1) and 1 (1, 1, -1), second will be for 0 and 3, and so forth
edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )

""" So, first we need some colors to choose from. OpenGL wants you to specify colors in an RGB format, but OpenGL expects it to be between 0 and 1, where 1 is the "strongest."

For example, a nice solid green would be: (0,1,0), which translates to 0 red, 1 green, 0 blue, or no red, full green, no blue
"""
colors = (
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (0,1,0),
    (1,1,1),
    (0,1,1),
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (1,0,0),
    (1,1,1),
    (0,1,1),
    )

# Define the surfaces - groups of vertices that make up the surface
surfaces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
    )

def Cube():
    # this below notifies OpenGL that we are about to throw some code at it, GL_LINES tells OpenGL how to handle that code
    # in this case, it will treat the code as line-drawing code
    # NOTE: you will need to open and close like this example 
    glBegin(GL_QUADS)
    for surface in surfaces:
        x = 0
        for vertex in surface:
            x+=1
            glColor3fv(colors[x])
            glVertex3fv(vertices[vertex])
    glEnd()

    # NOTE: if we draw the lines first, then the surface will overlap with the edges and may cause a transparent effect
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex]) # performs *glVertex3fv()* on the [vertex] element of the vertices tuple
    # notify OpenGL that we're done telling it waht to do
    glEnd()
    
def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    """
    The major difference in this Pygame code implementation compared to the usual work is that
    we are adding another parameter after the display in the last line
    DOUBLEBUF|OPENGL is a constant that will tell PyGame that we are feeding OpenGL code operations
    # DOUBLEBUF: stands for double buffer, a type of buffering where there are two buffers to comply with monitor refresh rates
    # '|' (pipe) symbol is used to separate constants   
    """

    # Determine the perspective 
    # - degree values of the Field of View (FOV)
    # - aspect ratio, which is the display width divided by the display height
    # - next two values: znear, zfar: near and far clipping planes
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    
    # Multiply the current matrix by a translation matrix
    glTranslatef(0.0,0.0, -5)
    
    glRotatef(25, 2, 1, 0)

    # the typical loop of Pygame
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # Movement features to navigate around the cube
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    glTranslatef(-0.5,0,0)
                if event.key == pygame.K_RIGHT:
                    glTranslatef(0.5,0,0)

                if event.key == pygame.K_UP:
                    glTranslatef(0,1,0)
                if event.key == pygame.K_DOWN:
                    glTranslatef(0,-1,0)
            
            # Pull the data from the user's mouse wheel, so we can implement zooming feature for our character
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    glTranslatef(0,0,1.0)

                if event.button == 5:
                    glTranslatef(0,0,-1.0)
        
        # glRotatef() multiples the current matrix by a rotation matrix | Parameters: angle, x, y, z
        # glRotatef(1, 3, 1, 1)
        # clearing function, we add a couple of special OpenGL spices to let the OpenGL know
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        # Once we have a clean canvas, we will call our Cube() function
        Cube()
        pygame.display.flip() # updaet our display
        pygame.time.wait(10)

main()
"""
Basically, for this program, you can use two main features:
- Move up, down, left, right with your arrow keys
- Zoom in and out with the middle mouse scroll
"""