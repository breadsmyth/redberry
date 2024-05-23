from OpenGL.GL import *

from materials.mat_basic import Mat_Basic


class Mat_Line(Mat_Basic):
    def __init__(self, properties={}):
        super().__init__()

        self.settings['draw_style'] = GL_LINE_STRIP
        self.settings['line_width'] = 1
        # valid options: 'connected', 'loop', 'segments'
        self.settings['line_type'] = 'connected'

        self.set_properties(properties)


    def update_render_settings(self):
        glLineWidth(self.settings['line_width'])

        match self.settings['line_type']:
            case 'connected':
                self.settings['draw_style'] = GL_LINE_STRIP
            case 'loop':
                self.settings['draw_style'] = GL_LINE_LOOP
            case 'segments':
                self.settings['draw_style'] = GL_LINES
            case _:
                raise Exception('Unknown draw style in Mat_Line')