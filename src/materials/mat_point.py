from OpenGL.GL import *

from materials.mat_basic import Mat_Basic


class Mat_Point(Mat_Basic):
    def __init__(self, properties={}):
        super().__init__()

        self.settings['draw_style'] = GL_POINTS
        self.settings['point_size'] = 8
        self.settings['rounded_points'] = False

        self.set_properties(properties)


    def update_render_settings(self):
        glPointSize(self.settings['point_size'])

        if self.settings['rounded_points']:
            glEnable(GL_POINT_SMOOTH)
        else:
            glDisable(GL_POINT_SMOOTH)