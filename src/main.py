import pygame
from pygame.locals import *

from OpenGL.GL import *

import config
import render
import input


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


render.init()

# Main loop
config.RUNNING = True
while config.RUNNING:
    input.process(pygame.event.get())

    render.test()

    pygame.display.flip()
    clock.tick(config.FPS)

pygame.quit()
