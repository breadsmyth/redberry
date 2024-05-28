import pygame
from OpenGL.GL import *


class Texture:
    def __init__(self, filename=None, properties={}):
        self.surface = None

        self.tex = glGenTextures(1)

        self.properties = {
            'mag_filter': GL_NEAREST,
            'min_filter': GL_NEAREST_MIPMAP_NEAREST,
            'wrap': GL_REPEAT}
        
        self.set_properties(properties)

        if filename is not None:
            self.load(filename)
            self.upload()
    

    def load(self, filename):
        self.surface = pygame.image.load(filename)
    

    def set_properties(self, properties):
        for name, data in properties.items():
            if name in self.properties.keys():
                self.properties[name] = data
            
            else:
                raise Exception(f'Texture has no property with name {name}')
    

    def upload(self):
        width = self.surface.get_width()
        height = self.surface.get_height()

        pixels = pygame.image.tostring(self.surface, 'RGBA', True)

        glBindTexture(GL_TEXTURE_2D, self.tex)

        glTexImage2D(GL_TEXTURE_2D,     # target
                     0,                 # level
                     GL_RGBA,           # internalformat
                     width,             # width
                     height,            # height
                     0,                 # border
                     GL_RGBA,           # format
                     GL_UNSIGNED_BYTE,  # type
                     pixels)            # data
        
        glGenerateMipmap(GL_TEXTURE_2D)

        glTexParameteri(GL_TEXTURE_2D,
                        GL_TEXTURE_MAG_FILTER,
                        self.properties['mag_filter'])
        glTexParameteri(GL_TEXTURE_2D,
                        GL_TEXTURE_MIN_FILTER,
                        self.properties['min_filter'])
        glTexParameteri(GL_TEXTURE_2D,
                        GL_TEXTURE_WRAP_S,
                        self.properties['wrap'])
        glTexParameteri(GL_TEXTURE_2D,
                        GL_TEXTURE_WRAP_T,
                        self.properties['wrap'])
        
        glTexParameterfv(GL_TEXTURE_2D,
                         GL_TEXTURE_BORDER_COLOR,
                         [1, 1, 1, 1])
