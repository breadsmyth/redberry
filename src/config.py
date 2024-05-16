import json


# Globals
def init():
    global FPS
    FPS = 120

    # keep track of key inputs
    global KEYS_DOWN
    KEYS_DOWN = []

    global KEYS_PRESSED
    KEYS_PRESSED = []

    global KEYS_UP
    KEYS_UP = []

    global RUNNING
    RUNNING = True

    global SCREEN_SIZE 
    SCREEN_SIZE = (1920, 1080)

    # keep track of total elapsed time
    global TOTAL_TIME
    TOTAL_TIME = 0

    global DELTA_TIME
    DELTA_TIME = 0


def load_from_settings():
    with open ('settings.json') as file:
        settings_json = file.read()

    settings_obj = json.loads(settings_json)

    global FPS
    FPS = settings_obj['fps']

    global SCREEN_SIZE
    SCREEN_SIZE = (
        settings_obj['resolution'][0],
        settings_obj['resolution'][1])

