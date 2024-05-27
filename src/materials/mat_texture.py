from OpenGL.GL import *

from scene.material import Material


class Mat_Texture(Material):
    def __init__(self, texture, properties={}):
        with open('shaders/texture.vert') as file:
            vert_code = file.read()
        with open('shaders/texture.frag') as file:
            frag_code = file.read()
        
        super().__init__(vert_code, frag_code)

        self.add_uniform('vec3', 'base_color', [1, 1, 1])
        self.add_uniform('sampler2D', 'texture', [texture.tex, 1])
        self.add_uniform('vec2', 'uv_repeat', [1, 1])
        self.add_uniform('vec2', 'uv_offset', [0, 0])
        self.locate_uniforms()

        self.settings['double_sided'] = True
        self.settings['wireframe'] = False
        # only used when wireframe = True
        self.settings['line_width'] = 1

        self.set_properties(properties)


    def update_render_settings(self):
        if self.settings['double_sided']:
            glDisable(GL_CULL_FACE)
        else:
            glEnable(GL_CULL_FACE)
        
        if self.settings['wireframe']:
            glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        else:
            glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        
        glLineWidth(self.settings['line_width'])
