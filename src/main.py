import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import config
import input
import util.opengl
from util.attribute import Attribute

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


program = util.opengl.link_program(vert_code, frag_code)
glLineWidth(4)


# Triangle
triangle_vao = glGenVertexArrays(1)
glBindVertexArray(triangle_vao)

triangle_pos_data = (
    (-.5, .8, 0),
    (-.2, .2, 0),
    (-.8, .2, 0))

triangle_vertex_count = len(triangle_pos_data)
triangle_attr = Attribute('vec3', triangle_pos_data)
triangle_attr.associate_variable(program, 'position')


# Square
square_vao = glGenVertexArrays(1)
glBindVertexArray(square_vao)

square_pos_data = (
    (.8, .8, 0),
    (.8, .2, 0),
    (.2, .2, 0),
    (.2, .8, 0))

square_vertex_count = len(square_pos_data)
square_attr = Attribute('vec3', square_pos_data)
square_attr.associate_variable(program, 'position')


# Main loop
config.RUNNING = True
glClearColor(.4, .7, .9, 1)
while config.RUNNING:
    input.process(pygame.event.get())

    glUseProgram(program)

    glBindVertexArray(triangle_vao)
    glDrawArrays(GL_LINE_LOOP, 0, triangle_vertex_count)

    glBindVertexArray(square_vao)
    glDrawArrays(GL_LINE_LOOP, 0, square_vertex_count)

    pygame.display.flip()
    clock.tick(config.FPS)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

pygame.quit()
