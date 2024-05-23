import json


# Globals
def init():
    'initialize constants'

    # keep track of key inputs
    global KEYS_DOWN
    global KEYS_PRESSED
    global KEYS_UP
    KEYS_DOWN = []
    KEYS_PRESSED = []
    KEYS_UP = []

    global RUNNING
    RUNNING = True

    # keep track of total elapsed time
    global TOTAL_TIME
    global DELTA_TIME
    TOTAL_TIME = 0
    DELTA_TIME = 0


def load_from_settings():
    with open('settings.json') as file:
        settings_json = file.read()

    settings_obj = json.loads(settings_json)

    global FOV
    FOV = settings_obj['fov']

    global FPS
    FPS = settings_obj['fps']

    global SCREEN_SIZE
    SCREEN_SIZE = (
        settings_obj['resolution'][0],
        settings_obj['resolution'][1])
    
    global ASPECT_RATIO
    ASPECT_RATIO = SCREEN_SIZE[0] / SCREEN_SIZE[1]

