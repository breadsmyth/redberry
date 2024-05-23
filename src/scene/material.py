from OpenGL.GL import *

from opengl import shaders
from opengl.uniform import Uniform


class Material:
    def __init__(self, vert_code, frag_code):
        self.program = shaders.compile(vert_code, frag_code)
        self.uniforms = {}

        self.uniforms['model_matrix']      = Uniform('mat4', None)
        self.uniforms['view_matrix']       = Uniform('mat4', None)
        self.uniforms['projection_matrix'] = Uniform('mat4', None)

        self.settings = {}
        self.settings['draw_style'] = GL_TRIANGLES
    

    def add_uniform(self, data_type, name, data):
        self.uniforms[name] = Uniform(data_type, data)


    def locate_uniforms(self):
        for name, uniform in self.uniforms.items():
            uniform.locate_variable(self.program, name)
    

    def update_render_settings(self):
        pass
    

    def set_properties(self, properties):
        for name, data in properties.items():
            if name in self.uniforms.keys():
                self.uniforms[name].data = data

            elif name in self.settings.keys():
                self.settings[name] = data
            
            else:
                raise Exception(f'Material has no property named {name}')

