# Help from this guy! : https://pythonprogramming.net/opengl-rotating-cube-example-pyopengl-tutorial/
import pygame
from pygame.locals import * # importing all of pygame locals
from OpenGL.GL import * # your typical OpenGL functions
from OpenGL.GLU import * # fancier OpenGL functions
import random

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

def Cube(vertices) -> None:
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
    
def setVertices(max_distance):
    x_value_change = random.randrange(-10, 10)
    y_value_change = random.randrange(-10, 10)
    # max_distance parameter represents the maximum distance out that we are going to consider drawing cubes
    z_value_change = random.randrange(-1*max_distance, -20)

    # Initialize the new vertices coordination of the new cube
    new_vertices = []

    for vert in vertices:
        # begin a loop for running through the vertices list
        new_vert = []

        new_x = vert[0] + x_value_change
        new_y = vert[1] + y_value_change
        new_z = vert[2] + z_value_change
        new_vert.append(new_x)
        new_vert.append(new_y)
        new_vert.append(new_z)

        new_vertices.append(new_vert)
    return new_vertices

    
def main() -> None:
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
    
    #start further back
    glTranslatef(random.randrange(-5,5), random.randrange(-5, 5), -40)

    # no more rotate
    # glRotatef(25, 2, 1, 0)

    # object_passed = False
    x_move = 0
    y_move = 0
    # Initiate a max distance 
    max_dist = 100
    # make as many cubes as in the range
    cube_dict = {}
    for x in range(20):
        # save the new vertices value to be called in Cube()
        cube_dict[x] = setVertices(max_distance=max_dist)

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
            """
            # Pull the data from the user's mouse wheel, so we can implement zooming feature for our character
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    glTranslatef(0,0,1.0)

                if event.button == 5:
                    glTranslatef(0,0,-1.0)
            """
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_move = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_move =0
        # Acquire our location based off the point of view
        x = glGetDoublev(GL_MODELVIEW_MATRIX)
        # print(x) # check
        # THe modelview matrix will contains X, Y, Z coordinates, which can retrieved like this
        camera_x = x[3][0]
        camera_y = x[3][1]
        camera_z = x[3][2]

        # glRotatef() multiples the current matrix by a rotation matrix | Parameters: angle, x, y, z
        # glRotatef(1, 3, 1, 1)

        # clearing function, we add a couple of special OpenGL spices to let the OpenGL know
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glTranslate(x_move, y_move, 0.50)
        # Once we have a clean canvas, we will call our Cube() function
        for cube in cube_dict:
            Cube(cube_dict[cube])
        pygame.display.flip() # updaet our display
        pygame.time.wait(10)


# Since we only have a cube running and it will end after we pass it, we can produce around 10 cubes for example for display value  
for x in range(10000):
    main()

    # DEBUG: still wondering why the game only displays a single cube, even though we call upon it for 10000 times?

pygame.quit()
quit()
