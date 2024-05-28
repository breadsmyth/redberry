from OpenGL.GL import *

import config
from scene.material import Material


class Mat_Sky(Material):
    def __init__(self, properties={}):
        with open('shaders/point.vert') as file:
            vert_code = file.read()
        with open('shaders/sky.frag') as file:
            frag_code = file.read()
        
        super().__init__(vert_code, frag_code)

        self.add_uniform('float', 'time', 0.0)
        self.add_uniform('float', 'day_length', config.DAY_LENGTH)
        self.add_uniform('float', 'sunset_length', config.SUNSET_LENGTH)
        self.locate_uniforms()

        self.set_properties(properties)