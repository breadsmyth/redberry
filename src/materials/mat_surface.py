from OpenGL.GL import *

from materials.mat_basic import Mat_Basic


class Mat_Surface(Mat_Basic):
    def __init__(self, properties={}):
        super().__init__()

        self.settings['draw_style'] = GL_TRIANGLES
        self.settings['double_sided'] = False
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
            glPolygonMode(GL_FRONT_AND_BACK. GL_FILL)
        
        glLineWidth(self.settings['line_width'])