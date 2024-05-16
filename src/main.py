import pygame
from pygame.locals import *

from OpenGL.GL import *

import config
import render
import input


config.init()
config.load_from_settings()
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
    if input.is_key_down('q'):
        config.RUNNING = False

    render.test()

    pygame.display.flip()
    clock.tick(config.FPS)

    config.DELTA_TIME = clock.get_time() / 1000
    config.TOTAL_TIME += config.DELTA_TIME

pygame.quit()
