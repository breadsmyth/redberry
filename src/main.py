import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import config
import input
import opengl_utils

config.init()
pygame.init()
clock = pygame.time.Clock()

pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLEBUFFERS, 1)
pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLESAMPLES, 4)
pygame.display.gl_set_attribute(
    pygame.GL_CONTEXT_PROFILE_MASK,
    pygame.GL_CONTEXT_PROFILE_CORE)
screen = pygame.display.set_mode(
    config.SCREEN_SIZE,
    DOUBLEBUF | OPENGL | FULLSCREEN)

# Get shaders
with open('shaders/test_vertex_shader.vert') as file:
    vert_code = file.read()
with open('shaders/test_fragment_shader.frag') as file:
    frag_code = file.read()

program = opengl_utils.link_program(vert_code, frag_code)
vao = glGenVertexArrays(1)
glBindVertexArray(vao)

glPointSize(10)  # point 10 pixels in diameter
# gluPerspective(45, (config.SCREEN_SIZE[0] / config.SCREEN_SIZE[1]), 0.1, 50.0)
# glTranslatef(0.0, 0.0, -5)

# Main loop
config.RUNNING = True
while config.RUNNING:
    input.process(pygame.event.get())

    glUseProgram(program)
    glDrawArrays(GL_POINTS, 0, 1)

    # glRotatef(1, 3, 1, 1)
    # glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    pygame.display.flip()
    clock.tick(config.FPS)

pygame.quit()
