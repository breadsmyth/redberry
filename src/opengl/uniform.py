from OpenGL.GL import *


class Uniform:
    def __init__(self, data_type, data):
        # data_type can be: int, bool, float, vec2, vec3, vec4, mat4
        self.data_type = data_type
        self.data = data
        self.variable = None


    def locate_variable(self, program, name):
        self.variable = glGetUniformLocation(program, name)


    def upload(self):
        if self.variable == -1:
            return
        
        match self.data_type:
            case 'int' | 'bool':
                glUniform1i(self.variable, self.data)
            case 'float':
                glUniform1f(self.variable, self.data)
            case 'vec2':
                glUniform2f(self.variable,
                            self.data[0], self.data[1])
            case 'vec3':
                glUniform3f(self.variable,
                            self.data[0], self.data[1], self.data[2])
            case 'vec4':
                glUniform4f(self.variable,
                            self.data[0], self.data[1], self.data[2], self.data[3])
            case 'mat4':
                glUniformMatrix4fv(self.variable,
                                  1, GL_TRUE, self.data)
            case 'sampler2D':
                tex_obj, tex_unit = self.data
                glActiveTexture(GL_TEXTURE0 + tex_unit)
                glBindTexture(GL_TEXTURE_2D, tex_obj)
                glUniform1i(self.variable, tex_unit)