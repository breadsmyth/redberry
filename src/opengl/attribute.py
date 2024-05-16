from OpenGL.GL import *
import numpy


class Attribute:
    def __init__(self, data_type, data):
        # data_type can be: int, float, vec2, vec3, vec4
        self.data_type = data_type
        self.data = data
        self.buffer = glGenBuffers(1)

        self.upload()
    

    def upload(self):
        data = numpy.array(self.data).astype(numpy.float32)
        glBindBuffer(GL_ARRAY_BUFFER, self.buffer)
        glBufferData(GL_ARRAY_BUFFER, data.ravel(), GL_STATIC_DRAW)
    

    def associate_variable(self, program, variable_name):
        variable = glGetAttribLocation(program, variable_name)
        if variable == -1:
            return
        
        glBindBuffer(GL_ARRAY_BUFFER, self.buffer)

        buffer_len = 1
        buffer_type = GL_FLOAT

        match self.data_type:
            case 'int':
                buffer_type = GL_INT
            case 'float':
                pass
            case 'vec2':
                buffer_len = 2
            case 'vec3':
                buffer_len = 3
            case 'vec4':
                buffer_len = 4
            case _:
                raise Exception(
                    f'Attribute {variable_name} has unknown type {self.data_type}')

        glVertexAttribPointer(
            variable, buffer_len, buffer_type, False, 0, None)
        
        glEnableVertexAttribArray(variable)
