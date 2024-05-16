import pygame

import config


def process(events):
    for event in events:
        if (event.type == pygame.QUIT):
            config.RUNNING = False
        
        elif event.type == pygame.KEYDOWN:
            process_key(event.key)


def process_key(key):
    match key:
        case pygame.K_q:
            config.RUNNING = False