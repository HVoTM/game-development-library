import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random



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

surfaces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
    )


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
    


def Cube():
    glBegin(GL_QUADS)
    for surface in surfaces:
        for vertex in surface:
            x+=1
            glColor3fv(colors[x])
            glVertex3fv(vertices[vertex])
    glEnd()
    
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()
    


def set_vertices(max_distance):
    x_value_change = random.randrange(-5,5)
    y_value_change = 0#random.randrange(-10,10)
    z_value_change = random.randrange(-1*max_distance,-20)


    
    new_vertices = []
    for vert in vertices:
        new_vert = []
        
        
        new_x= vert[0] + x_value_change
        new_y= vert[1] + y_value_change
        new_z= vert[2] + z_value_change
        

        
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

# CUT LINES BC THEY HURT PROCESSING
##    glBegin(GL_LINES)
##    for edge in edges:
##        for vertex in edge:
##            glVertex3fv(new_vertices[vertex])
##    glEnd()

    
def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 150.0)
    glTranslatef(random.randrange(-5,5),0, -20)

    x_move = 0
    y_move = 0

    max_distance = 300

    
    cube_dict = {}

    for x in range(60):
        cube_dict[x] = set_vertices(max_distance)


    object_passed = False

    while not object_passed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    x_move = 0.3
                    
                if event.key == pygame.K_RIGHT:
                    x_move = -0.3

                if event.key == pygame.K_UP:
                    y_move = -0.3

                if event.key == pygame.K_DOWN:
                    y_move = 0.3

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    x_move = 0
                    
                if event.key == pygame.K_RIGHT:
                    x_move = 0

                if event.key == pygame.K_UP:
                    y_move = 0

                if event.key == pygame.K_DOWN:
                    y_move = 0
        
        x = glGetDoublev(GL_MODELVIEW_MATRIX)

        camera_x = x[3][0]
        camera_y = x[3][1]
        camera_z = x[3][2]

        glTranslatef(x_move,y_move,3)

        """
        ONE SPECIAL NOTE FOR GRAPHICS RENDERING: 
        Keep in mind the order of things you are drawing so as not to disorient your depiction of the game and the perception of the users
        Check before committing to the final version
        """
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Ground()
        for each_cube in cube_dict:
            Cube(cube_dict[each_cube])
            
        pygame.display.flip()

            
main()