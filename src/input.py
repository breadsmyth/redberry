import pygame

import config


def process(events):
    config.KEYS_DOWN = []
    config.KEYS_UP = []

    for event in events:
        if event.type == pygame.QUIT:
            config.RUNNING = False
        
        elif event.type == pygame.KEYDOWN:
            name = pygame.key.name(event.key)
            config.KEYS_DOWN.append(name)
            config.KEYS_PRESSED.append(name)
        
        elif event.type == pygame.KEYUP:
            name = pygame.key.name(event.key)
            config.KEYS_PRESSED.remove(name)
            config.KEYS_UP.append(name)
    

def is_key_down(key):
    return key in config.KEYS_DOWN
def is_key_pressed(key):
    return key in config.KEYS_PRESSED
def is_key_up(key):
    return key in config.KEYS_UP
