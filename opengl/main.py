import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random
"""
THis final code is for some optimization on rendering our cubes problem. The main improvements are:
1. Cubes pop up sometimes very close to us, we would want them to start ideally in our far clipping range
2. We want the cubes to follow us every where we go as we use the movement keys.
"""
# Hyperparameters
NUM_CUBES = 30

# represent the coordinates of the vertices of a 3D object, in this cube, we have 8 points (corners)
# more mathematical jargons can be mentioned here, but I will need some further reading
# we will be utilizing these vertices to draw surfaces and edges to represent a 3D cube
vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
    )
# representing the lines to be drawn between the vertices (corners) of the cube
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

# coordinates or index of vertices that will group together into a set to draw the planar surfaces 
surfaces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
    )

# Color reference to display in RGB, with a scale of 0 to 1
# IN the Cube() function, the code will call and iterate upon each set of color to draw
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

ground_surfaces = (0,1,2,3)

ground_vertices = (
    (-10,-0.1,50),
    (10,-0.1,50),
    (-10,-0.1,-300),
    (10,-0.1,-300),

    )

# Creating a ground, wall, ceiling works the same way as making a cube
# the numebr of vertices will be 4 for a planar representation
def Ground():
    glBegin(GL_QUADS)

    x = 0
    for vertex in ground_vertices:
        x+=1
        glColor3fv((0,1,1))
        glVertex3fv(vertex)
        
    glEnd()
    

def setVertices(max_distance, min_distance = 20, camera_x=0, camera_y=0): 
    """
    Create new coordinations for the vertices in the cubes

    Args:
    - max_distance: the farthest distance on the z-axis that we can set
    - min_distance: the nearest distance on the z-axis to set
    - camera_x, camera_y

    Return:
    - None
    """
    # 
    camera_x = -1 * int(camera_x) # use int to round up the current positional values
    camera_y = -1 * int(camera_y)
    # Set the x/y/z value of the coordinate by 0 if you want to fixate on an axis
    # x,y axis for height and width of the cube
    x_value_change = random.randrange(camera_x-75,camera_x + 75)
    y_value_change = random.randrange(camera_y - 75, camera_y + 75)
    # z value represents how far or near the object is in the direction that we are looking into the screen
    z_value_change = random.randrange(-1*max_distance,-20)
    
    new_vertices = []
    for vert in vertices:
        new_vert = []
        new_x= vert[0] + x_value_change
        new_y= vert[1] + y_value_change
        new_z= vert[2] + z_value_change
        # Add the new value created for the new cube's coordinates
        new_vert.append(new_x)
        new_vert.append(new_y)
        new_vert.append(new_z)

        new_vertices.append(new_vert)
    return new_vertices


def Cube(new_vertices):
    glBegin(GL_QUADS)
    for surface in surfaces:
        x = 0
        for vertex in surface:
            x+=1
            glColor3fv(colors[x])
            glVertex3fv(new_vertices[vertex])
    glEnd()

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(new_vertices[vertex])
    glEnd()

    
def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 150.0)
    glTranslatef(random.randrange(-5,5), random.randrange(-5, 5), -40)
    #glTranslatef(0,0, -40)
    x_move = 0
    y_move = 0

    curr_x = 0
    curr_y = 0
    # TODO: we can set this as a hyperparameter
    GAME_SPEED = 2
    DIRECTION_SPEED = 2
    MAX_DISTANCE = 100
    
    cube_dict = {}

    # let's set 20 cubes for one instance now
    for x in range(NUM_CUBES):
        cube_dict[x] = setVertices(MAX_DISTANCE)

    #glRotatef(25, 2, 1, 0)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    x_move = DIRECTION_SPEED
                    
                if event.key == pygame.K_RIGHT:
                    x_move = -1 * DIRECTION_SPEED

                if event.key == pygame.K_UP:
                    y_move = - 1 * DIRECTION_SPEED

                if event.key == pygame.K_DOWN:
                    y_move = DIRECTION_SPEED

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_move = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_move = 0

        x = glGetDoublev(GL_MODELVIEW_MATRIX)

        camera_x = x[3][0]
        camera_y = x[3][1]
        camera_z = x[3][2]

        # Tweak the current speed of the cubes coming at you based on your speed
        curr_x += x_move
        curr_y += y_move

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glTranslatef(x_move,y_move,GAME_SPEED) 

        """
        ONE SPECIAL NOTE FOR GRAPHICS RENDERING: 
        Keep in mind the order of things you are drawing so as not to disorient your depiction of the game and the perception of the users
        Check before committing to the final version
        """
        # temporarily keep the ground function aside for now
        # Ground()
        # looping on to create new cubes by using Cube function
        for each_cube in cube_dict:
            Cube(cube_dict[each_cube])
        # for each cube created and rendered, check if they pass our point of view to create a new one
        for each_cube in cube_dict:
            if camera_z <= cube_dict[each_cube][0][2]:
                # print("passed a cube")
                new_max = int(-1*(camera_z-MAX_DISTANCE))

                cube_dict[each_cube] = setVertices(new_max,int(camera_z-MAX_DISTANCE), curr_x, curr_y)
            
        pygame.display.flip()

            
main()
pygame.quit()
quit()