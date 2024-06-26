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

    # number of seconds in a 24-hour period
    global DAY_LENGTH
    DAY_LENGTH = 10

    # how long it takes for the sun to set/rise (included in DAY_LENGTH)
    global SUNSET_LENGTH
    SUNSET_LENGTH = 2


def load_from_settings():
    with open('settings.json') as file:
        settings_json = file.read()

    settings_obj = json.loads(settings_json)

    global FOV
    FOV = settings_obj['fov']

    global FPS
    FPS = settings_obj['fps']

    global MOUSE_SENSITIVITY
    MOUSE_SENSITIVITY = settings_obj['mouse_sensitivity']

    if MOUSE_SENSITIVITY <= 0:
        raise Exception("settings.json: field 'mouse_sensitivity' must be greater than 0")

    global SCREEN_SIZE
    SCREEN_SIZE = (
        settings_obj['resolution'][0],
        settings_obj['resolution'][1])
    
    global ASPECT_RATIO
    ASPECT_RATIO = SCREEN_SIZE[0] / SCREEN_SIZE[1]

