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

def Cube():
    # this below notifies OpenGL that we are about to throw some code at it, GL_LINES tells OpenGL how to handle that code
    # in this case, it will treat the code as line-drawing code
    # NOTE: you will need to open and close like this example 
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
    glTranslatef(0.0, 0.0, -5)

    # the typical loop of Pygame
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # glRotatef() multiples the current matrix by a rotation matrix | Parameters: angle, x, y, z
        glRotatef(1, 3, 1, 1)
        # clearing function, we add a couple of special OpenGL spices to let the OpenGL know
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        # Once we have a clean canvas, we will call our Cube() function
        Cube()
        pygame.display.flip() # updaet our display
        pygame.time.wait(10)

main()