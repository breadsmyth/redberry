import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import config
import input

config.init()


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


def draw_cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


pygame.init()
screen_size = (1920, 1080)

clock = pygame.time.Clock()

pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLEBUFFERS, 1)
pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLESAMPLES, 4)
pygame.display.gl_set_attribute(
    pygame.GL_CONTEXT_PROFILE_MASK,
    pygame.GL_CONTEXT_PROFILE_CORE)
screen = pygame.display.set_mode(screen_size, DOUBLEBUF | OPENGL | FULLSCREEN)

gluPerspective(45, (screen_size[0] / screen_size[1]), 0.1, 50.0)

glTranslatef(0.0, 0.0, -5)


# Main loop
config.RUNNING = True
while config.RUNNING:
    input.process(pygame.event.get())

    glRotatef(1, 3, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    draw_cube()

    pygame.display.flip()
    clock.tick(config.FPS)

pygame.quit()
